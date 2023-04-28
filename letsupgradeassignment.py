def odd_or_not(n):
    result = "odd"
    if n%2 == 0:
        result = "even"
    return result
x = int(input("Enter a number: "))
print(odd_or_not(x))
