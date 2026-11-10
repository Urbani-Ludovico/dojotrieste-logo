from elements.judo import judo
from elements.sakura import sakura, sakura_background
from elements.text import text_path
from elements.tori import tori

from utils.parser import parse_args
from utils.check_parameters import check_parameters

import drawsvg as draw
import cairosvg

from math import ceil, log10


def main(
        size: int = 1024,
        main_color: str = "white",
        background: str | None = None,
        output: str | None = "logo.svg"
) -> draw.Drawing:
    check_parameters(
        size = size,
        main_color = main_color,
        background = background,
        output = output
    )

    #
    # SVG
    #

    radius = size / 2
    round_precision = ceil(max(0, -log10(radius * 4)))

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
    if background is not None:
        svg.append(sakura_background(radius = radius, color = background, round_precision = round_precision))

    # Sun
    svg.append(draw.Circle(
        0, 0, round(0.42 * radius, round_precision),
        fill = "#FF8000",
        stroke = "none",
        stroke_width = 0
    ))

    # Tori
    svg.append(tori(radius = radius, round_precision = round_precision))

    # Sakura
    svg.append(sakura(radius = radius, round_precision = round_precision))

    # Judo kanji
    svg.append(judo(radius = radius, round_precision = round_precision))

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
    if not output:
        svg.set_render_size(400)
        svg.rasterize()
        
    elif output[-4:] == ".svg":
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
