print("Hello World!")
# Day-1 exercise 1.1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print(\"what to print\")")
# Print multiple lines
print("Hello World!\nHello World!\nHello World!")
# Concatenate with '+'
print("Hello" + "Aditya")      # it will print HelloAditya
# We can add space in b/w by adding space after Hello or before Aditya or add a new string in b/w using + sign as " "
# Day-1 exercise 1.2  debugging
print("Day 1 - String Manipulation")   # added " in starting
print("String Concatenation is done with \"+\" sign.") # added \ before 2nd "" to print them also
print('e.g. print("Hello " + "world")') # remove space from starting
print("New lines can be created with a backslash and n.") # removed the extra ( from starting
# Input function- to take input from user
input("What is your name?")   # it will ask name and when i text something then nothing will happen as its not being used anywhere
print("Hello " + input("What is your name?"))  # now it will ask name and then print that name also as Hello Aditya bcz of print
# Day-1 exercise 1.3  count of char in name
# i was stuck as i was using direct result which is no. so need to convert it into string while concatenation
print("There are " + str(len(input("What is your name?"))) + " characters in your name.")
# Day-1 exercise 1.4  reverse the value of a & b
a = input("a:")
b = input("b:")
# add code here
c = a
a = b
b = c
# till here
print("a = " + a)
print("b = " + b)
# Day1 - Prject [Band name generator]
print("Welcome to the band name generator.")
city = input("Which city did you grow up in?\n")
print(city)
pet = input("What is the name of a pet?\n")
print("Your band name could be " + city + " " + pet)