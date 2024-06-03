

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name , pwd = data.split('|')
            print("name: " + name + " , password: " ,pwd)

def add():
    name = input("Enter Account Name : ")
    password = input("Password : ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + password + "\n")


while True:
    #user get to decide if he/she wants to add or view or quit
    mode = input("Would you like to create a new passowrd or viwe the existing password (view / add) or q to quit ? ").lower()

    #condition if user chooses to quit 
    if mode == 'q':
        break

    # condition if user chooses to view the existing password
    if mode == 'view':
        view()

    #condition if user choose to add new password
    elif mode == 'add':
        add()