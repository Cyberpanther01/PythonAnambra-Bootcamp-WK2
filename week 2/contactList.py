contact_list = [
    {"name": "Micheal Griffin ", "phone": "432-083-8753 ", "email": "griffinmicheal@example.com"},
    {"name": "Chinaza Benjamin ", "phone": "908-347-9384", "email": "chi@example.com "},
    {"name": "Tafawa Balewa ", "phone": "093-424-2434 ", "email": "tafawa@example.com"},
    {"name": "James Bond", "phone": "344-233-3443", "email": "bond@example.com"}
]

#function to access and print their details

def print_details():
    print('Contact list:')
    
    for contact in contact_list:
        print(f"Name: {contact_list['name']}, Phone: {contact_list['phone']}, Email{contact_list['email']}")

# function to modify data

def modify(name, phone, email):
    for contact in contact_list:
        if contact['name'] == name:
            if phone:
                contact['phone'] == phone
            if email:
                contact['email'] == email
            print(f'New contact: {contact}')
    else:
        print('Contact not found.')        

# function to add a new contact
def add_contact(name, phone, email):
    new_contact = {'name': name, 'phone': phone, 'email': 'email'}
    contact_list.append(new_contact)
    print(f'Added new contact: {new_contact}')

#function to remove a contact
def del_contact(name, phone, email):
    delete = {'name': name, 'phone':phone, 'email':email}
    contact_list.remove(delete)
    return f'Successfully deleted.'