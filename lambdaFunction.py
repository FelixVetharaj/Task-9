#Task-9-Question-1-Ecxpected ouput of code
#Answer - prints a list with data element greater than 4. In the below data all the elements greater than 4. So it prints the full list

data = [10, 501, 22, 37, 100, 999, 87, 351]

result = filter(lambda x: x >4, data)
print(list(result))
