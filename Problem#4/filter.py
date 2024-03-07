def process_and_print(input_string):
     # Split into separate strings
    splitstring = input_string.split()
    # Convert strings to integers and filter out negative values
    filtered = []
    for i in splitstring:
        if int(i) < 0:
            filtered.append(int(i))
    # Sort integers in reverse order
    filtered.sort()
    filtered.reverse()
    # Print sorted integers
    toprint = ""
    for j in filtered:
        toprint += str(j) + " "
    print(toprint,end="")
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
