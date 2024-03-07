def check_palindrome(user_input):
 #type your code here
    input = user_input
    split = input.split()
    word = ""
    for i in split:
        if i != " ":
            word += i
    reversed = ""
    for i in word:
        reversed = i + reversed
    if word == reversed:
        print("palindrome: " + input)
    else:
        print("not a palindrome: " + input)
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
