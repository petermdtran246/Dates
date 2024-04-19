from datetime import date, timedelta

# 1 Complete read_date()
def read_date():
    """Read a string representing a date in the format 2121-04-12, create a
    date object from the input string, and return the date object
    """
    date_string = input()
    # Split the input string into year, month, and day
    year, month, day = date_string.split("-")
    # Convert string to integer
    year = int(year)
    month = int(month)
    day = int(day)
    # Create a date object from the input string
    date_object = date(year, month, day)
    return date_object


# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list
date_list = []
for i in range(4):
    date_list.append(read_date())

# 3. Use sorted() to sort the dates, earliest first
sorted_dates = sorted(date_list)

# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yy
for date in sorted_dates:
    print(date.strftime("%m/%d/%Y"))

# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number
last_two_dates = sorted_dates[-2:]
days_between = (last_two_dates[1] - last_two_dates[0]).days
print(f"{days_between}")

# 6. Output the date that is 3 weeks from the most recent date in the list
most_recent_date = sorted_dates[-1]
three_weeks_from_recent = most_recent_date + timedelta(weeks=3)
print(f"{three_weeks_from_recent.strftime('%B %d, %Y')}")

# 7. Output the full name of the day of the week of the earliest day
earliest_day = sorted_dates[0]
print(f"{earliest_day.strftime('%A')}")