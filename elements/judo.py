import drawsvg as draw


def judo(
        radius: int,
        color: str
) -> draw.Group:
    coords = lambda x, y: (x * radius, y * radius)

    group = draw.Group(
        fill = "none",
        stroke = "green",
        stroke_width = 1,
        opacity = 0.5
    )

    # First kanji - top part
    group.append(path := draw.Path())
    path.M(*coords(0.4707, -0.3008))
    path.C(*coords(0.498, -0.2891), *coords(0.5029, -0.3027), *coords(0.499, -0.333))
    path.C(*coords(0.4297, -0.2734), *coords(0.3906, -0.2715), *coords(0.3428, -0.2607))
    path.C(*coords(0.3711, -0.2793), *coords(0.4102, -0.2988), *coords(0.4561, -0.3486))
    path.C(*coords(0.3906, -0.3359), *coords(0.3672, -0.3184), *coords(0.3516, -0.3428))
    path.S(*coords(0.3516, -0.3613), *coords(0.3906, -0.3662))
    path.S(*coords(0.459, -0.377), *coords(0.4824, -0.3828))
    path.C(*coords(0.4492, -0.4326), *coords(0.4492, -0.4326), *coords(0.5078, -0.4189))
    path.C(*coords(0.5605, -0.4629), *coords(0.5078, -0.4492), *coords(0.4688, -0.4395))
    path.S(*coords(0.4102, -0.4102), *coords(0.3867, -0.4688))
    path.C(*coords(0.4102, -0.459), *coords(0.5039, -0.4688), *coords(0.5459, -0.4893))
    path.C(*coords(0.5723, -0.4785), *coords(0.5977, -0.4609), *coords(0.6074, -0.4492))
    path.C(*coords(0.6211, -0.4277), *coords(0.5859, -0.4395), *coords(0.5234, -0.4062))
    path.C(*coords(0.5244, -0.4023), *coords(0.5244, -0.3965), *coords(0.5234, -0.3926))
    path.C(*coords(0.5996, -0.418), *coords(0.6006, -0.415), *coords(0.6445, -0.3887))
    path.S(*coords(0.6699, -0.3535), *coords(0.6406, -0.3496))
    path.S(*coords(0.5449, -0.3047), *coords(0.5811, -0.3457))
    path.S(*coords(0.5273, -0.3613), *coords(0.5176, -0.3604))
    path.C(*coords(0.5605, -0.3398), *coords(0.5576, -0.2598), *coords(0.5117, -0.2441))
    path.C(*coords(0.5039, -0.25), *coords(0.4766, -0.2891), *coords(0.4658, -0.2959))
    path.Z()

    return group