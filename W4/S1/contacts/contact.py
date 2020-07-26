# Class Contact

class Contact:
    def __init__(self, fname, lname):

        self.fname = fname
        self.lname = lname
        self.email = ""
        self.phone_numbers = dict()
        self.labels = list()

        print(f"A new contact for '{self.fname}' has been created.")

    def __str__(self):
        return f"""
        Contact information for {self.lname.capitalize()}, {self.fname.capitalize()}.
        Contact has {len(self.phone_numbers)} phone numbers and {len(self.labels)} labels.
        """

    def add_phone(self, phone_number, label):
        self.phone_numbers[label] = phone_number

    def add_label(self, label):
        self.labels.append(label)
