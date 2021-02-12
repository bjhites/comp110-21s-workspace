"""Tar Heels exercise redux as a structured program."""

__author__ = "730391204"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(x: int) -> str:
    if(((x % 2) == 0) and ((x % 7) == 0)):
        return ("TAR HEELS")
    elif((x % 2) == 0):
        return ("TAR")
    elif((x % 7) == 0):
        return ("HEELS")
    else:
        return ("CAROLINA")


if __name__ == "__main__":
    main()
