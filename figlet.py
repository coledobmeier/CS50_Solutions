import sys
import pyfiglet
import random

def main():
    args = sys.argv

    if len(args) == 1:
        font = random.choice(pyfiglet.FigletFont.getFonts())
    elif len(args) == 3 and (args[1] == "-f" or args[1] == "--font"):
        if args[2] in pyfiglet.FigletFont.getFonts():
            font = args[2]
        else:
            sys.exit("Error: Font not found. Use a valid font name.")
    else:
        sys.exit("Usage: figlet.py [-f FONT_NAME]")

    text = input("Input: ")

    figlet = pyfiglet.Figlet(font=font)
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
