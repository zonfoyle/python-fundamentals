"""Day 4 — String Methods in Python (Notes + Practice)"""

# ------------------------------------------------------------
# 1) USER INPUT (input() always returns a STRING)
# ------------------------------------------------------------
name = input("Enter your name: ")  # input() displays a prompt, waits for input, and returns a str

# ------------------------------------------------------------
# 2) len() FUNCTION
# ------------------------------------------------------------
result = len(name)  # len() returns the number of characters in a string (spaces count too)
# Example: len("Zonique") -> 7
# Example: len("Zonique Foyle") -> 13 (space included)
print("len(name):", result)

# len() also works with other data types:
numbers = [10, 20, 30, 40]
print("len(list):", len(numbers))  # Output: 4

fruits = ("apple", "banana", "orange")
print("len(tuple):", len(fruits))  # Output: 3

student = {"name": "Zonique", "major": "Business Analytics", "year": "Graduate"}
print("len(dict):", len(student))  # Output: 3 (counts keys)

# ------------------------------------------------------------
# 3) find() and rfind()
# ------------------------------------------------------------
# .find() returns the index of the FIRST occurrence. Returns -1 if not found.
first_o = name.find("o")
print("name.find('o'):", first_o)

# .rfind() returns the index of the LAST occurrence. Returns -1 if not found.
last_o = name.rfind("o")
print("name.rfind('o'):", last_o)

# ------------------------------------------------------------
# 4) capitalize(), upper(), lower()
# ------------------------------------------------------------
# These return NEW strings. They do NOT change the original unless you reassign.
print("name.capitalize():", name.capitalize())  # First letter uppercase, rest lowercase
print("name.upper():", name.upper())            # All uppercase
print("name.lower():", name.lower())            # All lowercase

# ------------------------------------------------------------
# 5) isdigit() and isalpha()
# ------------------------------------------------------------
# .isdigit() checks if ALL characters are digits (0-9). No spaces, no decimals, no negatives.
print("name.isdigit():", name.isdigit())

# .isalpha() checks if ALL characters are letters (a-z / A-Z). No spaces, no digits, no symbols.
print("name.isalpha():", name.isalpha())

# ------------------------------------------------------------
# 6) strip()
# ------------------------------------------------------------
# .strip() removes extra spaces from the beginning and end ONLY (not the middle)
messy_name = "   Zonique   "
print("messy_name.strip():", messy_name.strip())

# common use: cleaning user input
email = input("Enter your email: ").strip()
print("clean email:", email)

# ------------------------------------------------------------
# 7) replace()
# ------------------------------------------------------------
# .replace(old, new) swaps text
text = "I love Python"
print("replace love -> like:", text.replace("love", "like"))

# cleaning messy values (real-life use)
price = "$1,200"
clean_price = price.replace("$", "").replace(",", "")
print("clean_price:", clean_price)  # Output: 1200

# ------------------------------------------------------------
# 8) split() and join()  (VERY IMPORTANT for AWS scripting)
# ------------------------------------------------------------
# .split() breaks a string into a LIST
services = "ec2 s3 iam lambda"
service_list = services.split()  # splits on spaces by default
print("service_list:", service_list)

# loop through values after split
for service in service_list:
    print("service:", service)

# split with a specific separator (comma)
items = "apple,banana,orange"
items_list = items.split(",")
print("items_list:", items_list)

# .join() takes a LIST of strings and combines them into ONE string
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print("joined sentence:", sentence)

# AWS-style example: resource naming
parts = ["prod", "web", "server"]
resource_name = "-".join(parts)
print("resource_name:", resource_name)  # prod-web-server

# .split() + .join() together
sentence2 = "Python is fun"
new_sentence = "-".join(sentence2.split())
print("split + join:", new_sentence)  # Python-is-fun

# Common beginner mistake:
# numbers = [1, 2, 3]
# result = ",".join(numbers)  # ERROR because join needs strings

numbers = [1, 2, 3]
numbers_str = [str(num) for num in numbers]  # convert each int to str
result_join = ",".join(numbers_str)
print("joined numbers:", result_join)

# ------------------------------------------------------------
# 9) startswith() and endswith()
# ------------------------------------------------------------
bucket_name = "prod-logs-bucket"
print("bucket_name.startswith('prod'):", bucket_name.startswith("prod"))

filename = "terraform.tf"
print("filename.endswith('.tf'):", filename.endswith(".tf"))

# multiple options using a tuple
image_file = "image.jpeg"
print("image_file.endswith(('.png','.jpg','.jpeg')):", image_file.endswith((".png", ".jpg", ".jpeg")))

# ------------------------------------------------------------
# 10) count()
# ------------------------------------------------------------
# .count() counts how many times something appears in a string
log = "ERROR ERROR WARNING ERROR INFO"
error_count = log.count("ERROR")
print("error_count:", error_count)

# ------------------------------------------------------------
# 11) CREATING STRINGS IN PYTHON
# ------------------------------------------------------------
letter = "P"  # A string can be a single character or a bunch of text
print(letter)         # Output: P
print(len(letter))    # Output: 1

greeting = "Hello, World!"  # single or double quotes both work
print(greeting)             # Output: Hello, World!
print(len(greeting))        # Output: 13

# multiline string using triple quotes
multiline_string = """I am pretty good with computers.
I love coding and I am enjoying the 30 days of Python challenge.
That is why I started doing the 30 days of python."""
print(multiline_string)

# ------------------------------------------------------------
# 12) STRING CONCATENATION (using +)
# ------------------------------------------------------------
first_name = "Zonique"
last_name = "Foyle"
space = " "
full_name = first_name + space + last_name  # + operator concatenates strings
print(full_name)  # Output: Zonique Foyle

print("len(first_name):", len(first_name))
print("len(last_name):", len(last_name))
print("len(full_name):", len(full_name))

# ------------------------------------------------------------
# 13) ESCAPE SEQUENCES (YES—learn these 4)
# ------------------------------------------------------------
# \n = new line
# \t = tab
# \\ = backslash
# \" = quote inside a string
print("I hope everyone is enjoying the 30 days of Python challenge.\nDo you?")  # line break
print("Days\tTopics\tExercises")  # tab spacing
print("Day 1\tStrings\tPractice")
print("This is a backslash symbol (\\)")
print("In every programming language it starts with \"Hello, World!\"")

