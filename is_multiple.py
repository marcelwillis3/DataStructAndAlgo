# Multiple checker
# Author: Marcel Willis

# Create a function called is_multiple. Takes two inputs, n and m
def is_multiple(n,m):
    # Convert inputs n and m to integers, compute m modulo n, and compare result to zero.
    if int(m) % int(n) == 0:
        # Print to the user that n is a multiple of m
        print(n,"is a multiple of",m)
    # Determine that n is not a multiple of m based on the above if statement.
    else:
        # Print to the user that n is not a multiple of m
        print(n,"is not a multiple of",m)