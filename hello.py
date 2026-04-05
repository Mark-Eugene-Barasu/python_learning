# if statement = a block of code that will execute if it's condition is true
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult!")
else:
    print("You are a child!")


# elif statement = a block of code that will execute if it's condition is true
# and is used after if statement and before else statement      
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult!")
elif age >= 13:
    print("You are a teenager!")
else:
    print("You are a child!")