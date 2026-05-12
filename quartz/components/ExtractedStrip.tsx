import { QuartzComponent, QuartzComponentConstructor } from "./types"
// @ts-ignore
import script from "./scripts/extracted.inline"

const ExtractedStrip: QuartzComponent = () => {
  return <div style="display:none" id="extracted-strip" />
}

ExtractedStrip.afterDOMLoaded = script

export default (() => ExtractedStrip) satisfies QuartzComponentConstructor
