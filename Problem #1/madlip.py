def food_input():
    user_input = input()
    tokens = user_input.split()
    print(len(tokens))
    #type you while  loop here
    i = 0
    while i < len(tokens):
        if tokens[i] == "quit":
            break
        print("Eating " + str(tokens[i + 1]) + " " + str(tokens[i]) + " a day keeps you happy and healthy.")
        i += 2

if __name__ == "__main__":
    food_input()
