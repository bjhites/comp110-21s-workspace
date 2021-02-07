"""An exercise in remainders and boolean logic."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
user_number: int = int(input("Enter an int: "))
if(((user_number % 2) == 0) and ((user_number % 7) == 0)):
    print("TAR HEELS")
elif((user_number % 2) == 0):
    print("TAR")
elif((user_number % 7) == 0):
    print("HEELS")
else:
    print("CAROLINA")

