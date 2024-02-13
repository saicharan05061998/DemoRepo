a = 10
b = 20.0


# addition of two numbers
def addition(num1, num2):
    sub = subtract(num1, num2)
    print("Type")
    print(type(sub))
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


sum = addition(a, b)
print(sum)
