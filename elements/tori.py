import drawsvg as draw


def tori(
        radius: int,
        color: str
) -> draw.Group:
    coord = lambda x: x * radius
    coords = lambda x, y: (x * radius, y * radius)

    def arrow(path: draw.Path, x: float, y: float) -> None:
        path.H(coord(x := x - 0.0234))
        path.V(coord(y := y - 0.0156))
        path.L(*coords(x := x - 0.0176, y := y - 0.0059))
        path.L(*coords(x := x + 0.0605, y := y - 0.0117))
        path.L(*coords(x := x + 0.0605, y := y + 0.0117))
        path.L(*coords(x := x - 0.0176, y := y + 0.0059))
        path.V(coord(y := y + 0.0156))
        path.H(coord(x := x - 0.0234))

    group = draw.Group(
        fill = color,
        stroke = "none",
        stroke_width = 0
    )

    # Architrave
    group.append(path := draw.Path())
    path.M(*coords(-0.6487, 0.2129))
    path.C(*coords(-0.6428, 0.1953), *coords(-0.6428, 0.1562), *coords(-0.6495, 0.123))
    path.C(*coords(-0.4883, 0.1953), *coords(0.0977, 0.1495), *coords(0.2676, 0.0488))
    path.C(*coords(0.252, 0.0781), *coords(0.2539, 0.1367), *coords(0.2598, 0.1562))
    path.L(*coords(0.1504, 0.1875))
    path.L(*coords(0.1406, 0.2275))
    path.C(*coords(0, 0.2539), *coords(-0.4883, 0.2695), *coords(-0.5557, 0.2607))
    path.L(*coords(-0.5645, 0.2257))
    path.Z()

    # Middle architrave
    group.append(path := draw.Path())
    path.M(*coords(-0.5508, 0.3301))
    path.C(*coords(-0.3906, 0.334), *coords(-0.0195, 0.3164), *coords(0.1328, 0.2988))
    path.V(coord(0.3535))
    path.C(*coords(-0.0195, 0.3594), *coords(-0.3906, 0.3789), *coords(-0.5508, 0.377))
    path.Z()

    # Middle logo
    group.append(path := draw.Path())
    path.M(*coords(-0.2891, 0.2441))
    path.L(*coords(-0.2695, 0.3379))
    path.L(*coords(-0.1914, 0.3359))
    path.L(*coords(-0.1699, 0.2402))
    path.Z()

    # Left pillar
    group.append(path := draw.Path())
    path.M(*coords(-0.4336, 0.2539))
    path.V(coord(0.2832))
    path.H(coord(-0.4238))
    path.L(*coords(-0.455, 0.7598))
    path.H(coord(-0.3906))
    path.L(*coords(-0.3809, 0.2832))
    path.H(coord(-0.3711))
    path.V(coord(0.2539))
    path.Z()

    # Left pillar - horizontal axis - top
    group.append(path := draw.Path())
    path.M(*coords(-0.5738, 0.5605))
    path.V(coord(0.5264))
    path.L(*coords(-0.2715, 0.54))
    path.V(coord(0.5732))
    path.Z()

    # Left pillar - horizontal axis - bottom
    group.append(path := draw.Path())
    path.M(*coords(-0.5664, 0.6973))
    path.L(*coords(-0.2734, 0.6953))
    path.V(coord(0.7266))
    path.L(*coords(-0.5078, 0.7335))
    path.Z()

    # Left pillar - left leg
    group.append(path := draw.Path())
    path.M(*coords(-0.5601, 0.6836))
    path.L(*coords(-0.5542, 0.4824))
    arrow(path, -0.5542, 0.4824)
    path.L(*coords(-0.5191, 0.7131))
    path.Z()

    # Left pillar - right leg
    group.append(path := draw.Path())
    path.M(*coords(-0.3301, 0.7617))
    path.L(*coords(-0.3262, 0.5))
    arrow(path, -0.3262, 0.5)
    path.L(*coords(-0.2832, 0.791))
    path.Z()

    # Right pillar
    group.append(path := draw.Path())
    path.M(*coords(-0.0762, 0.2344))
    path.V(coord(0.2656))
    path.H(coord(-0.0664))
    path.L(*coords(-0.0723, 0.8047))
    path.A(*coords(0.0391, 0.006), 0, 0, 0, *coords(0.0059, 0.8047))
    path.L(*coords(-0.0195, 0.2656))
    path.H(coord(-0.0098))
    path.V(coord(0.2344))
    path.Z()

    # Right pillar - horizontal axis - top
    group.append(path := draw.Path())
    path.M(*coords(-0.1914, 0.5664))
    path.V(coord(0.5234))
    path.L(*coords(0.1133, 0.543))
    path.V(coord(0.5801))
    path.Z()

    # Right pillar - horizontal axis - bottom
    group.append(path := draw.Path())
    path.M(*coords(-0.1934, 0.75))
    path.V(coord(0.709))
    path.L(*coords(0.1152, 0.7051))
    path.V(coord(0.7422))
    path.Z()

    # Right pillar - left leg
    group.append(path := draw.Path())
    path.M(*coords(-0.173, 0.4766))
    arrow(path, -0.173, 0.4766)
    path.L(*coords(-0.127, 0.8105))
    path.A(*coords(0.0273, 0.004), 0, 0, 1, *coords(-0.1816, 0.8105))
    path.Z()

    # Right pillar - right leg
    group.append(path := draw.Path())
    path.M(*coords(0.0625, 0.4941))
    arrow(path, 0.0625, 0.4941)
    path.L(*coords(0.1055, 0.7949))
    path.A(*coords(0.02345, 0.004), 0, 0, 1, *coords(0.0586, 0.7949))
    path.Z()

    return group
