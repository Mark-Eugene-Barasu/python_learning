# index operator [] = used to access a specific element in a collection using its index
# string, list, tuple
name = "Bro Code"
first_letter = name[0]

if(name[0].islower()):
    print("First letter is lowercase")
else:
    print("First letter is uppercase")

# name[0] = "B" # error, string is immutable
# lists are mutable
food = ["pizza", "hamburger", "hotdog", "spaghetti", "sushi"]
food[0] = "taco"
print(food[0]) # taco
print(food[1]) # hamburger
print(food[2]) # hotdog
print(food[3]) # spaghetti
print(food[4]) # sushi


