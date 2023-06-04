from datetime import date
from math import floor

# take date from user
date_from_user = input("Please enter a date (in DD/MM/YYYY): ")
date_split = date_from_user.split('/')
day = int(date_split[0])
month = int(date_split[1])
year = int(date_split[2])

# convert user input into date format
user_date = date(year, month, day)

#retrieve current date from datetime
today = date.today()

# calculate age between current date and given date
age = today - user_date

# convert days into years and round down to give age.
print(floor(age.days/365))