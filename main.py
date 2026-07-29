from elements.sakura import sakura, sakura_background
from elements.tori import tori

from utils.parser import parse_args

import drawsvg as draw


def main(
        size: int = 1024,
        main_color: str = "black",
        background: str | None = "white",
        output: str | None = "logo.svg"
) -> draw.Drawing:
    #
    # SVG
    #

    radius = size / 2

    svg = draw.Drawing(
        size, size,
        origin = "center"
    )


    #
    # ELEMENTS
    #

    # Background
    if background is not None:
        svg.append(sakura_background(radius = radius))

    # Sun
    svg.append(draw.Circle(
        0, 0, 210,
        fill = "#FF8000",
        stroke = "none",
        stroke_width = 0
    ))

    # Pagoda
    svg.append(tori(radius = radius, color = main_color))

    # Sakura
    svg.append(sakura(radius = radius))


    #
    # SAVE
    #

    if output[-4:] == ".svg":
        svg.save_svg(output)

    return svg


if __name__ == "__main__":
    main(**vars(parse_args()))