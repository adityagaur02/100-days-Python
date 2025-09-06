# Data Types

# String
print("Hello"[0])    # H and [4]->o

# Integer
print(123 + 345)      # 123,456,789 is written as 123_456_789 in python for more visual

# Float
3.14159

# Boolean
True
False

# type of data
num_char = len(input("What is your Name?"))
print(type(num_char))

# Day-2 exercise 2.1
# sum of digits of number
two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit
print(result)

# Mathematic Operators
3 + 5
7 - 4
3 * 2
6 / 3  # / will always give o/p as float like 2.0
2 ** 2  # ** is used as power like 2 ** 3 = 8
# Priority of operators [PEMDAS] in which * / , + - are treated on same level respectively
print(3 * 3 + 3 / 3 - 3)    # o/p 7.0

# Day-2 exercise 2.2
# BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
# round() function
print(round(8 / 3, 2))   # it will gives us float
print(round(8 // 3))     # it will directly gives us integer
# instead of result = result + 1, we can result += 1

# f-string:- instead of converting all data/value to string, we can do it all together using "f" and add value/data in {}
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Day-2 exercise 2.3
age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)

# Project: Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")