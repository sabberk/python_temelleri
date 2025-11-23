from db_class import MySQLDatabase

db=MySQLDatabase("oython")
db.connection()
while True:
    print("\n User Management System")
    print("1. Register")
    print("2. Login")
    print("3. List Users")
    print("4. Update User")
    print("5. Delete User")
    print("6. Exit")
    choice=int(input("Select an option (1-5):"))
    if (choice==1):
        username= input("Enter a username: ")
        password= input("Enter a password: ")
        name= input("Enter a name: ")
        lastname= input("Enter a lastname: ")
        age= int(input("Enter age= "))
        hashed_password = db.hash_password(password)
        values = {
            "username": username,
            "password_hash": hashed_password,
            "user_name": name,
            "user_lastname": lastname,
            "user_age":age,
            "user_active":1
        }
        db.insert_record("users",values)

    elif(choice==2):
        username = input("Enter username: ")
        password = input("Enter password: ")   
        result = db.getRow("SELECT * FROM users WHERE username=%s AND user_active=1",(username,))     
        if result is None:
            print("User not found!")  

        stored_hash = result[6]   

        if db.check_password(password,stored_hash):
            print("Login succesful!")
        else:
            print("Wrong password!")     

    elif(choice==3):
        user_id=int(input("Enter the id number you want to update:"))
        name_update=input("Enter a name:")
        lastname_update=input("Enter a lastname:")
        age_update=int(input("Enter an age:"))
        columns={"user_name":name_update,"user_lastname":lastname_update,"user_age":age_update}
        conditions={"id":user_id}
        db.update("users",columns,conditions)
    elif(choice==4):
        user_id=int(input("Enter the id number you want to delete:"))
        columns={"user_active":0}
        conditions={"id":user_id}
        db.update("users",columns,conditions)
    elif(choice==5):
        print("Exiting...Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5\n")



db.disconnect()








                

