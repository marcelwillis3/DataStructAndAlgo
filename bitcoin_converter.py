# Bitcoin Converter
# Author: Marcel Willis

# Notify the user of the current bitcoin rate (source: Coinbase.com)
print("As of 8/28/2019 at 8:43pm, bitcoin is currently trading at $9720.67 per bitcoin")

# Allow user to input their number of bitcoins and convert to float
bitcoin = float(input("Enter your bitcoin amount: "))

# Convert bitcoin to US Dollars
bitcoin2USD = round(9720.67*bitcoin,2)

# Return to the user what their bitcoin amounts to in US Dollars
print("That is worth","$",str(bitcoin2USD))