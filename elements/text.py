import drawsvg as draw
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen


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
    x_cursor = x

    group = draw.Group()

    for char in text:
        glyph_name = cmap.get(ord(char))
        if glyph_name and glyph_name in glyph_set:
            pen = SVGPathPen(glyph_set)
            
            # Flip Y-axis (OTF use Y-up; SVG uses Y-down)
            tpen = TransformPen(pen, (scale, 0.0, 0.0, -scale, x_cursor, y))
            glyph_set[glyph_name].draw(tpen)

            path_d = pen.getCommands()
            if path_d:
                group.append(draw.Path(d=path_d))

            advance_width = hmtx[glyph_name][0]
            x_cursor += advance_width * scale

    return group