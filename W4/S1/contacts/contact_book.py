from contact import Contact

# class ContactBook


class ContactBook:
    def __init__(self):
        self.contacts = list()

    def add(self, contact):
        self.contacts.append(contact)

    def get_contact(self, contact, keyword):
        if contact.fname.lower() or contact.lname.lower() or contact.email.lower() == keyword:
            return contact
        else:
            return None

    def search(self, keyword=""):
        results = list()

        for contact in self.contacts:
            contact = self.get_contact(contact, keyword.lower())

            if contact != None:
                results.append(contact)

            if len(results) > 0:
                print(
                    f"Found {len(results)} results matching the keyword '{keyword}'.")
                for contact in results:
                    print(contact)
            else:
                print(f"No results found matching the keyword: '{keyword}'.")

    def print_all_contacts(self):
        for contact in self.contacts:
            print(contact)
