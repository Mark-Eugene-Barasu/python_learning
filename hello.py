# functions = reusable pieces of code that perform a specific task

def say_hello():
    print("Hello, World!")

say_hello()  # calling the function to execute its code

# functions can also take parameters to make them more flexible
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")  # calling the function with an argument