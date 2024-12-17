camel = input("camelCase: ")
print("snake_case: " , end="")
for c in camel:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")
print("")


