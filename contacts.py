# To add:
# ask to confirm duplicate
# format phone number
# save and exit, allow user to view newly added changes prior to saving / exiting


import json
import os

# Defines global variable for our contacts.txt file
contacts_file = 'contacts.txt'



# File is created and initialized if it doesn't already exist
def initialize_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file: # Opens filename in write-mode
            json.dump([], file, indent=4) # File starts with [an empty] JSON structure; indented for readability
            
            

# File is loaded and read if it already exists
def load_contacts_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return [] # Returns an empty array if it doesn't exist
            
            

# Saves any changes to [contacts.txt] file           
def save_contacts_to_file(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4) # Writes to file our [loaded_contacts_from_file] newly fed list, overriding any old content
        
        
        
# Allows user to add a contact with "name, phone & email" parameters
def add_contact(firstName, lastName, phone, email):
    contacts = load_contacts_from_file(contacts_file)
    contacts.append ({ # Appends added contact to our loaded list (in memory) [via "contacts" variable]
        'firstName' : firstName,
        'lastName' : lastName,
        'phone' : phone,
        'email' : email
    })

    save_contacts_to_file(contacts, contacts_file) # Saves added contact [from loaded list in-memory (with newly appended info)] to our contacts.txt file upon completion of function execution
    
    print("\nContact added successfully!\n") # Notifies user upon successful completion of function execution



# Allows user to view contacts
def view_contacts():
    contacts = load_contacts_from_file(contacts_file)
    if not contacts:
        print("No contacts available.") # Prints "No contacts available." if no contacts are stored
        return
    
    # Prints contact details by looping through the contacts list
    for contact in contacts:
        print(f"    Name: {contact['firstName']} {contact['lastName']}")
        print(f"    Phone Number: {contact['phone']}")
        print(f"    Email Address: {contact['email']}")
        print() # Prints a blank line [for spacing between contacts] for readability
        
        

# Allows user to update a contact
def update_contact(name, contacts):
    contacts = load_contacts_from_file(contacts_file)
    
    updated_contact = [] # Array for updated contacts to be stored in
    
    for contact in contacts:
        if name.lower() in contact['firstName'].lower() or name.lower() in contact['lastName'].lower(): # Checks the user's input if ['firstName' or 'lastName'] contains the substring that was provided by the user; and returns True if found
            
            print("\nUpdating:\n") # Prints user's details to be updated upon met condition
            print(f"    Name: {contact['firstName']} {contact['lastName']}")
            print(f"    Phone Number: {contact['phone']}")
            print(f"    Email Address: {contact['email']}")
            print() # Prints a blank line
            
            new_firstName = input(f"Enter new First Name (or leave blank to keep '{contact['firstName']}'): ") # Prompts user for first name
            new_lastName = input(f"Enter new Last Name (or leave blank to keep '{contact['lastName']}'): ") # Prompts user for last name
            new_phone = input(f"Enter new Phone Number (or leave blank to keep '{contact['phone']}'): ") # Prompts user for phone number
            new_email = input(f"Enter new Email Address (or leave blank to keep '{contact['email']}'): ") # Prompts user for email address
            
            
            print("\nContact updated successfully!\n") # Notifies user upon successful completion of function execution
            
            
            if new_firstName: # If returned True
                contact['firstName'] = new_firstName # Contact's 'firstName' gets updated with new_firstName input
            if new_lastName: # If returned True
                contact['lastName'] = new_lastName # Contact's 'lastName' gets updated with new_lastName input      
            if new_phone: # If returned True
                contact['phone'] = new_phone # Contact's 'phone' gets updated with new_phone input
            if new_email: # If returned True
                contact['email'] = new_email # Contact's 'email' gets updated with new_email input
                
                
        else: print("\nError! Contact does not seem to exist.\nReturning you to the main menu...\n")
                
        updated_contact.append(contact) # Places contacts in the updated_contact array; and appends each contact that was updated [retaining the original contacts position]
    
    contacts[:] = updated_contact # Places 'updated_contact' array in place of previous 'contacts' array, replacing all elements with the newly updated ones
    
    save_contacts_to_file(contacts, contacts_file) # Saves it to contacts.txt file
    
    

# Allows user to remove a contact
def remove_contact(name, contacts):
    contacts = load_contacts_from_file(contacts_file)
    
    new_contacts = [] # Array for contacts to be stored in [minus the ones removed]
    contact_found = False # Flag variable for contact found
    
    for contact in contacts:
        if name.lower() in contact['firstName'].lower() or name.lower() in contact['lastName'].lower(): # Matches user's input with data in 'firstName' and 'lastName' element if True
            contact_found = True # Flags as True [for "False" message to not be printed]
            
            print(f"\nAre you sure you want to remove:\n")
            print(f"    Name: {contact['firstName']} {contact['lastName']}")
            print(f"    Phone Number: {contact['phone']}")
            print(f"    Email Address: {contact['email']}")
            print() # Prints a blank line
            
            
            choice = input(f"\nPress 'y' for Yes or 'n' for No: ").strip().lower() # Strips user's input of any leading or trailing whitespaces and sets it to lowercase for flexibility of input
            
            
            if choice in ['yes', 'y']: # If user chooses to continue with removal
                print("\nContact removed successfully!\n")
            
            elif choice in ['no', 'n']: # If user chooses to cancel removal
                print("\nContact removal canceled.\nReturning you to the main menu...\n")
                new_contacts.append(contact) # Adds contact back to new_contacts
           
           
        else:
            new_contacts.append(contact) # Updates the new_contacts list with the ones that weren't removed
        
    if not contact_found: # If user input didn't match criteria
        print("\nNo contact found with that name.\nReturning you to the main menu...\n") # Returns message
            
    contacts[:] = new_contacts # Replaces 'contacts' array with the elements of 'new_contacts'
    
    save_contacts_to_file(contacts, contacts_file) # Saves it to contacts.txt file
            
            
            
# Function to initiate application         
def main():
    initialize_file(contacts_file)
    contacts = load_contacts_from_file(contacts_file)

    # Printing introductory message outside of loop to avoid repetition if user enters anything other than menu options
    print("\nMy Contacts App:")
    print("\nWhat would you like to do today?\n")
        
    while True:
        
        print("1. Add a Contact")
        print("2. View My Contacts")
        print("3. Update a Contact")
        print("4. Remove a Contact")
        print("5. Exit")
        choice = input ("\nEnter your Prompt: ")
        
        
        if choice == '1':
            firstName = input ("\nEnter First Name: ")
            lastName = input ("Enter Last Name: ")
            phone = input ("Enter Phone Number: ")
            email = input ("Enter Email Address: ")
            add_contact(firstName, lastName, phone, email)
            
            
        elif choice == '2':
            print("\nViewing Contacts:\n")
            view_contacts()
            
            
        elif choice == '3':
            print("\nUpdating a Contact:\n")
            name = input("Enter the name or partial name of the contact you'd like to update: ")
            update_contact(name, contacts)
            
            
        elif choice == '4':
            name = input("\nEnter the name or partial name of the contact you'd like to remove: ")
            remove_contact(name, contacts)
            
            
        elif choice == '5':
            print("Exiting the application...")
            break
        
        
        else: print("\nError! Invalid prompt.\nPlease enter a number from the menu: \n")



# Loads application
main()