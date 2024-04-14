num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    num1, num2 = num2, num1

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
print(f"The HCF of {num1} and {num2} is: {num1}")
