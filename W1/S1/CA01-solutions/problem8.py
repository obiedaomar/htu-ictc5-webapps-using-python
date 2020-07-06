password = "P@$$w0rd"
count_char = 0
count_symbol = 0
count_digit = 0

for c in password:
    if c.isdigit():
        count_digit += 1
    elif c.isalpha:
        count_char += 1
    else:
        count_symbol += 1

print("Your password contains %d chars. %d digits. %d symbols." %
      (count_char,  count_digit, count_symbol))
