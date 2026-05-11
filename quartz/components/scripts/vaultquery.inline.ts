const API_URL = "https://vault-query-umber.vercel.app/api/query"

function getPageContext(): { title: string; content: string } {
  const title = document.querySelector("h1.article-title")?.textContent?.trim() ?? document.title
  const articleEl = document.querySelector("article") ?? document.querySelector(".popover-hint")
  const content = articleEl?.innerText?.slice(0, 3000) ?? ""
  return { title, content }
}

function setupVaultQuery() {
  const trigger = document.getElementById("vq-trigger")
  const panel = document.getElementById("vq-panel")
  const closeBtn = document.getElementById("vq-close")
  const input = document.getElementById("vq-input") as HTMLTextAreaElement
  const submitBtn = document.getElementById("vq-submit") as HTMLButtonElement
  const responseText = document.getElementById("vq-response-text") as HTMLElement
  const placeholder = document.getElementById("vq-placeholder") as HTMLElement
  const actions = document.getElementById("vq-actions") as HTMLElement
  const copyBtn = document.getElementById("vq-copy") as HTMLButtonElement
  const downloadBtn = document.getElementById("vq-download") as HTMLButtonElement
  const sourcesLabel = document.getElementById("vq-sources-label") as HTMLElement
  const contextLabel = document.getElementById("vq-context-label") as HTMLElement

  if (!trigger || !panel) return

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

  trigger.addEventListener("click", () => (isOpen ? close() : open()))
  closeBtn?.addEventListener("click", close)

  // Close on Escape
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOpen) close()
  })

  // Submit on Ctrl/Cmd+Enter
  input?.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault()
      submitBtn.click()
    }
  })

  async function submit() {
    const query = input.value.trim()
    if (!query) return

    const { content: pageContent, title: pageTitle } = getPageContext()

    submitBtn.disabled = true
    submitBtn.textContent = "…"
    placeholder.style.display = "none"
    actions.style.display = "none"
    responseText.textContent = ""
    responseText.classList.add("loading")
    currentResponse = ""

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query, pageContent, pageTitle }),
      })

      if (!res.ok) throw new Error(`API error ${res.status}`)

      const reader = res.body!.getReader()
      const decoder = new TextDecoder()
      let buffer = ""
      let sources: string[] = []

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
      actions.style.display = "flex"
      sourcesLabel.textContent = sources.length ? `${sources.length} source${sources.length > 1 ? "s" : ""}` : ""
      sourcesLabel.title = sources.join("\n")
    } catch (err) {
      responseText.classList.remove("loading")
      responseText.textContent = "Something went wrong. Please try again."
      console.error(err)
    } finally {
      submitBtn.disabled = false
      submitBtn.textContent = "Ask"
    }
  }

  submitBtn?.addEventListener("click", submit)

  copyBtn?.addEventListener("click", () => {
    if (!currentResponse) return
    navigator.clipboard.writeText(currentResponse).then(() => {
      copyBtn.textContent = "Copied!"
      setTimeout(() => {
        copyBtn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy`
      }, 1500)
    })
  })

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
  })
}

document.addEventListener("nav", setupVaultQuery)
