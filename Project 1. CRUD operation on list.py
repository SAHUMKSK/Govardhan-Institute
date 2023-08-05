# Write a program to make crud operation on list.

listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "One", "Two", "Three", "Four", "Five"]

print("Here is the list:", listx)

print('''We have below functionalities.
1. Insert
2. Update
3. Delete
4. Display''')

choice = int(input("What to do you want?: "))

if (choice == 1):
    value = int(input("Enter the value you want to insert: "))
    listx.append(value)
    print("Given value has been inserted successfully.")
    
    print("Here is the updated list:", listx)
elif (choice == 2):
    update_index = int(input("Enter the index postion you want to update: "))
    if update_index >= 0 and update_index <= len(listx) - 1:
        
        
        update_value = input("Enter the value: ")
        
        #listx.insert(update_index, update_value)
        listx[update_index]=update_value
        #listx.pop(listx.index(update_index + 1))
        
        print("Here is the updated list:", listx)

    else:
        print("You have entered invalid index postion.")

elif (choice == 3):
    delete_index = int(input("Enter the index value:"))
    if delete_index >= 0 and delete_index <= len(listx):
        listx.pop(delete_index)
        print("Given index position has been removed.")
        print("Here is the updated list:", listx)

    else:
        print("Entered index postion is not exist.")
        
    
        
elif(choice == 4):
    print("Here is the list value: ", listx)
else:
    print("You have entered invalid choice.")