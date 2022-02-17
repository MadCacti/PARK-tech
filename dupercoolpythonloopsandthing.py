number1 = int(input("enter1"))
number2 = int(input("enter2"))
placeholder = 0
def sorter (number1, number2):
    print(number1)
    print(number2)
    if number1 > number2:
        number1 = number1
        number2 = number2
    else:
        # number1, number2 = number2, number1
        placeholder = number2
        number2 = number1
        number2 = placeholder


sorter(number1, number2)

print ("number1 sorted ", number1)
print ("number2 sorted ", number2)