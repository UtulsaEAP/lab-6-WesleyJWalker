def filter_and_print_range(input_list, min_val, max_val):
    toprint = ""
    for i in input_list:
        if int(i) >= int(min_val) and int(i) <= int(max_val):
            toprint = toprint + str(i) + "," 
    print(toprint, end="")

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split()

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    ranges = user_input.split()
    min_val, max_val = ranges[0], ranges[1]

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
   
