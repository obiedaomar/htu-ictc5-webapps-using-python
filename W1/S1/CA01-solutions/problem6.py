days = 3
hours = 14
minutes = 27
seconds = 33

total_in_seconds = (days * 24 * 60 * 60) + \
    (hours * 60 * 60) + (minutes * 60) + (seconds)


print("%d days, %d hours, %d minutes, %d seconds in seconds is: %d" %
      (days, hours, minutes, seconds, total_in_seconds))
