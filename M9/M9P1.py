# Module 9, Problem 1 

# Define function to compute extended price  
def compute_total(quantity, unit_price):

 	# Declare variable to store / calculate extended price  
 	extended_price = quantity * unit_price 

 	# Determine discount if applicable 
 	if (extended_price > 100000):
 		extended_price = extended_price - (extended_price * .10)

 	# Return extended price back to caller  
 	return extended_price

# Define main() function 
def main(): 

	# Declare variable to store running total of extended price 
	total_extended_price = 0

	# Prompt the user to enter loop check value 
	answer = input("Would you like to enter an item? (Yes/No): ")
	
	# Create a while loop 
	while (answer == "Yes"):

		# Prompt the user to enter quantity 
		quantity = int(input("\nEnter quantity: "))

		# Prompt the user to enter price
		unit_price = float(input("Enter price: $"))

		extended_price = compute_total(quantity, unit_price)

		# Display quantity, price, and total back to user 
		print("\nQuantity: " + str(quantity))
		print(f"Price: ${unit_price:.2f}")
		print(f"Total: ${extended_price:.2f}")

		# Accumulate final_total variable 
		total_extended_price += extended_price

		# Prompt the user to enter loop check value 
		answer = input("\nWould you like to enter another item? (Yes/No):  ")

	# Display final total back to user 
	print(f"\nFinal Total: ${total_extended_price:.2f}")

# Call main() function
if __name__ == "__main__":
    main()

