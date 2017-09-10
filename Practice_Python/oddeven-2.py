userNum = input("Please enter a number: ")

if int(userNum) % 4 == 0:
    print(userNum + " is a multiple of 4")
elif int(userNum) % 2 == 0:
    print(userNum + " is an even number")
else:
    print(userNum + " is an odd number")
