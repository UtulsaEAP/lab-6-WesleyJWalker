def process_user_contacts(user_input):
    user_contacts = user_input.split()
    '''names = []
    numbers = []
    for i in range(len(user_contacts)):
        if i % 2 == 0:
            numbers.append(user_contacts[i])
        else:
            names.append(user_contacts[i])

    # Put word pairs into a dictionary
    
    # Get contact name from input, output contact's phone number'''
    contact_name = input("Enter the contact name: ")
    print(user_contacts[user_contacts.index(contact_name) + 1])
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
