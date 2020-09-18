# Temperature Converter from Fahrenheit to Celsius
# Author: Marcel Willis

# Allow user to convert up to 3 different temperatures
for temp_Conversions in range(3):
    
    # Receive user input for temp in Fahrenheit and convert from string to float
    fahrenheit = float(input("Enter your temperature in Fahrenheit: "))
    
    # Calculate temp in Celsius and round to 2 decimal places, using the fahrenheit variable from the user
    celsius = round((fahrenheit - 32)/1.8,2)
    
    # Return temp in Celsius to the user for review
    print("Your temperature in Celsius is:", str(celsius), "deg C")