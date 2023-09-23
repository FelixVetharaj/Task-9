# Task-9 - Question-3-Fibonacci series 1 to 50 using lambda
num = 1
num1 = 1
print(num)
print(num1)
for i in range(2, 50):
    result = lambda x,y: x+y
    num3 = result(num, num1)
    print(num3)
    num = num1
    num1 = num3
