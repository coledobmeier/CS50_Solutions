import random

def get_positive_integer(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass  # Ignore invalid input
        print("Please enter a positive integer.")

def main():
    # Prompt the user for the level
    level = get_positive_integer("Level: ")

    # Generate a random target number
    target = random.randint(1, level)

    while True:
        # Prompt the user to guess
        guess = get_positive_integer("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
