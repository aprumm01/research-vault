import { QuartzComponent, QuartzComponentConstructor } from "./types"
// @ts-ignore
import script from "./scripts/vaultquery.inline"
import style from "./styles/vaultquery.scss"

const VaultQuery: QuartzComponent = () => {
  return (
    <div id="vault-query-root">
      {/* Floating trigger button */}
      <button id="vq-trigger" aria-label="Ask Claude" title="Ask Claude about your research">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
        </svg>
        <span>Ask Claude</span>
      </button>

      {/* Query panel */}
      <div id="vq-panel" aria-hidden="true">
        <div id="vq-header">
          <span id="vq-title">Ask Claude</span>
          <span id="vq-context-label"></span>
          <button id="vq-close" aria-label="Close">✕</button>
        </div>

        <div id="vq-response-area" aria-live="polite">
          <p id="vq-placeholder">Ask a question about your research. Claude will search your vault notes for relevant context.</p>
          <div id="vq-response-text"></div>
        </div>

        <div id="vq-actions" style="display:none">
          <button id="vq-copy" title="Copy to clipboard">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
            </svg>
            Copy
          </button>
          <button id="vq-download" title="Download as markdown">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>
            </svg>
            Download
          </button>
          <span id="vq-sources-label"></span>
        </div>

        <div id="vq-input-row">
          <textarea
            id="vq-input"
            placeholder="Ask about your research…"
            rows={2}
            aria-label="Ask Claude a question"
          />
          <button id="vq-submit">Ask</button>
        </div>
      </div>
    </div>
  )
}

VaultQuery.afterDOMLoaded = script
VaultQuery.css = style

export default (() => VaultQuery) satisfies QuartzComponentConstructor
