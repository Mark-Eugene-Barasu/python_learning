# strings in python
name = "John" 
surname = "Doe"
print(name + " " + surname) # concatenation of strings
print(f"My name is {name} {surname}") # using f-string for formatting   

full_name = name + " " + surname
print(full_name) # printing the full name   
print(full_name.upper()) # converting to uppercase
print(full_name.lower()) # converting to lowercase

print(full_name.isupper()) # checking if the string is uppercase
print(full_name.islower()) # checking if the string is lowercase

print(len(full_name)) # getting the length of the string

print(full_name[0]) # accessing the first character of the string
print(full_name[1]) # accessing the second character of the string
print(full_name[-1]) # accessing the last character of the string   

print(full_name.index("Doe")) # finding the index of the substring "Doe"
print(full_name.replace("John", "Jane")) # replacing "John" with "Jane"