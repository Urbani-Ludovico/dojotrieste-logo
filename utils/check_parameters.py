
def check_parameters(
        size,
        main_color,
        background,
        output
) -> None:
    if not isinstance(size, int):
        raise TypeError(f"Size {size} is not correct integer")
    if size <= 0:
        raise ValueError(f"Size {size} is not positive")

    if main_color not in ["white", "black"]:
        raise ValueError(f"Main color \"{main_color}\" is not valid")

    if background not in ["white"] and background is not None:
        raise ValueError(f"Background color \"{background}\" is not valid")

    if not isinstance(output, str):
        raise TypeError(f"Output path \"{output}\" is not a valid string")