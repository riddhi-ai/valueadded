n = int(input("Enter a number: "))

result = 1
for i in range(1, n + 1):
    result *= i

print("Factorial:", result)

"""
for backward    (1*2*3*4*5)
for i in range (n,0)
fact = fact*i 
print(fact) 
"""