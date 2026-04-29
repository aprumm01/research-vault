import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/aprumm01/research-vault",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.PageTypeBadge(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.CitationBlock(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      sortFn: (a, b) => {
        const folderOrder = ["communities", "topics", "papers", "authors"]
        if (a.isFolder && b.isFolder) {
          const ai = folderOrder.indexOf(a.slugSegment ?? "")
          const bi = folderOrder.indexOf(b.slugSegment ?? "")
          if (ai !== -1 || bi !== -1) {
            const av = ai !== -1 ? ai : 99
            const bv = bi !== -1 ? bi : 99
            return av - bv
          }
          return a.displayName.localeCompare(b.displayName, undefined, { numeric: true, sensitivity: "base" })
        }
        if (!a.isFolder && !b.isFolder) {
          return a.displayName.localeCompare(b.displayName, undefined, { numeric: true, sensitivity: "base" })
        }
        return a.isFolder ? -1 : 1
      },
    }),
  ],
  right: [
    Component.Graph({
      localGraph: {
        showTags: false,
        scale: 1.4,
        repelForce: 0.6,
        linkDistance: 40,
        fontSize: 0.55,
        focusOnHover: true,
      },
      globalGraph: {
        showTags: false,
        depth: 2,
        scale: 1.1,
        repelForce: 0.9,
        linkDistance: 65,
        fontSize: 0.6,
        opacityScale: 0,
        focusOnHover: true,
        enableRadial: false,
      },
    }),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      sortFn: (a, b) => {
        const folderOrder = ["communities", "topics", "papers", "authors"]
        if (a.isFolder && b.isFolder) {
          const ai = folderOrder.indexOf(a.slugSegment ?? "")
          const bi = folderOrder.indexOf(b.slugSegment ?? "")
          if (ai !== -1 || bi !== -1) {
            const av = ai !== -1 ? ai : 99
            const bv = bi !== -1 ? bi : 99
            return av - bv
          }
          return a.displayName.localeCompare(b.displayName, undefined, { numeric: true, sensitivity: "base" })
        }
        if (!a.isFolder && !b.isFolder) {
          return a.displayName.localeCompare(b.displayName, undefined, { numeric: true, sensitivity: "base" })
        }
        return a.isFolder ? -1 : 1
      },
    }),
  ],
  right: [],
}
