# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
num_days_year = 365
seconds_in_day = 86400

print("Here are the days:", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

print('The days of the week are: %s' % days)
print('The months of the year are: \n%s' % months)
print('There are %d days in a year. %d seconds in a day. %d seconds in a year.' %
      (num_days_year, seconds_in_day, num_days_year * seconds_in_day))
