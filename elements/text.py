import drawsvg as draw
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.filterPen import FilterPen


class RoundingPen(FilterPen):
    """Intercepts pen drawing commands and rounds coordinates to a specified precision."""
    def __init__(self, out_pen, precision=4):
        super().__init__(out_pen)
        self.precision = precision

    def _round_pt(self, pt):
        return (round(pt[0], self.precision), round(pt[1], self.precision))

    def moveTo(self, pt):
        self._outPen.moveTo(self._round_pt(pt))

    def lineTo(self, pt):
        self._outPen.lineTo(self._round_pt(pt))

    def curveTo(self, *pts):
        self._outPen.curveTo(*[self._round_pt(p) for p in pts])

    def qCurveTo(self, *pts):
        self._outPen.qCurveTo(*[self._round_pt(p) for p in pts])


def text_path(
        text: str,
        x: float,
        y: float,
        font_size: float
) -> draw.Group:
    font = TTFont("elements/font.otf")

    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    units_per_em = font["head"].unitsPerEm

    scale = font_size / units_per_em
    x_cursor = round(x, 4)
    y = round(y, 4)

    group = draw.Group()

    for char in text:
        glyph_name = cmap.get(ord(char))
        if glyph_name and glyph_name in glyph_set:
            svg_pen = SVGPathPen(glyph_set)
            
            # Wrap SVGPathPen inside RoundingPen
            rpen = RoundingPen(svg_pen, precision=4)
            
            # Flip Y-axis (OTF uses Y-up; SVG uses Y-down)
            tpen = TransformPen(rpen, (scale, 0.0, 0.0, -scale, x_cursor, y))
            glyph_set[glyph_name].draw(tpen)

            path_d = svg_pen.getCommands()
            if path_d:
                group.append(draw.Path(d=path_d))

            advance_width = hmtx[glyph_name][0]
            x_cursor = round(x_cursor + advance_width * scale, 4)

    return group