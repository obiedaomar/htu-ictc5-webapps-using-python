from contact import Contact
from contact_book import ContactBook

# create contact for Cookie Monster

cookie = Contact("Cookie", "Monster")
cookie.add_phone("12345678", "Work")
cookie.add_phone("00123456", "Cookie Line")
cookie.add_label("Cookie")
cookie.add_label("Friend")

# create contact for Don Music

don = Contact("Don", "Music")
don.add_label("Music")
don.add_label("Friend")

# create contact for Roosevelt Franklin

roosevelt = Contact("Roosevelt", "Franklin")

# create a contact book
sesame_street = ContactBook()

# add contacts to contact book
sesame_street.add(cookie)
sesame_street.add(don)
sesame_street.add(roosevelt)

# print the number of contacts in contact book
print(len(sesame_street.contacts))

# print all contacts
sesame_street.print_all_contacts()
