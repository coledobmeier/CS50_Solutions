lists = {}
while True:
    try:
        item = input()
        item = item.upper()
        if item in lists.keys():
            lists[item] += 1
        else:
            lists[item] = 1
    except EOFError:
        break

mykeys = list(lists.keys())
mykeys.sort()

sd = {i: lists[i] for i in mykeys}
for key, value in sd.items():
    print(value, key)

#for key, value in lists.items():
    #print(value, key)
