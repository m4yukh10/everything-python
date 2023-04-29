def century(age):
    m = 2023 - age
    hundred = m+100
    return hundred
x = input("What is your name? ")
y = int(input("Enter your age: "))
hundred_year= century(y)
print(f"Hey {x}, you will turn hundred in {hundred_year}!")
