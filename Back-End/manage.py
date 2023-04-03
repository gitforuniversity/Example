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
