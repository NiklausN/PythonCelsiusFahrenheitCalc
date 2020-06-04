# Prompt the User to Select from a Menu
print("What temperature are you converting to?")
print("+--------------------+")
print("|   1 = To Celsius   |")
print("|   2 = To Fahren.   |")
print("+--------------------+")
uSel = int(input("User: "))

# Retrieve the Temperature from the User
print("What is the temperature that will be converted?")
temp1 = float(input("User: "))

# Execute the Users Selection and Display the Results
if uSel == 1: # To Celsius

    # Convert the Temperature
    temp2 = float((temp1 - 32.00) * (5.00 / 9.00))

    # Display the Results
    print(temp1, "Fahrenheit is equal to", temp2, "Celsius.")

elif uSel == 2: # To Fahrenheit

    # Convert the Temperature
    temp2 = float((temp1 * (5.00 / 9.00)) + 32.00)

    # Display the Results
    print(temp1, "Celsius is equal to", temp2, "Fahrenheit.")

else:

    # Display an Error Message
    print("Error: Please select an option from the provided list! Rerun the program and try again.")
