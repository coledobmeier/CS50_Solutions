def main():
    # List of month names
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date_input = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ").strip()

        # Check for MM/DD/YYYY format
        if "/" in date_input:
            parts = date_input.split("/")
            if len(parts) == 3:
                month, day, year = parts
                if month.isdigit() and day.isdigit() and year.isdigit():
                    month, day, year = int(month), int(day), int(year)
                    if validate_date(month, day, year):
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
        # Check for Month Day, Year format
        elif "," in date_input:
            parts = date_input.split(",")
            if len(parts) == 2:
                month_day, year = parts
                year = year.strip()
                if year.isdigit():
                    year = int(year)
                    month_day_parts = month_day.split()
                    if len(month_day_parts) == 2:
                        month_name, day = month_day_parts
                        if month_name in months and day.isdigit():
                            month = months.index(month_name) + 1
                            day = int(day)
                            if validate_date(month, day, year):
                                print(f"{year:04d}-{month:02d}-{day:02d}")
                                break
        # If input is invalid
        print("Invalid date format. Please try again.")

def validate_date(month, day, year):
    """Validates that the month, day, and year are within reasonable bounds."""
    if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
        return True
    return False

if __name__ == "__main__":
    main()
