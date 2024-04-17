import hashlib
import getpass

password_maanger = {}
#dictionary

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter the password: ")
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    #hexadecimal string 32 byte(256bits)
    password_maanger[username]= hashed_password
    print("Account Created Sucessfully")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password:" )
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    if username in password_maanger.keys() and password_maanger[username]== hashed_password:
        print("Login Sucessfull!")
    else:
        print("Login was unsucessfull")
        print("Invalid Username or Password")

def main():
    while True:
        choice = print("Enter the choice you want to select , 1->Create Account , 2->Login , 0->Break :")   
        if choice == '1':
            create_account() 
        elif choice == '2':
            login()
        elif choice == '0':
            break
        else:
            print("Invalid Choice.")

if __name__  == "__main__":
    main()

    


