# Population estimate calculator
# Author: Marcel Willis

# Retreive inputs from the user.
P0 = eval(input("Input your initial population: "))
k  = eval(input("Input the growth/decay rate: "))
t  = eval(input("Input the number of years you wish to estimate: "))

# Estimate the new population
    # Import the math library
import math
    # Use the growth/decay rate equation
P = P0 * math.e**(k * t)
    # Display the result to the user
print(int(P))