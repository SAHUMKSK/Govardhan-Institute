# New Project

admin_credentials = [{'admin_username': 'MUKESH', 'admin_password': '123456'}]
front_end_credentials = [{'front_end_username': 'MUKESH', 'front_end_password': '123456'}]


questions = [
{'que': 'What is the formula of Oxygen?', 'ans': ['O', 'X', 'OX', 'None from above', 'O']},
{'que': 'What is the formula of Carbon?', 'ans': ['Ca', 'N', 'C', 'None from above', 'O']}
]

update_flag = True
delete_flag = True


while(True):
    
    print('''We have the below options: 
    1. Admin
    2. Front-End User
    0. Exit
    ''')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        
        while(True):

            print('''We have the below options:
            1. Registration
            2. Login
            0. Exit
            ''')
            
            admin_choice = int(input("What do you want: "))
            if admin_choice == 1:
                
                admin_credential = {}
                print("Enter below details(Registration):")
                
                admin_credential["admin_username"] = input("Enter your username: ")
                admin_credential["admin_password"] = input("Enter your password: ")
                
                print("You have successfully registered.")
                
                admin_credentials.append(admin_credential)
                
                print(admin_credential)
                print(admin_credentials)
            elif admin_choice == 2:
        
                print("Enter your credential(Login): ")
                
                check_username = input("Enter your username: ")
                check_password = input("Enter your password: ")
                for uap in admin_credentials:
                    if (check_username == uap["admin_username"] and check_password == uap["admin_password"]):
                        print("\nYou have successfully logged in.")
                        while(True):
                            print('''\nWe have the below options:
                            1. Insert
                            2. Update
                            3. Delete
                            4. View
                            0. Exit
                            ''')
                            task = int(input("Enter your choice: "))
                            if task == 1:
                                
                                question = {} # Created the new dictionary to store the questions with it's answer along with options.
                                
                                que = input("Enter the question: ")
                                q_op1 = input("Enter 1st option: ")
                                q_op2 = input("Enter 2nd option: ")
                                q_op3 = input("Enter 3rd option: ")
                                q_op4 = input("Enter 4th option: ")
                                
                                
                                if (q_op1 == q_op2) or (q_op1 == q_op3) or (q_op1 == q_op4) or (q_op2 == q_op3) or (q_op2 == q_op4) or (q_op3 == q_op4):
                                
                                    print("You have entered same option twice or multiple times.")
                                
                                else:
                                    q_options = []
                                    
                                    q_ans = input("Enter the correct option: ")
                                    
                                    q_options.append(q1_op1)
                                    q_options.append(q1_op2)
                                    q_options.append(q1_op3)
                                    q_options.append(q1_op4)
                                    
                                    if q_ans not in q_options:
                                        
                                        print("Previously you have not entered the correct options.")
                                    
                                    else:
                                        q_options.append(q_ans)
                                        
                                        print(q_options)
                                        
                                        question["que"] = que
                                        
                                        question["ans"] = q_options
                                        
                                        
                                        
                                        questions.append(question)
                                        
                                        print("A new question has been enetered successfully.")
                                        
                                        print(questions)
                                        
                                        
                                        
                            elif task == 2:
                                
                                check_question = input("Enter the question you want to update: ")
                                
                                for queandans in questions:
                                    
                                    if check_question == queandans["que"]:
                                        
                                        update_flag = False
                                        
                                        print("Enetred question has been found.")
                                    
                                        update_question = input("Enter the new question you want to update: ")
                                        q1_op1 = input("Enter 1st option: ")
                                        q1_op2 = input("Enter 2nd option: ")
                                        q1_op3 = input("Enter 3rd option: ")
                                        q1_op4 = input("Enter 4th option: ")
                                        
                                        if (q1_op1 == q1_op2) or (q1_op1 == q1_op3) or (q1_op1 == q1_op4) or (q1_op2 == q1_op3) or (q1_op2 == q1_op4) or (q1_op3 == q1_op4):
                                
                                            print("You have entered same option twice or multiple times.")
                                        else:
                                
                                        
                                        
                                            q1_options = []
                                        
                                            q1_ans = input("Enter the correct option: ")
                                        
                                            q1_options.append(q1_op1)
                                            q1_options.append(q1_op2)
                                            q1_options.append(q1_op3)
                                            q1_options.append(q1_op4)
                                            
                                            if q1_ans not in q1_options:
                                                print("Previously you have not enetred the correct option.")
                                            else:
                                                q1_options.append(q1_ans)
                                                
                                                queandans["que"] = update_question
                                                queandans["ans"] = q1_options
                                        
                                                print("Question has been updated successfully.")
                                                print("Question:", queandans["que"])
                                                print("Options are:", queandans["ans"])
                                        
                                        
                                        
                        
                                if (update_flag == True):
                                    print("Enetred question does not exist.")
                        
                                        
                                        
                                    
                            elif task == 3:
                                
                                delete_question = input("Enter question you want to delete: ")
                                
                                for queandans in questions:
                                    
                                    if delete_question == queandans["que"]:
                                        
                                        delete_flag = False
                                        
                                        print("Enetred question has been found.")
                                        
                                        
                                if (delete_flag == True):
                                    print("Enetred question does not exist.")
                                    
                                    
                                    
                                    
                            elif task == 4:
                                
                                if questions == []:
                                    print("\nAny of the questions are not present.")
                                else:
                                    
                                    print("\nHere are the questions: ")
                                    
                                    
                                    n = 0
                                    for queandans in questions:
                                    
                                        n = n + 1
                                        print("\nQuestion #", n, ":", queandans["que"])
                                        x = 0
                                        for i in range(len(queandans["ans"])- 1):
                                            x = x + 1
                                            print("Option ",x, ": ",queandans["ans"][i], sep = "")
                                        
                                        
                                        
                                        
                            elif task == 0:
                                break
                            else:
                                print("You have entered invalid input.")

                    else:
                        print("Username and password are incorrect.")

            elif admin_choice == 0:
            
                break
            
            else:
                print("You have entered wrong choice.")
                
                    
    
    elif choice == 2:
        while(True):
            print('''We have the below options:
            1. Registration
            2. Login
            0. Exit
            ''')
        
            front_end_choice = int(input("What do you want: "))
            
            if front_end_choice == 1:
            
                front_end_credential = {}
                
                print("Enter below details(Registration):")
                
                front_end_credential["front_end_username"] = input("Enter your username: ")
                front_end_credential["front_end_password"] = input("Enter your password: ")
                
                front_end_credentials.append(front_end_credential)
                
                print("You have successfully registered your user.")
                
                print(front_end_credential)
                print(front_end_credentials)

                
            elif front_end_choice == 2:
                
                check_username = input("Enter your username: ")
                check_password = input("Enter your password: ")
                
                for uap in front_end_credentials:
                    
                    if (check_username == uap["front_end_username"] and check_password == uap["front_end_password"]):
                        print("You have successfully logged in.\n")
                        
                        print(front_end_credentials)
                        
                        while(True):
                        
                            print('''We have the below options.
                            1. Insert
                            2. Update
                            3. Delete
                            4. View
                            5. Exit
                            ''')
                            
                            task = int(input("Enter your choice: "))
                            
                            if task == 1:
                                pass
                                
                            elif task == 2:
                                
                                pass
                            
                            elif task == 3:
                                
                                pass
                            
                            elif task == 4:
                                
                                pass
                            
                            elif task == 5:
                                
                                break
                            
                            else:
                                ("You have entered wrong choice.")
                            
                    else:
                        print("You have entered wrong username and password.")
                            
            elif front_end_choice == 3:
        
                break
        
            else:
            
                print("You have entered wrong choice.")
            
    elif choice == 0:
    
        break
        
        
    else:
        print("You have entered wrong choice.")