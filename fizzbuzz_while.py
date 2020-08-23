cont = "y"
while cont is "y":
    num = input("Please enter to fizzbuzz\n")
    num = int(num)
    if num % 5 == 0 and num % 3 == 0:
        print(num, "= FizzBuzz")
    elif num % 3 == 0:
        print(num, "= Fizz")
    elif num % 5 == 0:
        print(num, "= Buzz")
    else:
        print(num, "cannot be fizzed or buzzed")
    cont = input("\nWould you like to continue? y/n\n")


