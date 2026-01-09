"""String Methods in Python"""
name = input("Enter your name: ") #input() is a built-in function that: Displays a prompt to the user
                                  # Also Waits for user input and always returns a string

result = len(name) #len function to get length of string ( It returns the number of characters in a string)
                   # Example: len("Zonique") #7 and len("Zonique Foyle") #13 (space included)

result = name.find("o") ##.find() returns the index of the first occurrence. Returns -1 if not found.

results = name.rfind("o") #rfind() returns the index of the last occurrence. Returns -1 if not found.
name = name.capitalize() #.capitalize() converts the first character to upper case

name =name.upper() #.upper() converts a string into upper case

name = name.lower() #.lower() converts a string into lower case

result = name.isdigit() #.isdigit() checks if all the characters in the text are digits

result = name.isalpha() #.isalpha() checks if all the characters in the text are letters (a-z)

print(result)


# Data types in this are (name, result, str, and bool "true results")

