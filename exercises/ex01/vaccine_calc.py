"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_ad: int = int(input("Doses administered: "))
daily_doses: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))

# Equation for calculation how many days to vaccinate
target_population: float = population * (target / 100)
target_remaining: float = target_population - (doses_ad / 2)
days_needed: int = round(target_remaining / (daily_doses / 2))

#Timedelta variables
today: datetime = datetime.today()
days_vaccinating: timedelta = timedelta(days_needed)
finish_date: datetime = today + days_vaccinating
print("We will reach " + str(target) + "vaccination in " + str(days_needed) + " days, which falls on " + finish_date.strftime("%B %d, %Y"))