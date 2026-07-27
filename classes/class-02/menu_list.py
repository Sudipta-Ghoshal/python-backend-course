# Since we dont have navbar, so we have to create Menu Driven Program using List
# Declaring a list to store multiple data
data_list: list = ['24', '20', '22', '22.5', '23.33' ,'sudipta', '24', '25', '20', 'apple', '30', '32', '50']
# data_list: list = [ 'apple', 'sudipta']
# data_list: list = list()
print(type(data_list))

# num_list = []
# def number_list(itm_list):
#     for itme in itm_list:
#         try:
#             num = float(item)
#             if(num.is_integer()):
#                 num_list.append(int(num))
#             else:
#                 num_list.append(num)
#         except:
#             pass

# print(20 == 20.0)
# print(20.0.is_integer())

while True:   # Infinite loop boolean True
    print("\n------ MENU ------")
    print("1. Add data")
    print("2. Display data")
    print("3. Insert item at a location")
    print("4. Addition of all integer values in the list")
    print("5. Search an numeric value in the list")
    print("6. Exit")

    choice: int = int(input("Enter your choice: "))

    if choice == 1:
        item: str = input("Enter data to add: ")
        data_list.append(item)                  # Item added to the end of the list              
        print("Data added successfully.")

    elif choice == 2:
        if len(data_list) == 0:                 # Consider no item in the list but user want to display data, so how do we know if the list has element or not
            print("List is empty.")             # calculate the len()
        else:
            print("Current List:", data_list)
            # for item in data_list:
            #     print(item)
            # for item in range(0, len(data_list)):
            #     print(f"Index {item}: {data_list[item]}")   # Displaying the index and the item in the list

    elif choice == 3:
        if len(data_list) == 0:
            print("List is empty. Add data first.")
        else:
            item = input("Enter item to insert: ")
            pos = int(input("Enter position (index starts from 0): "))
            
            if pos >= 0 and pos <= len(data_list):
                data_list.insert(pos, item)
                print("Item inserted successfully.")
            else:
                print("Invalid position.")

    elif choice == 4:
        if len(data_list) == 0:
            print("List is empty. Add data first.")
        else:
            total = 0
            for item in data_list:
                if item.isdigit():
                    total += int(item)
                else:
                    print(f"The type of {item} is:", type(item))
            print("The sum of all integer values in the list is:", total)

    elif choice == 5:
        if len(data_list) == 0:
            print("List is empty. Add data first.")
        else:
            search_item = float(input("Enter the numeric value to search: "))
            num_list = []
            for item in data_list:
                try:
                    num = float(item)
                    if num.is_integer():
                        num_list.append(int(num))
                    else:
                        num_list.append(num)
                except ValueError:
                    pass

            if len(num_list) == 0:
                print('No number found')
                break

            if search_item in num_list:
                print(f"Exact match found: {int(search_item) if search_item.is_integer() else search_item}")
            else:
                upper = search_item + 5
                found = False

                for num in num_list:
                    if num > search_item and num <= upper:
                        print(f"Number within +5 range: {num}")
                        found = True

                if not found:
                    print("No match found")
            # for item in data_list:
            #     if int(item) == search_item:
            #         print(f"{search_item} found in the list.")
            #     else:
            #         print(f"{search_item} not found in the list.")
    elif choice == 6:
        print("Exiting program...")
        break   # Exit infinite loop

    else:
        print("Invalid choice. Try again.")

    cont: int = int(input("\nPress 1 to continue: "))
    if cont != 1:
        print("Program terminated.")
        break