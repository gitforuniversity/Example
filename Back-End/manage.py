def counter(num1, num2):
    new = []

    for i in range(num1, num2):
        new.append(i)
    
    return new

def length(list):
    counter = 0

    for i in list:
        counter += 1

    return counter

def printer(string):
    print(string)

def manage(num1, num2):

    sum = 0

    for i in range(num1, num2):
        sum += i

    return sum

