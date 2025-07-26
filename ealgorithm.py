# user input
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# Euclidean Algorithm
#a = qb + r
def func(a, b):
    r = a % b #calculates remainder
    if r > 0:
        result = func(b, r)
    else:
        result = b #sets result to first value
    return result

#Displays Greatest Common Divisor
gcd = func(num1, num2)
print(gcd)