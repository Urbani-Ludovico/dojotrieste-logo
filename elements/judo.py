import drawsvg as draw


def judo(
        radius: int
) -> draw.Group:
    coord = lambda x: x * radius
    coords = lambda x, y: (x * radius, y * radius)

    group = draw.Group(
        fill_rule = "evenodd"
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

    # First kanji - bottom part
    group.append(path := draw.Path())
    path.M(*coords(0.5283, -0.2383))
    path.C(*coords(0.625, -0.2539), *coords(0.6367, -0.2617), *coords(0.6729, -0.2363))
    path.S(*coords(0.668, -0.1934), *coords(0.6504, -0.2002))
    path.S(*coords(0.5859, -0.2051), *coords(0.5264, -0.2012))
    path.C(*coords(0.6641, -0.1016), *coords(0.6934, -0.1348), *coords(0.7051, -0.1074))
    path.C(*coords(0.5762, -0.0781), *coords(0.5977, -0.0781), *coords(0.5205, -0.1699))
    path.C(*coords(0.5215, -0.1172), *coords(0.5273, -0.0938), *coords(0.5117, -0.0762))
    path.S(*coords(0.4863, -0.0566), *coords(0.4707, -0.0947))
    path.S(*coords(0.4766, -0.1172), *coords(0.4756, -0.1553))
    path.C(*coords(0.4297, -0.1211), *coords(0.3711, -0.0957), *coords(0.3086, -0.0869))
    path.C(*coords(0.3711, -0.123), *coords(0.4102, -0.1426), *coords(0.4639, -0.1963))
    path.C(*coords(0.4297, -0.1934), *coords(0.3906, -0.1836), *coords(0.3711, -0.1777))
    path.S(*coords(0.3477, -0.1602), *coords(0.3252, -0.1914))
    path.S(*coords(0.3027, -0.209), *coords(0.3672, -0.2178))
    path.S(*coords(0.4492, -0.2266), *coords(0.4727, -0.2314))
    path.C(*coords(0.4395, -0.2891), *coords(0.5176, -0.248), *coords(0.5283, -0.2383))
    path.Z()

    # Second kanji - first apostrophe
    group.append(path := draw.Path())
    path.M(*coords(0.3896, 0.0718))
    path.C(*coords(0.3644, 0.0907), *coords(0.3499, 0.0631), *coords(0.3392, 0.0472))
    path.C(*coords(0.3152, 0.0118), *coords(0.3004, -0.0002), *coords(0.3641, 0.0151))
    path.C(*coords(0.4227, 0.0292), *coords(0.4072, 0.0586), *coords(0.3896, 0.0718))
    path.Z()

    # Second kanji - second apostrophe
    group.append(path := draw.Path())
    path.M(*coords(0.5093, 0.0443))
    path.C(*coords(0.4835, 0.0616), *coords(0.4789, 0.0387), *coords(0.4688, 0.0209))
    path.C(*coords(0.4466, -0.0183), *coords(0.4524, -0.0147), *coords(0.4942, -0.0036))
    path.C(*coords(0.5253, 0.0047), *coords(0.5275, 0.032), *coords(0.5093, 0.0442))
    path.Z()

    # Second kanji - third apostrophe
    group.append(path := draw.Path())
    path.M(*coords(0.5391, 0.0498))
    path.S(*coords(0.5469, 0.0488), *coords(0.5635, -0.002))
    path.C(*coords(0.5664, -0.0078), *coords(0.5391, -0.0449), *coords(0.6055, -0.0205))
    path.C(*coords(0.6543, 0.0039), *coords(0.625, 0.0059), *coords(0.6133, 0.0127))
    path.S(*coords(0.5664, 0.0449), *coords(0.5391, 0.0498))

    # Second kanji - first block
    group.append(path := draw.Path())
    path.M(*coords(0.4941, 0.1299))
    path.C(*coords(0.4961, 0.125), *coords(0.5, 0.1074), *coords(0.4971, 0.0977))
    path.C(*coords(0.4531, 0.1055), *coords(0.4453, 0.1172), *coords(0.4287, 0.0928))
    path.S(*coords(0.4102, 0.0742), *coords(0.4492, 0.0684))
    path.C(*coords(0.5957, 0.0527), *coords(0.6055, 0.0215), *coords(0.6465, 0.0508))
    path.S(*coords(0.6445, 0.0918), *coords(0.6348, 0.0898))
    path.S(*coords(0.5859, 0.0908), *coords(0.5469, 0.0918))
    path.C(*coords(0.5664, 0.1055), *coords(0.5469, 0.1094), *coords(0.5352, 0.1211))
    path.C(*coords(0.5781, 0.1113), *coords(0.5781, 0.1113), *coords(0.6172, 0.125))
    path.S(*coords(0.6289, 0.1602), *coords(0.6328, 0.2051))
    path.S(*coords(0.6348, 0.2734), *coords(0.6211, 0.2891))
    path.S(*coords(0.5957, 0.3027), *coords(0.582, 0.2822))
    path.L(*coords(0.4902, 0.2881))
    path.C(*coords(0.4844, 0.2949), *coords(0.4688, 0.3145), *coords(0.4512, 0.2773))
    path.S(*coords(0.4531, 0.2734), *coords(0.4521, 0.2051))
    path.S(*coords(0.4141, 0.1074), *coords(0.4805, 0.1318))
    path.Z()
    path.M(*coords(0.4922, 0.1562))
    path.C(*coords(0.5859, 0.1367), *coords(0.5742, 0.1367), *coords(0.5752, 0.252))
    path.L(*coords(0.4922, 0.2627))
    path.V(coord(0.2432))
    path.C(*coords(0.5078, 0.2441), *coords(0.5469, 0.2402), *coords(0.5645, 0.2363))
    path.C(*coords(0.5625, 0.2109), *coords(0.543, 0.2031), *coords(0.4922, 0.2168))
    path.V(coord(0.1982))
    path.C(*coords(0.5078, 0.1992), *coords(0.5469, 0.1953), *coords(0.5645, 0.1914))
    path.C(*coords(0.5625, 0.166), *coords(0.543, 0.1582), *coords(0.4922, 0.1719))
    path.Z()

    # Second kanji - second block
    group.append(path := draw.Path())
    path.M(*coords(0.3594, 0.291))
    path.C(*coords(0.3555, 0.2246), *coords(0.3164, 0.2383), *coords(0.3477, 0.1641))
    path.C(*coords(0.332, 0.1797), *coords(0.3027, 0.1816), *coords(0.2949, 0.1514))
    path.C(*coords(0.3223, 0.1504), *coords(0.3398, 0.1387), *coords(0.3477, 0.127))
    path.S(*coords(0.3516, 0.1113), *coords(0.3906, 0.125))
    path.S(*coords(0.4141, 0.1602), *coords(0.3984, 0.166))
    path.S(*coords(0.3809, 0.1855), *coords(0.375, 0.1992))
    path.S(*coords(0.3672, 0.2148), *coords(0.3867, 0.2314))
    path.S(*coords(0.4141, 0.2637), *coords(0.3965, 0.292))
    path.C(*coords(0.4688, 0.3027), *coords(0.5078, 0.3291), *coords(0.7188, 0.3262))
    path.C(*coords(0.6738, 0.3613), *coords(0.5957, 0.3984), *coords(0.5664, 0.3857))
    path.S(*coords(0.4004, 0.3252), *coords(0.375, 0.3252))
    path.S(*coords(0.3223, 0.3516), *coords(0.3008, 0.3242))
    path.S(*coords(0.2734, 0.2891), *coords(0.3594, 0.291))
    path.Z()

    return group