import getpass as gp
def Create():
    print("Please select the type of user you want to create :\n1 : Normal User\n2 : Admin User\n")
    choice = int(input("Enter your choice : "))
    if(choice==1):
        print("\nTo continue, Please enter required details.")
        userName = input("UserName : ")
        email = input("Mail ID : ")
        password = gp.getpass("Password : ")
        with open("D:/Codes/Python/Data/UserName.txt","r") as u1, open("D:\Codes\Python\Data\Email.txt","r") as e1, open("D:\Codes\Python\Data\Password.txt","r") as p1:
            users = list(u1.readlines())
            emails = list(e1.readlines())
            passwords = list(p1.readlines())
            if((userName+'\n' in users) and (email+'\n' in emails) and (password+'\n' in passwords)):
                print("User Already exists, Try with different details or Login using the same.")
            else:
                u1.close()
                p1.close()
                e1.close()
                with open("D:/Codes/Python/Data/UserName.txt","a") as u1, open("D:\Codes\Python\Data\Email.txt","a") as e1, open("D:\Codes\Python\Data\Password.txt","a") as p1:
                    u1.write(userName+'\n')
                    p1.write(password+'\n')
                    e1.write(email+'\n')
                print("Login Credentials Registered, Thank You.")
        
    elif(choice==2):
        print("\nTo continue, Please enter Super-Admin Credentials : ")
        userName = input("\nSuper-Admin UserName : ")
        password = gp.getpass("Super-Admin Password : ")
        if(userName=="admin" and password=="Cooler Master"):
            print("\nSuper-Admin Verified, Now enter the account details")
            userName = input("\nEnter Admin UserName : ")
            password = gp.getpass("Enter Admin Password : ")
            password1 = gp.getpass("Enter Admin Password again : ")
            if(password==password1):
                with open("D:/Codes/Python/Data/adminUserName.txt","r") as u1, open("D:/Codes/Python/Data/adminPassword.txt","r") as p1:
                    users = list(u1.readlines())
                    passwords = list(p1.readlines())
                    if((userName+'\n' in users) and (password+'\n' in passwords)):
                        print("Admin account already exists.")
                    else:
                        u1.close()
                        p1.close()
                        with open("D:/Codes/Python/Data/adminUserName.txt","a") as u1, open("D:/Codes/Python/Data/adminPassword.txt","a") as p1:
                            u1.write(userName+"\n")
                            p1.write(password+"\n")
                        print("\nAdmin user created.")
            else:
                print("\nPasswords Mismatch")
        else:
            print("Super-Admin not verified.")

def Login():
    print("To Continue, Please enter,")
    userName = input("UserName : ")
    password = gp.getpass("Password : ")
    with open("D:/Codes/Python/Data/UserName.txt") as u1, open("D:\Codes\Python\Data\Password.txt") as p1:
        users = list(u1.readlines())
        keys = list(p1.readlines())
        if(userName+"\n" in users):
            if(password+"\n" in keys):
                print("Welcome Back ",userName)
                print()
            else:
                print("Incorrect Password, Please Try Again.\n")
        else:
            print("Credentials mismatch\n")

def Admin():
    print("\nTo Continue, PLease Login with admin credentials.")
    userName = input("Enter UserName : ")
    password  = gp.getpass("Enter Password : ")
    with open("D:/Codes/Python/Data/adminUserName.txt","r") as u1, open("D:/Codes/Python/Data/adminPassword.txt","r") as p1:
        users = list(u1.readlines())
        passwords = list(p1.readlines())
        if((userName+'\n' in users) and (password+'\n' in passwords)):
            print("\nWelcome "+userName+",")
            while(True):
                print("Select one\n1 : View and Find Accounts\n2 : Modify Data")
                choice = int(input("Enter your choice : "))
                if(choice == 1):
                    while(True):
                        print("What would u like to do ?\n1 : View Accounts\n2 : Find User\n3 : View Admin Accounts\n4 : Find Admin Usern\n5 : Go Back")
                        with open("D:/Codes/Python/Data/UserName.txt","r") as u1, open("D:/Codes/Python/Data/Password.txt","r") as p1:
                            with open("D:/Codes/Python/Data/adminUserName.txt","r") as au1, open("D:/Codes/Python/Data/adminPassword.txt","r") as ap1:
                                users = list(u1.readlines())
                                passwords = list(p1.readlines())
                                adminUsers = list(au1.readlines())
                                adminPasswords = list(ap1.readlines())
                                choice = int(input("\nEnter your choice : "))
                                if(choice == 1):
                                    print(str(len(users))+" users recorded")
                                    for i,j in zip(users,passwords):
                                        print(i[:len(i)-1],j[:len(j)-1])
                                    print()
                                elif(choice == 2):
                                    find = input("Enter the UserName to be found : ")
                                    if(find+'\n' in users):
                                        print("\nUser Exists.\n")
                                    else:
                                        print("User not Registered.")
                                elif(choice == 3):
                                    print(str(len(users))+" users recorded")
                                    for i,j in zip(adminUsers,adminPasswords):
                                        print(i[:len(i)-1],j[:len(j)-1])
                                    print()
                                elif(choice == 4):
                                    find = input("Enter the Admin UserName to be found : ")
                                    if(find+'\n' in adminUsers):
                                        print("\nAdmin Exists.\n")
                                    else:
                                        print("Admin not Registered.")
                                elif(choice == 5):
                                    print("Exited.")
                                    break
                elif(choice == 2):
                    pass
        else:
            print("Admin Not Registered.")

def SuperAdmin():
    userName = input("Admin UserName : ")
    password = gp.getpass("Admin Password : ")
    if(userName=="admin" and password=="Cooler Master"):
        print("\nKudos Sir, Welcome Back\n")
        with open("D:/Codes/Python/Data/UserName.txt") as u1, open("D:\Codes\Python\Data\Password.txt") as p1:
            users = list(u1.readlines())
            keys = list(p1.readlines())
            print(users,keys)
            for i,j in zip(users,keys):
                print(i[:len(i)-1],j[:len(j)-1])
            print()
    else:
        print("Incorrect Credentials, You don't have access to this page")

#DRIVER CODE
print("Welcome to Login Portal, Please select the below options \n1 : New User\n2 : Existing User\n3 : Admin Controls\n4 : Super-Admin Controls\n5 : Exit")
while(True):
    choice = int(input("\nEnter the Choice : "))
    if(choice == 1):
        Create()
    elif(choice == 2):
        Login()
    elif(choice == 3):
        Admin()
    elif(choice == 4):
        SuperAdmin()
    elif(choice == 5):
        print("Thank You.")
        break
    print("\nWhat next ?\n1 : New User\n2 : Existing User\n3 : Admin Controls\n4 : Super-Admin Controls\n5 : Exit")