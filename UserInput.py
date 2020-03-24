user_input = int(input("Please Enter Your Number: "))
s = 0

while user_input < 0:
    user_input = int(input("Please Enter Another Number: "))

while user_input:
    s += user_input % 10
    user_input //= 10

print("You've entered a positive number! The sum of the digits is: ", s)