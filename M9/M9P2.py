# Module 9, Problem 2 

# Define function to compute batting average 
def compute_batting_avg(hits, at_bats): 

	# Define variable to store / compute batting avg 
	batting_avg = hits / at_bats

	# Return batting average back to caller
	return batting_avg

# Define main() function 
def main():

	# Define variable to store number of players entered
	player_count = 0

	# Prompt the user to enter loop check value 
	answer = input("Would you like to enter a player? (Yes/No): ")
	
	# Create a while loop 
	while (answer == "Yes"):

		# Prompt user to enter last name
		last_name = input("\nEnter last name: ")

		# Prompt number of hits for player 
		num_hits = int(input("Enter number of hits: "))

		# Prompt user to enter number of at bats 
		at_bats = int(input("Enter number of at bats: "))

		# Declare variable to store / calculate batting average 
		batting_avg = compute_batting_avg(num_hits, at_bats)

		# Display last name, batting average back to user 
		print("\nLast Name: " + last_name)
		print(f"Batting Average: {batting_avg:.3f}")

		player_count += 1 

		# Prompt the user to enter loop check value 
		answer = input("\nWould you like to enter another player? (Yes/No):  ")

	# Display count of number of players entered back to user 
	print("\nCount: " + str(player_count))

# Call main() function 
if __name__ == "__main__":
    main()

