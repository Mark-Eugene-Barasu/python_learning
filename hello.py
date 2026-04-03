phrase = "Hello, World!"
print(phrase.lower())
print(phrase.upper()) 
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))  
print(phrase[0])  #H is the first character
print(phrase[7])    #W is the 8th character (index starts at 0)
print(phrase.index("X"))  #Find the index of 'X' (will raise an error if not found)
print(phrase.replace("Hello", "Hi"))  #Replace "Hello" with "Hi"
