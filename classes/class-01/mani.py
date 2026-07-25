from calculate import checkGreater, sum

while True:
    print("1: Add: ")
    print("2: Check Greater: ")
    print("3: Exit: ")
    choice: int = int(input("Enter your choice: "))

    nOne: int = int(input("Enter first number: "))
    nTwo: int = int(input("Enter second number: "))

    if choice == 1:
        result: int = sum(nOne, nTwo)
        print(f"The sum of {nOne} and {nTwo} is: {result}")
    elif choice == 2:
        result: int = checkGreater(nOne, nTwo)
        print(f"The greater number between {nOne} and {nTwo} is: {result}")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")