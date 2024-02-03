# Date and Time Guide

# 1. Importing the datetime module
from datetime import datetime, date, time, timedelta

# 2. Getting the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# 3. Extracting components from a datetime object
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)

# 4. Creating a datetime object
custom_datetime = datetime(2023, 1, 15, 12, 30, 45)
print("Custom Date and Time:", custom_datetime)

# 5. Formatting a datetime object as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# 6. Parsing a string to create a datetime object
date_string = "2023-01-20 18:45:30"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime:", parsed_datetime)

# 7. Date and Time arithmetic
one_day = timedelta(days=1)
one_hour = timedelta(hours=1)

tomorrow = current_datetime + one_day
one_hour_later = current_datetime + one_hour

print("Tomorrow:", tomorrow)
print("One Hour Later:", one_hour_later)

# 8. Date-only and Time-only objects
current_date = date.today()
current_time = datetime.now().time()

print("Current Date:", current_date)
print("Current Time:", current_time)

# 9. Working with time deltas
time_difference = custom_datetime - current_datetime
print("Time Difference:", time_difference)

# 10. Day of the week and other properties
day_of_week = current_date.weekday()  # Monday is 0 and Sunday is 6
is_leap_year = current_date.year % 4 == 0 and (current_date.year % 100 != 0 or current_date.year % 400 == 0)

print("Day of the Week:", day_of_week)
print("Is Leap Year?", is_leap_year)

# 11. Working with the time module
# Example: Measure the execution time of a specific operation

# Importing the time module
import time

# Record the start time
start_time = time.time()

# Simulate a time-consuming operation (e.g., a loop)
for _ in range(1000000):
    pass

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Elapsed Time for the Operation: {elapsed_time:.6f} seconds")
