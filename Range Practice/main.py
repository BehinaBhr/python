def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2):  # Make the loop run twice (two rows)
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low"
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low - 1, -1):
            if y == low:
                # Don’t print a comma after the last item
                print(str(y))
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ")

sequence(1, 3)





for outer_Loop in range(2, 6+1):
   for inner_loop in range(outer_Loop):
           if inner_loop % 2 == 0:
                   print(inner_loop)



def odd_numbers(maximum):
    return_string = ''  # Initializes variable as an empty string

    # Complete the for loop with a range that includes all
    # odd numbers up to and including the "maximum" value.
    for num in range(1, maximum + 1, 2):
        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        return_string += str(num) + ' '

    # This strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()

print(odd_numbers(6))  # Should be "1 3 5"
print(odd_numbers(10))  # Should be "1 3 5 7 9"
print(odd_numbers(1))  # Should be "1"
print(odd_numbers(3))  # Should be "1 3"
print(odd_numbers(0))  # Should be an empty string (no numbers displayed)







def divisible(maximum, divisor):
    count = 0  # Initialize an incremental variable

    # Complete the for loop
    for x in range(maximum + 1):
        # Check if x is evenly divisible by the divisor
        if x % divisor == 0:
            # Increment the count variable
            count += 1

    return count

print(divisible(100, 10))  # Should be 10
print(divisible(10, 3))    # Should be 4
print(divisible(144, 17))  # Should be 9



