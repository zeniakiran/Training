print("====================================")
print("      Welcome to Ride Selector!     ")
print("====================================")
print()

print("Step 1: Choose your vehicle")
print("  1 - Bike")
print("  2 - Car")
print()

vehicle_choice = int(input("Enter your choice (1 or 2): "))
print()

if vehicle_choice == 1:
    # This block runs only if the user selects Bike
    print("Step 2: Choose your bike")
    print("  1 - Scooty")
    print("  2 - Mountain Bike")
    print()

    bike_choice = int(input("Enter 1 or 2: "))
    print()

    if bike_choice == 1:
        print("Your ride   : Scooty")
        print("Max speed   : 80 km/h")
        print("Perfect for : Daily city travel")
    else:
        print("Your ride   : Mountain Bike")
        print("Max speed   : 40 km/h")
        print("Perfect for : Rocky trails")

elif vehicle_choice == 2:
    # This block runs only if the user selects Car
    print("Step 2: Choose your car")
    print("  1 - Sedan")
    print("  2 - SUV")
    print()

    car_choice = int(input("Enter 1 or 2: "))
    print()

    if car_choice == 1:
        print("Your ride   : Sedan")
        print("Capacity    : 5 people")
        print("Perfect for : Comfortable family travel")
    else:
        print("Your ride   : SUV")
        print("Capacity    : 7 people")
        print("Perfect for : Long road trips")

else:
    print("Invalid selection!")
    print("Please choose 1 for Bike or 2 for Car.")

print()
print("====================================")
print("     Your ride has been selected!   ")
print("      Have a safe journey! 🚗🏍️      ")
print("====================================")