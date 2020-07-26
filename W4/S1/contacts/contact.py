# Class Contact

class Contact:

    # init for Contact(fname, lname)
    def __init__(self, fname, lname):

        #
        # instance attributes
        #

        self.fname = fname
        self.lname = lname
        self.email = ""
        self.phone_numbers = dict()
        self.labels = list()

        print(f"A new contact for '{self.fname}' has been created.")

    #
    # instance methods
    #

    # override __str__()
    def __str__(self):
        # override __str__
        return f"""
        Contact information for {self.lname.capitalize()}, {self.fname.capitalize()}.
        Contact has {len(self.phone_numbers)} phone numbers and {len(self.labels)} labels.
        """

    # add_phone(phone_number, label)
    def add_phone(self, phone_number, label):
        # add the phone_number to the contact list of phone numbers
        self.phone_numbers[label] = phone_number

    # add_label(label)
    def add_label(self, label):
        # append label to the contact list of labels
        self.labels.append(label)
