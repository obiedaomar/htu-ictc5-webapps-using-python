def ask_user():
    while r := input("Do you want to save? (Enter yes/no)").lower() not in {"yes", "no"}:
        pass
    return r.lower() == "yes"


ask_user()
