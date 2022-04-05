givenTime = "07:05:45PM".split(":")
convertedTime = givenTime
if givenTime[2].endswith("AM"):
    if givenTime[0] == "12":
        convertedTime[0] = "00"
else:
    if 1 <= int(givenTime[0]) <= 11:
        convertedTime[0] = int(givenTime[0]) + 12

print("{}:{}:{}".format(convertedTime[0], convertedTime[1], convertedTime[2][0:2]))