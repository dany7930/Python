largest = None
smallest = None

while True:
    sval = input("Enter a number: ")
    if sval == 'done':  # Exit the loop
        break
    try:
        num = int(sval)  # Convert input to an integer
    except ValueError:
        print("Invalid input")  # Handle non-numeric input
        continue

    # Update largest and smallest numbers
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

# Output the results
print("Maximum is", largest)
print("Minimum is", smallest)
