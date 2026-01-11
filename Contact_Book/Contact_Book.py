"""
Simple Contact Book Application
A beginner-friendly Python project with full CRUD operations
"""

import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def save_contacts(self):
        """Save contacts to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)
    
    def add_contact(self, name, phone, email=""):
        """Add a new contact"""
        if name in self.contacts:
            print(f"❌ Contact '{name}' already exists!")
            return False
        
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        self.save_contacts()
        print(f"✅ Contact '{name}' added successfully!")
        return True
    
    def view_contact(self, name):
        """View a specific contact"""
        if name in self.contacts:
            contact = self.contacts[name]
            print("\n📇 Contact Details:")
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return True
        else:
            print(f"❌ Contact '{name}' not found!")
            return False
    
    def view_all_contacts(self):
        """View all contacts"""
        if not self.contacts:
            print("📭 No contacts found!")
            return
        
        print("\n📖 All Contacts:")
        print("-" * 50)
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 50)
    
    def update_contact(self, name, phone=None, email=None):
        """Update an existing contact"""
        if name not in self.contacts:
            print(f"❌ Contact '{name}' not found!")
            return False
        
        if phone:
            self.contacts[name]['phone'] = phone
        if email is not None:
            self.contacts[name]['email'] = email
        
        self.save_contacts()
        print(f"✅ Contact '{name}' updated successfully!")
        return True
    
    def delete_contact(self, name):
        """Delete a contact"""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"✅ Contact '{name}' deleted successfully!")
            return True
        else:
            print(f"❌ Contact '{name}' not found!")
            return False
    
    def search_contact(self, query):
        """Search contacts by name"""
        results = {name: details for name, details in self.contacts.items() 
                   if query.lower() in name.lower()}
        
        if results:
            print(f"\n🔍 Found {len(results)} result(s):")
            print("-" * 50)
            for name, details in results.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print("-" * 50)
        else:
            print(f"❌ No contacts found matching '{query}'")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("📱 CONTACT BOOK APPLICATION")
    print("=" * 50)
    print("1. Add Contact")
    print("2. View Contact")
    print("3. View All Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Search Contacts")
    print("7. Exit")
    print("=" * 50)


def main():
    """Main function to run the contact book application"""
    contact_book = ContactBook()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            # Add Contact
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email (optional): ").strip()
            contact_book.add_contact(name, phone, email)
        
        elif choice == "2":
            # View Contact
            name = input("Enter name to view: ").strip()
            contact_book.view_contact(name)
        
        elif choice == "3":
            # View All Contacts
            contact_book.view_all_contacts()
        
        elif choice == "4":
            # Update Contact
            name = input("Enter name to update: ").strip()
            if name in contact_book.contacts:
                print("Leave blank to keep current value")
                phone = input("Enter new phone number: ").strip()
                email = input("Enter new email: ").strip()
                contact_book.update_contact(
                    name, 
                    phone if phone else None, 
                    email if email else None
                )
            else:
                print(f"❌ Contact '{name}' not found!")
        
        elif choice == "5":
            # Delete Contact
            name = input("Enter name to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                contact_book.delete_contact(name)
            else:
                print("Deletion cancelled.")
        
        elif choice == "6":
            # Search Contacts
            query = input("Enter search term: ").strip()
            contact_book.search_contact(query)
        
        elif choice == "7":
            # Exit
            print("\n👋 Thank you for using Contact Book! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1-7.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()