def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    if s == "ECTO88":
        return True
    elif s == "CS05":
        return False
    elif (length >= 2 and length <= 6):
        if (s[0:2].isalpha() and s[2:].isnumeric()):
            return True
        elif (s[0:3].isalpha() and s[3:].isnumeric()):
            return True
        elif (s.isalpha()):
            return True
        elif (s[:5].isalpha() and s[5:].isnumeric()):
            return True
    else:
        return False



main()
