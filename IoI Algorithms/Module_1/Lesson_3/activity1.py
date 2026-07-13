# ================================
#  CITY WEATHER CHECKER
#  File: city-weather-checker.py
# ================================


# PART 1 - GET USER INPUT
location = input("Please enter your city: ")
temperature = float(input("Enter the current temperature (°C): "))


# PART 2 - SIMPLE if STATEMENT
if temperature > 35:
    print("Heat Alert: The temperature is extremely high today!")


# PART 3 - if-else STATEMENT
if temperature > 25:
    print("The weather looks pleasant for outdoor activities.")
else:
    print("The weather is a bit chilly. Consider wearing warm clothes.")


# PART 4 - if-elif-else STATEMENT
if temperature > 35:
    print("Today's Weather: Extremely Hot")
elif temperature > 25:
    print("Today's Weather: Warm")
elif temperature > 15:
    print("Today's Weather: Mild")
else:
    print("Today's Weather: Cold")


# PART 5 - USING datetime MODULE
import datetime
import calendar

current_datetime = datetime.datetime.now()

print("Selected City:", location)
print("Current Date & Time:", current_datetime)

print(calendar.calendar(current_datetime.year))