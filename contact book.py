import tkinter as tk
from tkinter import messagebox

# Initialize the contact list
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        contacts.append(contact)
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required.")

# Function to display the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = search_entry.get()
    if search_term:
        matching_contacts = []
        for contact in contacts:
            if (search_term.lower() in contact['Name'].lower()) or (search_term in contact['Phone']):
                matching_contacts.append(contact)
        update_contact_list()
        for contact in matching_contacts:
            contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
    else:
        update_contact_list()

# Function to update a contact
def update_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        contact = contacts[selected_index]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        contact['Name'] = name
        contact['Phone'] = phone
        contact['Email'] = email
        contact['Address'] = address
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Warning", "Please select a contact to update.")

# Function to delete a contact
def delete_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        contacts.pop(selected_index)
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Contact Book")

# Labels and Entry fields
name_label = tk.Label(app, text="Name:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

phone_label = tk.Label(app, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(app)
phone_entry.pack()

email_label = tk.Label(app, text="Email:")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

address_label = tk.Label(app, text="Address:")
address_label.pack()
address_entry = tk.Entry(app)
address_entry.pack()

# Buttons
add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(app, text="Search:")
search_label.pack()
search_entry = tk.Entry(app)
search_entry.pack()

search_button = tk.Button(app, text="Search", command=search_contact)
search_button.pack()

update_button = tk.Button(app, text="Update Contact", command=update_selected_contact)
update_button.pack()

delete_button = tk.Button(app, text="Delete Contact", command=delete_selected_contact)
delete_button.pack()

# Listbox to display contacts
contact_list = tk.Listbox(app)
contact_list.pack()

update_contact_list()

# Start the application
app.mainloop()
