"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730391204"


# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...
rand_number: int = randint(1,4)
print("Your fortune cookie says...")
if(rand_number <= 1):
    print("An A+ is right around the corner!")
elif(rand_number <= 2):
    print("You're style is coming into fashion")
elif(rand_number <= 3):
    print("Soon, you'll be greeted with unlimited coding potential")
elif(rand_number <= 4):
    print("Wow, I'm seeing a fantastic Olive Garden dinner in your future")

print("Now, go spread positive vibes!")