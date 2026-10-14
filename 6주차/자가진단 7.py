hour, minute = map(int, input().split())

if hour >= 12:
    meridiem = "PM"
    if hour > 12:
        hour -= 12
else:
    meridiem = "AM"
    if hour == 0:
        hour = 12


print("%02d : %02d %s" % (hour, minute, meridiem))
