def process_input(input_string):
      # Split into separate strings
    split = input_string.split()

    # Convert strings to floats
    floats = []
    for i in split:
        floats.append(float(i))

    # Get max and average
    floats.sort()
    max_value = floats[-1]
    total = float(0)
    for i in floats:
        total += i
    average_value = total / len(floats)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
