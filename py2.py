print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))

        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start > end:
            print("Start number must be smaller than end number.")
        else:
            total = 0

            for i in range(start, end + 1):
                if i % 2 == 0:
                    print("Number", i, "is even")
                else:
                    print("Number", i, "is odd")

                total = total + i

            print("Sum of all numbers from", start, "to", end, "is:", total)

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice")
