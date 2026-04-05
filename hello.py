# tuple = a collection which is ordered and unchangeable used to group together related data
student = ("Alice", 25, "Computer Science")
print(student)  # prints ('Alice', 25, 'Computer Science')
print(student[0])  # prints 'Alice'
print(student[1])  # prints 25
print(student[2])  # prints 'Computer Science'
# student[0] = "Bob"  # This will raise an error because tuples are immutable
# However, you can concatenate tuples to create a new tuple
new_student = student + ("Senior",)
print(new_student)  # prints ('Alice', 25, 'Computer Science', 'Senior')    