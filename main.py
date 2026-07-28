from sakura import sakura, sakura_background
from tori import tori

import drawsvg as draw


##########################################
# PARAMETERS                             #
##########################################

size = 1024

main_color: str = "black"
background: str | None = "white"


##########################################
# SVG                                    #
##########################################

radius = size / 2

svg = draw.Drawing(
    size, size,
    origin = "center"
)


##########################################
# ELEMENTS                               #
##########################################

#
# Background
#

if background is not None:
    svg.append(sakura_background(radius = radius))


#
# Sun
#

svg.append(draw.Circle(
    0, 0, 210,
    fill = "#FF8000",
    stroke = "none",
    stroke_width = 0
))


#
# Pagoda
#

svg.append(tori(radius = radius, color = main_color))


#
# Sakura
#

svg.append(sakura(radius = radius))


########################################
# SAVE SVG                             #
########################################

svg.save_svg("logo.svg")