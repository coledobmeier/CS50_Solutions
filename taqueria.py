prices = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0.00

while True:
    try:
        item = input("Item: ")
        item = item.lower()
        if item in prices:
            total += float(prices[item])
            print(f"Total: ${total:.2f}")
        elif item == ("stop"):
            print(f"Total: ${total:.2f}")
            break
    except EOFError:
        break
