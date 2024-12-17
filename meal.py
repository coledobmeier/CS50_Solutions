def main():
   time = str(input("What time is it? "))
   time = convert(time)

   if time >= 7 and time <= 8:
      print("Breakfast time")
   elif time >= 12 and time<= 13:
      print("Lunch time")
   elif time >= 18 and time <= 19:
      print("Dinner time")
   else:
      print("")


def convert(time):
   hours, minutes = time.split(":")
   hours, minutes = float(hours), float(minutes)
   minutes = minutes/60
   time = float(hours + minutes)

   return time


if __name__ == "__main__":
    main()
