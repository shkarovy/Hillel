number = int(input("Enter number vor 4 Zahl pleas: "))

thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10

print(thousands)
print(hundreds)
print(tens)
print(ones)
