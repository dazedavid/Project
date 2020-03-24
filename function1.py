# Functions 
# Addition Function 
def add_numbers(a,b):

   c = (int(a)) +(int(b))
   return c

# Substraction Function 
def sub_numbers(a,b):

   c = (int(a)) -(int(b))
   return c

# Multiplication Function 
def mult_numbers(a,b):

   c = (int(a)) *(int(b))
   return c

# Division Function 
def div_numbers(a,b):

   c = (int(a)) /(int(b))
   return c

# Taking input of two numbers 
e = input("enter first number")
f = input("enter second number")

# Printing numbers
print ("The sum of number is =", add_numbers(e, f))
print ("The difference of two number is =",(abs(sub_numbers(e, f))))
print ("The multiplication of two numbers is =", mult_numbers(e, f))
print ("The division is =", div_numbers(e, f))