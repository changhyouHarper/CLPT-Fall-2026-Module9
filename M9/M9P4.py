# Module 9, Problem 4

# Define function to determine pay rate 
def compute_pay_rate(job_code):

	# Declare variable to store pay rate 
	pay_rate = 0

	# Determine pay rate based on job_code value 
	if (job_code == "L"):
		pay_rate = 25
	elif (job_code == "A"):
		pay_rate = 30
	elif (job_code == "J"):
		pay_rate = 50

	# Return pay rate back to caller 
	return pay_rate

# Define main() function 
def main(): 

	# Declare variable to store gross pay 
	gross_pay = 0 

	# Prompt the user to enter loop check value 
	answer = input("Would you like to enter employee information? (Yes/No): ")
	
	# Create a while loop 
	while (answer == "Yes"):

		# Prompt user to enter employee last name 
		last_name = input("\nEnter employee last name: ")

		# Prompt user to enter job code 
		job_code = input("Enter job code: ")

		# Prompt user to enter number of hours worked:
		num_hours = int(input("Enter number of hours worked: "))

		# Declare variable to store pay rate value 
		pay_rate = compute_pay_rate(job_code)

		# Declare variable to store individual user's total pay
		total = 0

		# Consider overtime considerations 
		if (num_hours > 40):
			# Calculate how many additional hours past 40 user worked 
			overtime_hours = num_hours - 40

			# Calculate regular pay 
			regular_pay = 40 * pay_rate

			# Calculate over time pay 
			overtime_pay = overtime_hours * (pay_rate * 1.5)

			# Calculate total overtime pay  
			total = regular_pay + overtime_pay
		else:
			# Otherwise, user gets their regular amount 
			total = num_hours * pay_rate

		# Display last name, total pay back to user 
		print("\nLast Name: " + last_name)
		print(f"Total Pay: ${total:.2f}")

		# Accumulate gross pay 
		gross_pay += total

		# Prompt the user to enter loop check value 
		answer = input("\nWould you like to enter another employee? (Yes/No):  ")

	# Display gross pay 
	print(f"\nGross Pay: ${gross_pay:.2f}")

# Call main() function 
if __name__ == "__main__":
    main()


