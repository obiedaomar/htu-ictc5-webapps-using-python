# Handling user input

def ask_user():
    # while the user input is not in the set of allowed values, pass
    while r := input("Do you want to save? (Enter yes/no)").lower() not in {"yes", "no"}:
        pass
    # otherwise return "yes"
    return r.lower() == "yes"


# call ask_user()
ask_user()
