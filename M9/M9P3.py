# Module 9, Problem 3 

# Define function to compute miles per gallon 
def compute_mpg(miles_travelled, gallons_used):

	# Define variable to store / calculate mpg
	mpg = miles_travelled / gallons_used

	# Return value back to user 
	return mpg

# Define main() function 
def main(): 

	# Declare variabl to store number of entries made
	trip_count = 0

	# Prompt the user to enter loop check value 
	answer = input("Would you like to enter a trip? (Yes/No): ")
	
	# Create a while loop 
	while (answer == "Yes"):

		# Prompt user to enter destination city 
		destination_city = input("\nEnter destination city: ")

		# Prompt user to enter miles travelled 
		miles_travelled = float(input("Enter miles travelled: "))

		# Prompt user to enter gallons of gas used for trip 
		gallons_used = float(input("Enter gallons of gas used: "))

		# Declare variable to store miles per gallon calculated 
		mpg = compute_mpg(miles_travelled, gallons_used)

		# Display city, miles, and mpg
		print("\nCity: " + destination_city)
		print(f"Miles Travelled: {miles_travelled:.2f}")
		print(f"Miles Per Gallon: {mpg:.2f}")

		trip_count += 1 

		# Prompt the user to enter loop check value 
		answer = input("\nWould you like to enter another trip? (Yes/No):  ")

	# Display number of entries made 
	print("\nTotal Trips Made: " + str(trip_count))

# Call main() function 
if __name__ == "__main__":
    main()


