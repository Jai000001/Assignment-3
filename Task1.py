a = input("Enter a number: ")
a = int(a)
def factorial(a):
    fact = 1
    for i in range(a+1):
        if i<2:
            fact = fact*1
        else:
            fact = fact*(i)
    return fact
print("Factorial of", a ,"is", factorial(a))