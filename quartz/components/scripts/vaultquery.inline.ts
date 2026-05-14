const API_URL = "https://vault-query-umber.vercel.app/api/query"
const QUARTZ_BASE = "https://aprumm01.github.io/research-vault"

function renderMarkdown(text: string): string {
  const escaped = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")

  function inline(s: string): string {
    return s
      .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\*(.+?)\*/g, "<em>$1</em>")
      .replace(/`(.+?)`/g, "<code>$1</code>")
  }

  const lines = escaped.split("\n")
  const out: string[] = []
  let inList = false

  for (const line of lines) {
    if (line.startsWith("### ")) {
      if (inList) { out.push("</ul>"); inList = false }
      out.push(`<h3>${inline(line.slice(4))}</h3>`)
    } else if (line.match(/^#{1,2} /)) {
      if (inList) { out.push("</ul>"); inList = false }
      out.push(`<h2>${inline(line.replace(/^#{1,2} /, ""))}</h2>`)
    } else if (line.match(/^[-*] /)) {
      if (!inList) { out.push("<ul>"); inList = true }
      out.push(`<li>${inline(line.slice(2))}</li>`)
    } else if (line.trim() === "") {
      if (inList) { out.push("</ul>"); inList = false }
    } else {
      if (inList) { out.push("</ul>"); inList = false }
      out.push(`<p>${inline(line)}</p>`)
    }
  }

  if (inList) out.push("</ul>")
  return out.join("")
}

function noteUrl(path: string): string {
  const slug = path.replace(/\.md$/, "").split("/").map(encodeURIComponent).join("/")
  return `${QUARTZ_BASE}/${slug}`
}

function getPageContext(): { title: string; content: string } {
  const title = document.querySelector("h1.article-title")?.textContent?.trim() ?? document.title
  const articleEl = document.querySelector("article") ?? document.querySelector(".popover-hint")
  const content = articleEl?.innerText?.slice(0, 3000) ?? ""
  return { title, content }
}

let vqController: AbortController | null = null

function setupVaultQuery() {
  const trigger = document.getElementById("vq-trigger")
  const panel = document.getElementById("vq-panel")
  const closeBtn = document.getElementById("vq-close")
  const input = document.getElementById("vq-input") as HTMLTextAreaElement
  const submitBtn = document.getElementById("vq-submit") as HTMLButtonElement
  const responseText = document.getElementById("vq-response-text") as HTMLElement
  const sourcesList = document.getElementById("vq-sources-list") as HTMLElement
  const placeholder = document.getElementById("vq-placeholder") as HTMLElement
  const actions = document.getElementById("vq-actions") as HTMLElement
  const copyBtn = document.getElementById("vq-copy") as HTMLButtonElement
  const downloadBtn = document.getElementById("vq-download") as HTMLButtonElement
  const sourcesLabel = document.getElementById("vq-sources-label") as HTMLElement
  const contextLabel = document.getElementById("vq-context-label") as HTMLElement

  if (!trigger || !panel) return

  // Abort any listeners from a previous nav so we don't accumulate duplicates
  vqController?.abort()
  vqController = new AbortController()
  const { signal } = vqController

  let currentResponse = ""
  let isOpen = false

  function open() {
    isOpen = true
    panel!.classList.add("open")
    panel!.setAttribute("aria-hidden", "false")
    const { title } = getPageContext()
    contextLabel.textContent = title ? `Context: ${title}` : ""
    setTimeout(() => input?.focus(), 50)
  }

  function close() {
    isOpen = false
    panel!.classList.remove("open")
    panel!.setAttribute("aria-hidden", "true")
  }

  trigger.addEventListener("click", () => (isOpen ? close() : open()), { signal })
  closeBtn?.addEventListener("click", close, { signal })

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOpen) close()
  }, { signal })

  input?.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault()
      submitBtn.click()
    }
  }, { signal })

  async function submit() {
    const query = input.value.trim()
    if (!query) return

    submitBtn.disabled = true
    submitBtn.textContent = "…"
    placeholder.style.display = "none"
    actions.style.display = "none"
    responseText.innerHTML = ""
    responseText.classList.add("loading")
    if (sourcesList) sourcesList.innerHTML = ""
    currentResponse = ""

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      })

      if (!res.ok) throw new Error(`API error ${res.status}`)

      const reader = res.body!.getReader()
      const decoder = new TextDecoder()
      let buffer = ""
      let sources: { title: string; path: string }[] = []

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split("\n\n")
        buffer = lines.pop() ?? ""

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue
          const data = JSON.parse(line.slice(6))
          if (data.type === "sources") {
            sources = data.sources ?? []
          } else if (data.type === "text") {
            currentResponse += data.text
            responseText.textContent = currentResponse
          }
        }
      }

      responseText.classList.remove("loading")
      responseText.innerHTML = renderMarkdown(currentResponse)

      if (sources.length) {
        const heading = document.createElement("p")
        heading.className = "vq-sources-heading"
        heading.textContent = `Sources (${sources.length})`
        sourcesList.appendChild(heading)

        const ul = document.createElement("ul")
        for (const src of sources) {
          const li = document.createElement("li")
          const a = document.createElement("a")
          a.href = noteUrl(src.path)
          a.textContent = src.title
          a.target = "_blank"
          a.rel = "noopener noreferrer"
          li.appendChild(a)
          ul.appendChild(li)
        }
        sourcesList.appendChild(ul)
        sourcesLabel.textContent = `${sources.length} source${sources.length > 1 ? "s" : ""}`
      } else {
        sourcesLabel.textContent = ""
      }

      actions.style.display = "flex"
    } catch (err) {
      responseText.classList.remove("loading")
      responseText.textContent = "Something went wrong. Please try again."
      console.error(err)
    } finally {
      submitBtn.disabled = false
      submitBtn.textContent = "Ask"
    }
  }

  submitBtn?.addEventListener("click", submit, { signal })

  copyBtn?.addEventListener("click", () => {
    if (!currentResponse) return
    navigator.clipboard.writeText(currentResponse).then(() => {
      copyBtn.textContent = "Copied!"
      setTimeout(() => {
        copyBtn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy`
      }, 1500)
    })
  }, { signal })

  downloadBtn?.addEventListener("click", () => {
    if (!currentResponse) return
    const { title } = getPageContext()
    const filename = `claude-response-${title.replace(/[^a-z0-9]/gi, "-").toLowerCase() || "response"}.md`
    const blob = new Blob([currentResponse], { type: "text/markdown" })
    const url = URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = filename
    a.click()
    URL.revokeObjectURL(url)
  }, { signal })
}

document.addEventListener("nav", setupVaultQuery)
