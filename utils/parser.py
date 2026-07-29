import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description = "Dojo Trieste logo creator."
    )

    parser.add_argument(
        "--size", "-s",
        type = positive_int,
        help = "Size of the svg logo",
        default = 1024
    )

    parser.add_argument(
        "--main-color", "-c",
        choices = ["white", "black"],
        help = "Main color",
        default = "black"
    )

    parser.add_argument(
        "--background", "-b",
        type = background,
        choices = ["white", "black", "none", "transparent"],
        default = None,
        help = "Background color",
    )

    parser.add_argument(
        "--output", "-o",
        type = str,
        required = True,
        help = "Output filename",
    )

    return parser.parse_args()


def positive_int(value: str) -> int:
    """
    Type validator to enforce positive integers.
    """

    try:
        ivalue = int(value)
    except ValueError:
        ivalue = 0

    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a valid positive integer")
    
    return ivalue

def background(value: str) -> str | None:
    """
    Type validator for background.
    """

    if value in ["white", "black"]:
        return value
    return None