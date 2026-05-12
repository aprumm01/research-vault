function stripExtracted() {
  document.querySelectorAll("article ul li, article ol li").forEach((li) => {
    if (!li.textContent?.includes("[EXTRACTED]")) return
    const firstLink = li.querySelector("a")
    if (!firstLink) return
    let node: ChildNode | null = firstLink.nextSibling
    while (node) {
      const next = node.nextSibling
      li.removeChild(node)
      node = next
    }
  })
}

document.addEventListener("nav", stripExtracted)
stripExtracted()
