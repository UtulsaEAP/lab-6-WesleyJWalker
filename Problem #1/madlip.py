def food_input():
    '''user_input = input()
    tokens = user_input.split()
    #print(len(tokens))
    #type you while  loop here
    for j in range(len(tokens)):
        print(tokens[j])
    i = 0
    while i < len(tokens):
        if tokens[i] == "quit":
            break
        print("Eating " + str(tokens[i + 1]) + " " + str(tokens[i]) + " a day keeps you happy and healthy.")
        i += 2'''
    
    while True:
        user_input = input()
        tokens = user_input.split()
        word = str(tokens[0])
        number = str(tokens[1])
        if word == "quit":
            return
        else:
            print("Eating " + number + " " + word + " a day keeps you happy and healthy.")

if __name__ == "__main__":
    food_input()
