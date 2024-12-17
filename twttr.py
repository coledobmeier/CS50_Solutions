def main():
    x = input("Input: ")
    print(shorten(x))


def shorten(x):
    vowels = ['a', 'e', 'i', 'o', 'u',]
    output_word = ""
    for s in x:
        if s.lower() not in vowels:
            output_word += s
    return f"Output: {output_word}"


if __name__ == "__main__":
    main()
