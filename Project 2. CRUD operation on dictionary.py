# Write a program to make crud operation on dictionary.

dictx = {"Name":"Mukesh Sahu", "Designation":"Quality Assurance", "Country":"India"}
print("\nHere is the original dictionary:", dictx)

while(True):
    print('''\nWe have the below options
        1. Insert
        2. Update
        3. Delete
        4. View
        5. Exit
    ''')
    
    flag = False
    
    
    choice = int(input("What do you want to do with this dictionary data structure: "))
    print()
    
    if choice == 1:
        key = input("Enter the key you want to add: ")
        if key in dictx.keys():
            print("Entered key is present in this dictionary.")
        else:
            value = input("Enter the value: ")
            dictx.update({key:value})
            print("A new key and value pair has been added successfully.")
            print("\nHere is the updated dictionary:", dictx)
        
    elif choice == 2:
        
        pass
        
    elif choice == 3:
    
        pass
    
    elif choice == 4:
        
        print('''We have the below options:
        1. To view the the only key value
        2. To view the whole
        ''')
        view_choice = int(input("What to you want to view: "))
        if view_choice == 1:
            key = input("Enter the key: ")
            print(key, ":", dictx.get(key))
        elif view_choice == 2:
            print("Here is the whole dictionary:", dictx)
        else:
            print("You have entered wrong choice.")
    
    elif choice == 5:
        
        break
        
    else:
        print("You have entered wrong input.")