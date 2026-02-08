# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder: mehreen ansari
# Date: 08/02/26

print("****SIMPLE INTEREST CALCULATOR****")
principal = int(input())
rate = int(input())
time = int(input())
simple_interest = (principal * rate * time) / 100
print(f"The simple interest is : ",(simple_interest))
