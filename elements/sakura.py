import drawsvg as draw
from math import sin, cos, pi
from typing import Callable

def sakura(
        radius: int | float,
        lround: Callable[[float], float],
        petals_number: int = 8,
        outer_radius_percentage: float = 1,
        inner_radius_percentage: float = 0.92,
        c_x_outer_angle_percentage: float = 0.115,
        c_x_inner_angle_percentage: float = 0.3,
        outer_c_x_outer_radius_percentage: float = 0.863,
        inner_c_x_outer_radius_percentage: float = 0.9,
        outer_c_x_inner_radius_percentage: float = 0.982,
        inner_c_x_inner_radius_percentage: float = 1.018,
        radius_inner_percentage: float = 0.85
) -> draw.Path:
    """
    Args:
        radius
        petals_number
        outer_radius_percentage: radius of the outer line, in percentage of image radius
        inner_radius_percentage: radius of the inner line, in percentage of image radius
        c_x_outer_angle_percentage: percentage of half petal angle for outer point of C curve
        c_x_inner_angle_percentage: percentage of half petal angle for inner point of C curve
        outer_c_x_outer_radius_percentage: percentage on line radius for radius for outer point of C outer curve
        inner_c_x_outer_radius_percentage: percentage on line radius for radius for outer point of C inner curve
        outer_c_x_inner_radius_percentage: percentage on line radius for radius for inner point of C outer curve
        inner_c_x_inner_radius_percentage: percentage on line radius for radius for inner point of C inner curve
        radius_inner_percentage: percentage of radius for inner point of the line
        main_color
    """

    path = draw.Path(
        fill_rule = "evenodd"
    )


    #
    # OUTER
    #

    sakura_loop(
        path,
        radius = radius * outer_radius_percentage,
        petals_number = petals_number,
        lround = lround,
        c_x_outer_angle = c_x_outer_angle_percentage * pi / petals_number,
        c_x_inner_angle = c_x_inner_angle_percentage * pi / petals_number,
        c_x_outer_radius = radius * outer_radius_percentage * outer_c_x_outer_radius_percentage,
        c_x_inner_radius = radius * outer_radius_percentage * outer_c_x_inner_radius_percentage,
        radius_inner_percentage = radius_inner_percentage
    )


    #
    # INNER
    #

    sakura_loop(
        path,
        radius = radius * inner_radius_percentage,
        petals_number = petals_number,
        lround = lround,
        c_x_outer_angle = c_x_outer_angle_percentage * pi / petals_number,
        c_x_inner_angle = c_x_inner_angle_percentage * pi / petals_number,
        c_x_outer_radius = radius * inner_radius_percentage * inner_c_x_outer_radius_percentage,
        c_x_inner_radius = radius * inner_radius_percentage * inner_c_x_inner_radius_percentage,
        radius_inner_percentage = radius_inner_percentage
    )


    return path


def sakura_background(
        radius: int | float,
        color: str,
        lround: Callable[[float], float],
        petals_number: int = 8,
        inner_radius_percentage: float = 0.92,
        c_x_outer_angle_percentage: float = 0.115,
        c_x_inner_angle_percentage: float = 0.3,
        inner_c_x_outer_radius_percentage: float = 0.9,
        inner_c_x_inner_radius_percentage: float = 1.018,
        radius_inner_percentage: float = 0.85
):
    """
    Args:
        radius
        petals_number
        inner_radius_percentage: radius of the inner line, in percentage of image radius
        c_x_outer_angle_percentage: percentage of half petal angle for outer point of C curve
        c_x_inner_angle_percentage: percentage of half petal angle for inner point of C curve
        inner_c_x_outer_radius_percentage: percentage on line radius for radius for outer point of C inner curve
        inner_c_x_inner_radius_percentage: percentage on line radius for radius for inner point of C inner curve
        radius_inner_percentage: percentage of radius for inner point of the line
        color
    """
    
    path = draw.Path(
        fill = color
    )

    sakura_loop(
        path,
        radius = radius * inner_radius_percentage * 1.01,
        petals_number = petals_number,
        lround = lround,
        c_x_outer_angle = c_x_outer_angle_percentage * pi / petals_number,
        c_x_inner_angle = c_x_inner_angle_percentage * pi / petals_number,
        c_x_outer_radius = radius * inner_radius_percentage * inner_c_x_outer_radius_percentage,
        c_x_inner_radius = radius * inner_radius_percentage * inner_c_x_inner_radius_percentage,
        radius_inner_percentage = radius_inner_percentage
    )
    
    return path


def sakura_loop(
        path: draw.Path,
        radius: int | float,
        petals_number: int,
        lround: Callable[[float], float],
        c_x_outer_angle: float,
        c_x_inner_angle: float,
        c_x_outer_radius: float,
        c_x_inner_radius: float,
        radius_inner_percentage: float
) -> draw.Path:
    path.M(lround(radius), 0)

    for i in range(1, 2 * petals_number + 1):
        if i % 2 == 0:
            path.C(
                lround(c_x_inner_radius * cos((i - 1) * pi / petals_number + c_x_inner_angle)),
                lround(c_x_inner_radius * sin((i - 1) * pi / petals_number + c_x_inner_angle)),
                lround(c_x_outer_radius * cos(i * pi / petals_number - c_x_outer_angle)),
                lround(c_x_outer_radius * sin(i * pi / petals_number - c_x_outer_angle)),
                lround(radius * cos(i * pi / petals_number)),
                lround(radius * sin(i * pi / petals_number))
            )
        else:
            path.C(
                lround(c_x_outer_radius * cos((i - 1) * pi / petals_number + c_x_outer_angle)),
                lround(c_x_outer_radius * sin((i - 1) * pi / petals_number + c_x_outer_angle)),
                lround(c_x_inner_radius * cos(i * pi / petals_number - c_x_inner_angle)),
                lround(c_x_inner_radius * sin(i * pi / petals_number - c_x_inner_angle)),
                lround(radius * radius_inner_percentage * cos(i * pi / petals_number)),
                lround(radius * radius_inner_percentage * sin(i * pi / petals_number))
            )

    path.Z()

    return path