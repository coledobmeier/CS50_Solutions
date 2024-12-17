import emoji

def emojize_text(text):
    return emoji.emojize(text)

# Prompt user for input
user_input = input("Input: ")

# Convert the input to its emojized version
emojized_output = emojize_text(user_input)

# Output the result
print(f"Output: {emojized_output}")
