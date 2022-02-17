def Age():
    age1 = input("Input a value for age1: ")
    age2 = input("Input a value for age2: ")
    print("Original:", age1, age2,)
    numbers = [age1, age2]
    print (sorted(numbers))

def Matrix():
    listofvalues = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for lists in listofvalues:
        print(*lists)

while True:
    thing = input("enter something: ")
    if thing == ("swapper"):
        Age()
    if thing == ("matrix"):
        Matrix()


