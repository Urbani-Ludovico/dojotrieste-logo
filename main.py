from elements.judo import judo
from elements.sakura import sakura, sakura_background
from elements.text import text_path
from elements.tori import tori

from utils.parser import parse_args

import drawsvg as draw
import cairosvg

from math import ceil, log10


def main(
        size: int = 1024,
        style: str = "default",
        background: bool = False,
        background_color: str | None = None,
        output: str = "logo.svg"
) -> draw.Drawing:
    #
    # PARAMETERS
    #

    if style == "light":
        main_color = "white"

        if not background:
            background_color = None
        elif background_color is None:
            background_color = "black"
    else:
        main_color = "black"
        
        if not background:
            background_color = None
        elif background_color is None:
            background_color = "white"

    radius = size / 2
    
    round_precision = ceil(max(0, -log10(radius * 4)))
    lround = lambda x: round(x, round_precision)

    #
    # SVG
    #

    svg = draw.Drawing(
        size, size,
        origin = "center",
        fill = main_color,
        stroke = "none",
        stroke_width = 0
    )


    #
    # ELEMENTS
    #

    # Background
    if background_color:
        svg.append(sakura_background(radius = radius, color = background_color, lround = lround))

    # Sun
    svg.append(draw.Circle(
        0, 0, lround(0.42 * radius),
        fill = "#FF8000",
        stroke = "none",
        stroke_width = 0
    ))

    # Tori
    svg.append(tori(radius = radius, lround = lround))

    # Sakura
    svg.append(sakura(radius = radius, lround = lround))

    # Judo kanji
    svg.append(judo(radius = radius, lround = lround))

    # Judo
    svg.append(text_path(
        text = "Judo",
        x = radius * 0.19,
        y = radius * 0.55,
        font_size = radius * 0.17
    ))

    # Dojo
    svg.append(text_path(
        text = "DOJO",
        x = -radius * 0.65,
        y = -radius * 0.225,
        font_size = radius * 0.27
    ))

    # Trieste
    svg.append(text_path(
        text = "Trieste",
        x = -radius * 0.5,
        y = radius * 0.01,
        font_size = radius * 0.22
    ))


    #
    # SAVE
    #
    if output[-4:] == ".svg":
        svg.save_svg(output)

    elif output[-4:] == ".png":
        svg.save_png(output)

    elif output[-4:] == ".pdf":
        svg_data = svg.as_svg()

        if svg_data is None:
            raise ValueError("SVG data is None, cannot convert to PDF.")
        
        cairosvg.svg2pdf(bytestring = svg_data.encode("utf-8"), write_to = output)

    return svg


if __name__ == "__main__":
    main(**vars(parse_args()))
