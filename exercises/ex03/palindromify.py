"""EX03 - palindromify function."""

__author__: str = "730391204"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("race", False))
    print(palindromify("live on time ", False))
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))


def palindromify(string: str, even: bool) -> str:
    palindrome: str = string
    i : int = 0
    if even:
        while i < len(string):
            palindrome += string[len(string) - (1 + i)]
            i += 1
    elif not even:
        while i < (len(string) - 1):
            palindrome += string[len(string) - (2 + i)]
            i += 1
    return palindrome



if __name__ == "__main__":
    main()