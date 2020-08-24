class UserDB:

    users = set()

    def add_user(self, user):
        print(f"User '{user.username}' added.")
        self.users.add(user)
    
    def get_user_by_username(self, username):

        for user in self.users:
            if user.username == username:
                return user
            else:
                return None
                
class User:

    contact_book = None
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_login(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            return False

    def assign_contact_book(self, contact_book):
        self.contact_book = contact_book