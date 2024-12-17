print("Amount Due: 50")
amount = 50
while amount > 0:
    money = int (input("Insert Coin: "))
    if money == 25 or money == 10 or money == 5:
        amount = (amount - money)
        if amount > 0:
            print("Amount Due: " + str(amount))
    elif money == 50:
        amount = 0
        print("Change Owed: 0")
    else:
        print("Amount Due: " + str(amount))
if amount <= 0:
    change = abs(amount)
    print("Change Owed: " + str(change))
