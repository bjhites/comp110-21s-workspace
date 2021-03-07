"""EX03 - avoid_fifth function."""

__author__: str = "YOUR PID HERE"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello thEre"))
    # ex. print(avoid_fifth("hello there"))


def avoid_fifth(string: str) -> str:
    i: int = 0
    new_string: str = ""
    while i < len(string):
        if(string[i] != "e" and string[i] != "E"):
            new_string += string[i]
        i += 1
    return new_string


if __name__ == "__main__":
    main()