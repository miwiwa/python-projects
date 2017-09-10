userNum = input("Please enter a number: ")

a = range(1, int(userNum) + 1)
b = []

[b.append(num) for num in a if int(userNum) % num == 0]

print(b)
