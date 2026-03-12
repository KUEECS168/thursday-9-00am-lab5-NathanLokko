groceryList = []
choice = 0

while choice == 1 or choice == 2 or choice == 3 or choice == 0:
    print("Welcome To Your Shopping List!")
    print(" 1) Add item" , "\n" , "2) Remove item" , "\n" , "3) print list" , "\n" , "4) Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("What will you add to the list? ")
        groceryList.append(item)
    elif choice == 2:
        index = int(input("Which item will you check off? ")) - 1
        item = groceryList[index]
        firstLetter = item[0]
        lastLetter = item[len(item) - 1]
        middleLetters = len(item) - 2
        dashes = '-' * middleLetters
        groceryList[index] = firstLetter + dashes + lastLetter
    elif choice == 3:
        print("Here is your list:")
        print(groceryList)
    elif choice == 4:
        print("Goodbye!")
        choice = 0


    