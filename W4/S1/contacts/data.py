from contact import Contact
from contact_book import ContactBook

book = ContactBook()

# Contact GK
contact = Contact("George", "Khoury")

contact.add_phone("123456789", "Work")
contact.add_phone("001234567", "Home")

contact.add_label("HTU")
contact.add_label("Programmer friends")

book.add(contact)

# Contact GK
contact = Contact("Bert", "Khoury")

contact.add_phone("123456789", "Private")

contact.add_label("Sesame Street")
contact.add_label("Friends")

book.add(contact)

# Print all contacts
book.print_all_contacts()

# Find by name
print(book.search("friends"))

print(book.search("Bert"))
print(book.search("George"))
print(book.search("friend"))
