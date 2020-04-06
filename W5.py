# Python program to Find day of the week for a given date

from datetime import date
import calendar

my_date = date.today()
calendar.day_name[my_date.weekday()]

if my_date.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay! ")