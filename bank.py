greeting = input("Greeting: ")

if "hello" in greeting:
    print("$0")

elif greeting.__contains__("Hello"):
    print("$0")

elif ("H") in greeting[0]:
    print("$20")

elif ("h") in greeting[0]:
    print("$20")

else:
    print("$100")
