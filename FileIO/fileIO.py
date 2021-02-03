# jabber = open("/Users/Gamer/Documents/Study.txt", "r")
#
# for line in jabber:
#     if "Control unit" in line:
#         print(line, end="")
# jabber.close()

# no need to explicitly close the file because the 'with' takes care of that
with open("/Users/Gamer/Documents/Study.txt", "r") as jabber:
    for line in jabber:
        if "CONTROL UNIT" in line.upper():
            print(line, end="")
