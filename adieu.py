def main():
    import sys

    # Collect names until EOF (Ctrl-D or Ctrl-Z)
    print("Enter names, one per line. Press Ctrl-D to finish.")
    try:
        names = []
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    # Ensure at least one name is entered
    if not names:
        sys.exit("Error: At least one name is required.")

    farewell = format_farewell(names)

    # Print the farewell message
    print(f"Adieu, adieu, to {farewell}")


def format_farewell(names):
    """Format the list of names into a grammatically correct farewell message."""
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()
