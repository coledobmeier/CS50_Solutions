while True:
    try:
        frac = input("Fraction: ")
        frac = frac.split("/")

        numerator = (float(frac[0]))
        denominator = (float(frac[1]))

        if not numerator.is_integer() or not denominator.is_integer():
            raise ValueError("Numerator and denominator must be whole numbers.")

        numerator *= 10
        denominator *= 10

        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        if numerator > denominator:
            raise ValueError("Numerator cannot be greater than denominator")

        if (numerator <= denominator):
            #basic division
            percentage = (numerator/denominator)
            percentage = (round(100*percentage))
            #E and F cases
            if (percentage <= 1):
                print("E")
            elif (percentage >= 99):
                print("F")
            else:
                print(str(percentage) + "%")
        break
    except(ValueError, IndexError):
        print("Invalid input. Please enter a valid fraction")

