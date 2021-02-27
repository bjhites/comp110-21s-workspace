"""Chose your own adventure into the woods!"""

__author__ = "730391204"

points: int = 10
char_class: str = ""
player: str = ""


def main() -> None:
    """Entrypoint to program."""
    global points
    points += 10
    greet()


def greet() -> None:
    """Entrypoint to adventure."""
    global points
    global player
    print("Welcome to the forest!")
    player += input("What's your name traveler?")
    adventure_start: str = input("You stumble upon a fork in the trail, go left, right, or turn back (L/R/TB): ")
    if(adventure_start == "L"):
        points += 20
        turn_left()
    elif(adventure_start == "R"):
        points += 20
        turn_right()
    else:
        print(f"you turned around, lame. ADVENTURE POINTS: {points}")


def turn_left() -> None:
    """turns deeper into forest, leads character towards being a bear."""
    global points
    global char_class
    points += 5
    cave_nap: str = input("\n The pine tree canopy shields the quiet forest floor from the amber sunset, you find a hillside with a small overhang. Spend the night or continue on deeper into the forest? (S/C) ")
    if(cave_nap == "S"):
        char_class += "bear"
        points = class_points(points, char_class)
        

def turn_right() -> None:
    """turns player right, deeper into the woods towards witch hut."""
    global points
    global char_class
    points += 10
    cabin: str = input("\n Your legs begin to ache as you crest a hill and find an old mill house beside a loud stream. Enter the cabin or contiune on? (E/C) ")
    if(cabin == "E"):
        char_class += "sorcerer"
        points = class_points(points, char_class)


def check_adventure_points() -> bool:
    """if character's points hit zero, end game."""
    global points
    if(points <= 0):
        print("you lost")
        return False
    else:
        return True


def class_points(points: int, char_class: str) -> int:
    """increases points dramatically based on class."""
    if(char_class == "bear"):
        points += 500
    else:
        points += 800
    return points


if __name__ == "__main__":
    main()