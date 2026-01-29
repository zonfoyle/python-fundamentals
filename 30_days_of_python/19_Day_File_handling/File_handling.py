#File Handling
import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt",)
print(f.read())
print(f.read(4)) # Runs the first for characters of the file


print(f.readline()) # Read the first line only
print(f.readline()) # Becuase of the first, this will read second line as follow.


for line in f:
    print(line)

f. close() # This cloeses the file

try:
   f = open("name_list.txt")
   print(f.read())
except:
   print("The file you want to read doesn't exist")
finally:
   f.close()


# Append - Creates the files if it doesn't exist

f = open("names.txt, "a")
f.write("Foyle")
f.close()

f = open("names.txt, "a")
print(f.read())
f.close()


# Write - (overwrite)

f = open("context.txt")
f.write(" I deleted all of the context")
f.closed()

f = open("context.txt", "w")
print(f.write())
f.closed()


# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist

f = open("name_list.txt", "w")
f.close()


# Creates the specififed file, but returns an error if the file exists
  if not os.path.exists("dave.txt"):
       f = open("dave.txt", "x")
       f.close()


# Delete  a file

# avoide an error if it doesn't exist

if os.path.exists("Zonique.txt"):
     os.remove("Zonique.txt")
else:
    print("The file you wish to delete does not exist")