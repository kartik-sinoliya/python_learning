# Writing variable names to calculate cars_not_driven, cars_driven, carpool_capacity and avg_passenger_per_car.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

# Print there are 100 cars available.
print("There are", cars, "cars available.")

# Print there are only 30 drivers available.
print("There are only", drivers, "drivers available.")

# Print how many empty cars available today.
print("There will be", cars_not_driven, "empty cars available.")

# Print how many carpool capacity available.
print("We can transport", carpool_capacity, "people today.")

# Print how many passengers we have to carpool today.
print("We have", passengers, "passengers to carpool today.")

# Print average passenger per car available.
print("We need to put about", average_passenger_per_car, "passengers in each car.")
