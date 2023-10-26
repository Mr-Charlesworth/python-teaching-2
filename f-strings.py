some_number = 42
print("Isn't it annoying when you are trying to concatenate using '+' but you need to convert if it's a number?")
print("E.g. Talking about meaningful numbers such as " + str(some_number) + " requires the str() function")
print("Is there any easier way?")

# To use 'f-strings' just put an 'f' before the string quotation mark and you're good to go.
# Variables that contain a string or something that can be converted to a string can be placed inside braces {like_this}
print(f"Using F-Strings makes it easier to say that {some_number} is the meaning of life the universe and everything")
