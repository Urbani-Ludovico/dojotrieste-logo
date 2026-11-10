import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description = "Dojo Trieste logo creator."
    )

    parser.add_argument(
        "--size",
        type = positive_int,
        help = "Size of the svg logo",
        default = 1024
    )

    parser.add_argument(
        "--style",
        choices = ["default", "light"],
        default = "default",
        help = "Style of the logo",
    )

    parser.add_argument(
        "--background",
        action = "store_true",
        help = "Add background to the logo",
    )

    parser.add_argument(
        "--background-color",
        help = "Color of the background",
    )

    parser.add_argument(
        "--output",
        type = str,
        default = "logo.svg",
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