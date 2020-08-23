ans = 'y'
while ans is 'y':
    count = input("Please enter the number to FizzBuzz up to: ")
    count = int(count)
    for i in range(1, count + 1):
        if i % 15 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif  i % 5 == 0:
            print(i, "Buzz")
        else:
            print(i)
    ans = input("Would you like to contine? y/n\n")
