# largestOfThree.py
# dH 2/15/23
#
# approved solution for Largest of Three program
#
# input: three integers from the user
# processing: find the sum of the three integers and the largest of the three
# output: largest and total
#
# References:
#   https://www.w3schools.com/python/python_user_input.asp
#   https://www.w3schools.com/python/python_conditions.asp
#
#
#
print("\n\n This is the Largest of Three program...")
# input three integers from the user.
num1 = input("\nEnter your first integer: ")
num2 = input("\nEnter your second integer: ")
num3 = input("\nEnter your third and last integer: ")

print("num1 = " + num1 + " num2 = " + num2 + " and num3 = " + num3)

# Find the largest
largest = 0

if num1 > num2:
    if num1 > num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 > num3:
        largest = num2
    else:
        largest = num3

# output the largest
print("The largest is " + largest)

# find the sum
the_sum = int(num1) + int(num2) + int(num3)

# output the sum
print("The sum of " + num1 + " and " + num2 + " and " + num3 + " is " + str(the_sum))
