# Nick Soter
# This is a planner to calculate the cost of a trip to a destination specified by the user.
intro_statement = "---------trip planner---------"
print(intro_statement.upper())
print("Hello! Welcome to trip planner. \n")

#user input
name = input("Enter your name: ")
destination = input("Enter your destination: ")
trip_distance_one_way = int(input("Enter the distance to your destination in miles: "))
vehicle_mpg = int(input("Enter your vehicle's miles per gallon (MPG): "))
gas_price_per_gallon = float(input("Enter the estimated price of gas per gallon: "))
num_travelers = float(input("Enter the number of travelers: "))

#calculations for trip cost
trip_distance_total = trip_distance_one_way * 2
total_gallons_needed = trip_distance_total / vehicle_mpg
total_gas_cost = total_gallons_needed * gas_price_per_gallon
cost_per_person = total_gas_cost / num_travelers

#printed summary
print("\n")
exit_statement = "---------trip summary---------"
print(exit_statement.upper())
print(f"Thank you {name} for your input!\nHere is your trip Summary:")
print(f"Destination: {destination}")
print(f"Total cost: ${round(total_gas_cost, 2)}")
print(f"Cost per person: ${round(cost_per_person, 2)}")

#Thank you