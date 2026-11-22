# Module 9, Problem 5 

# Define function to compute tuition owed 
def compute_tuition_owed(credit_hours, district_code):

	# Declare variable to store pre_credit_hour depending on I or O
	tuition_rate = 0

	# Determine tuition rate owed depending on whether they're I or O
	if (district_code == "I"):
		tuition_rate = 250
	elif (district_code == "O"):
		tuition_rate = 550

	# Calculate tuition total 
	tuition = tuition_rate * credit_hours

	# Return total tuition owed back to caller 
	return tuition

# Define main() function 
def main():

	# Declare variable to store total of all tuitions 
	tuition_total = 0

	# Prompt the user to enter loop check value 
	answer = input("Would you like to enter a student? (Yes/No): ")
	
	# Create a while loop 
	while (answer == "Yes"):

		# Prompt user to enter student last name 
		last_name = input("\nEnter last name: ")

		# Prompt number of credit hours 
		credit_hours = int(input("Enter number of credits: "))

		# Prompt user to enter district code
		district_code = input("Enter district code (I/O): ")

		# Declare variable to store total tuition owed
		tuition = compute_tuition_owed(credit_hours, district_code)

		# Display student name, tuition owed 
		print("\nStudent Last Name: " + last_name)
		print(f"Tuition Owed: ${tuition:.2f}")

		# Accumulate tuition_total 
		tuition_total += tuition

		# Prompt the user to enter loop check value 
		answer = input("\nWould you like to enter another student? (Yes/No):  ")

	# Display tuition_total back to user 
	print(f"\nTuition total: ${tuition_total:.2f}")

# Call main() function 
if __name__ == "__main__":
    main()

