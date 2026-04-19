import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const CitationBlock: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
  const fm = fileData.frontmatter
  if (!fm) return null

  // Only render for research papers (has a source PDF)
  const sourceFile = (fm.source_file as string) ?? ""
  if (sourceFile === "") return null

  const authors = fm.authors as string | undefined
  const year = fm.year as string | number | undefined
  const venue = fm.venue as string | undefined
  const doi = fm.doi as string | undefined

  // Nothing to show yet
  if (!authors && !year && !venue && !doi) return null

  return (
    <div class="citation-block">
      {authors && <div class="citation-authors">{authors}</div>}
      {(year || venue) && (
        <div class="citation-meta">
          {year && <span class="citation-year">{year}</span>}
          {year && venue && <span class="citation-sep"> · </span>}
          {venue && <span class="citation-venue">{venue}</span>}
        </div>
      )}
      {doi && (
        <a
          class="citation-doi"
          href={`https://doi.org/${doi}`}
          target="_blank"
          rel="noopener noreferrer"
        >
          ↗ doi:{doi}
        </a>
      )}
    </div>
  )
}

CitationBlock.css = `
  .citation-block {
    display: flex;
    flex-direction: column;
    gap: 0.3em;
    padding: 0.7em 1em;
    border-left: 3px solid var(--secondary);
    background: color-mix(in srgb, var(--secondary) 5%, var(--light));
    border-radius: 0 6px 6px 0;
    margin: 0.25rem 0 1.25rem 0;
    font-family: var(--bodyFont);
  }

  .citation-authors {
    font-size: 0.88rem;
    font-weight: 500;
    color: var(--darkgray);
    line-height: 1.45;
  }

  .citation-meta {
    font-size: 0.82rem;
    color: var(--gray);
  }

  .citation-year {
    font-weight: 600;
    color: var(--secondary);
  }

  .citation-sep {
    opacity: 0.5;
  }

  .citation-venue {
    font-style: italic;
  }

  .citation-doi {
    font-size: 0.78rem;
    color: var(--secondary);
    text-decoration: none;
    opacity: 0.85;
    font-family: var(--codeFont);
    word-break: break-all;
  }

  .citation-doi:hover {
    opacity: 1;
    text-decoration: underline;
  }
`

export default (() => CitationBlock) satisfies QuartzComponentConstructor
