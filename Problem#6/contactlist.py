def process_user_contacts(user_input):
    user_contacts = user_input.split()
    contactsList = {}
    # Put word pairs into a dictionary
    for i in range(len(user_contacts)):
        contact = user_contacts[i].split(",")
        contactsList.update({contact[0]:contact[1]})
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    print(contactsList.pop(contact_name))
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
