import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join([f"{name}: {details['Phone']}" for name, details in self.contacts.items()])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self, query):
        results = [(name, details) for name, details in self.contacts.items()
                   if query.lower() in name.lower() or query in details['Phone']]
        if not results:
            messagebox.showinfo("Info", "No matching contacts found.")
        else:
            matching_contacts = "\n".join([f"{name}: {details['Phone']}" for name, details in results])
            messagebox.showinfo("Matching Contacts", matching_contacts)

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        else:
            messagebox.showinfo("Info", f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
        else:
            messagebox.showinfo("Info", f"Contact '{name}' not found.")


class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contact_book = ContactBook()

        # Create and set up widgets
        self.label = tk.Label(root, text="Contact Book", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_add.pack(pady=5)

        self.button_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.button_view.pack(pady=5)

        self.button_search = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.button_search.pack(pady=5)

        self.button_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.button_update.pack(pady=5)

        self.button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.button_delete.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        address = simpledialog.askstring("Input", "Enter address:")
        if name and phone:
            self.contact_book.add_contact(name, phone, email, address)

    def view_contacts(self):
        self.contact_book.view_contacts()

    def search_contact(self):
        query = simpledialog.askstring("Input", "Enter name or phone number to search:")
        if query:
            self.contact_book.search_contact(query)

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter name of the contact to update:")
        phone = simpledialog.askstring("Input", "Enter new phone number:")
        email = simpledialog.askstring("Input", "Enter new email address:")
        address = simpledialog.askstring("Input", "Enter new address:")
        if name:
            self.contact_book.update_contact(name, phone, email, address)

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter name of the contact to delete:")
        if name:
            self.contact_book.delete_contact(name)


if __name__ == "__main__":
    root = tk.Tk()
    contact_book_gui = ContactBookGUI(root)
    root.mainloop()
