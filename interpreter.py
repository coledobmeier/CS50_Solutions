expression = input("Expression: ")
x, y, z = expression.split()

match y:
    case "+":
        equals = float(x) + float(z)
    case "-":
        equals = float(x) - float(z)
    case "/":
        equals = float(x) / float(z)
    case "*":
        equals = float(x) * float(z)

print(equals)
