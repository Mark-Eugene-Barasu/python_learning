# nested loops = a loop inside a loop

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
# end="" prevents the print function from moving to the next line after printing the symbolReplace the symbol with a space to create a hollow rectangle