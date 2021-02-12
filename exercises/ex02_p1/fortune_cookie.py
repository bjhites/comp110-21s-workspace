"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730391204"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    rand_number: int = randint(1,4)
    if(rand_number <= 1):
        return "An A+ is right around the corner!"
    elif(rand_number <= 2):
        return "You're style is coming into fashion"
    elif(rand_number <= 3):
        return "Soon, you'll be greeted with unlimited coding potential"
    elif(rand_number <= 4):
        return "Wow, I'm seeing a fantastic Olive Garden dinner in your future"
    else:
        return "broke"


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
