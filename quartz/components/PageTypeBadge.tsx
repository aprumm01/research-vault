import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const PageTypeBadge: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
  const slug = fileData.slug ?? ""
  const title = fileData.frontmatter?.title ?? slug

  // Don't show badge on index
  if (slug === "index") return null

  // Community cluster pages
  if (title.startsWith("_COMMUNITY_") || slug.startsWith("_COMMUNITY_")) {
    return (
      <div class="page-type-badge badge-community">
        <span class="badge-dot" />
        Community Cluster
      </div>
    )
  }

  // Research paper pages — titles contain parenthesised author/institution info
  const looksLikePaper = /\(.*?\)/.test(title) || title.includes(" et al")
  if (looksLikePaper) {
    return (
      <div class="page-type-badge badge-article">
        <span class="badge-dot" />
        Research Paper
      </div>
    )
  }

  // Topic / concept pages
  return (
    <div class="page-type-badge badge-topic">
      <span class="badge-dot" />
      Topic / Concept
    </div>
  )
}

PageTypeBadge.css = `
  .page-type-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.45em;
    padding: 0.28em 0.75em;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    font-family: var(--bodyFont);
    border: 1.5px solid currentColor;
  }

  .badge-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: currentColor;
    flex-shrink: 0;
  }

  /* Community — warm amber */
  .badge-community {
    color: var(--secondary);
    background: color-mix(in srgb, var(--secondary) 10%, transparent);
    border-color: color-mix(in srgb, var(--secondary) 35%, transparent);
  }

  /* Research paper — teal/green */
  .badge-article {
    color: #3d8b6e;
    background: rgba(61, 139, 110, 0.1);
    border-color: rgba(61, 139, 110, 0.3);
  }

  /* Topic — slate blue */
  .badge-topic {
    color: #4a6fa5;
    background: rgba(74, 111, 165, 0.1);
    border-color: rgba(74, 111, 165, 0.3);
  }

  :root[saved-theme="dark"] .badge-article {
    color: #6ecfaa;
    background: rgba(110, 207, 170, 0.12);
    border-color: rgba(110, 207, 170, 0.3);
  }

  :root[saved-theme="dark"] .badge-topic {
    color: #87aadb;
    background: rgba(135, 170, 219, 0.12);
    border-color: rgba(135, 170, 219, 0.3);
  }
`

export default (() => PageTypeBadge) satisfies QuartzComponentConstructor
