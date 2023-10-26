# Function for checking if x is dividable by n
# It has 2 parameters: x and n
# We return True or False based on the remainder of x divided by n is equal to 0
def is_x_dividable_by_n(x, n):
    return x % n == 0


# Function for checking a single number: x
# Returns "Fizz", "Buzz", "FizzBuzz" or just the number
# Since the call to 'is_x_dividable_by_n' returns a boolean (True or False), we can use the call as the 'if' condition
# Note that using the return keyword early ends the function execution early and the rest is ignored in this case.
# We don't actually need the 'elif' bits, these could just be 'if', can you see why?
def get_fizz_buzz(x):
    if is_x_dividable_by_n(x, 3) and is_x_dividable_by_n(x, 5):
        return 'FizzBuzz'
    elif is_x_dividable_by_n(x, 3):
        return 'Fizz'
    elif is_x_dividable_by_n(x, 5):
        return 'Buzz'
    return x


# So far we have only defined functions, actual execution starts here
# Since the call to 'get_fizz_buzz' returns a number or a string, we can use the call directly in the 'print' function
for x in range(1, 101):
    print(get_fizz_buzz(x))
