accounts=[]
cur=''
def deposit(cur):
    ind=0
    for i in range(len(accounts)):
        if accounts[i][0] == cur:
            ind=i
            break
    depo = int(input("how much money do you want to deposit?: "))
    if depo<0:
        loggedin(cur)
        return
    accounts[ind][2] += depo
    loggedin(cur)

def withdraw(cur):
    ind=0
    for i in range(len(accounts)):
        if accounts[i][0] == cur:
            ind=i
            break
    withdrawal = int(input("how much money do you want to withdraw? "))
    if(accounts[ind][2]<withdrawal):
        print("\ninsufficient funds")
        loggedin(cur)
        return
    accounts[ind][2] -= withdrawal
    loggedin(cur)

def checkbal(cur):
    ind=0
    for i in range(len(accounts)):
        if accounts[i][0] == cur:
            ind=i
            break
    print(f"\nYour balance is {accounts[ind][2]}")
    loggedin(cur)

def transaction(cur):
    dest = input("Enter name of the depositer: ")
    amt = int(input("How much do you want to deposit? "))
    ind=-1
    for i in range(len(accounts)):
        if accounts[i][0] == cur:
            ind=i
            break
    ind1=-1
    for i in range(len(accounts)):
        if accounts[i][0] == dest:
            ind1=i
            break
    if ind==-1:
        print("User not found")
        loggedin(cur)
        return
    if(accounts[ind][2]<amt):
        print("insufficient funds")
        loggedin(cur)
        return
    print("\nTransaction succesful")
    accounts[ind][2]-=amt
    accounts[ind1][2]+=amt
    loggedin(cur)

def loggedin(cur):
    print(f"Hello, {cur}")
    print("0) logout")
    print("1) deposit")
    print("2) withdraw")
    print("3) check balance")
    print("4) transitulobis kanoni")
    oper = input()
    if oper == '0':
        unregistered()
        return
    elif oper == '1':
        deposit(cur)
        loggedin(cur)
        return
    elif oper == '2':
        withdraw(cur)
        loggedin(cur)
        return
    elif oper == '3':
        checkbal(cur)
        loggedin(cur)
        return
    elif oper == '4':
        transaction(cur)
        loggedin(cur)
        return

def register():
    print("0) return")
    print("1) register")
    oper = input()
    if oper == '0':
        unregistered()
        return
    if oper == '1':
        flag = True
        name = input("Enter username: ")
        password = input("Enter password: ")
        confirm = input("Confirm password: ")
        for i in accounts:
            if i[0] == name:
                print("username taken")
                register()
                return
        if password != confirm:
            print("Passwords do not match\n")
            register()
            return
        print("\nSuccesfully registered")
        accounts.append([name,password,0])
        # print(accounts)
        unregistered()
    else:
        print("Wrong operation")
        register()

def login():
    print("0) return")
    print("1) login")
    oper = input()
    if oper == '0':
        unregistered()
        return
    if oper == '1':
        name = input("Enter username: ")
        password = input("Enter password: ")
        for i in accounts:
            if i[0] == name and i[1] == password:
                print("\nSuccesful login")
                cur=name
                loggedin(cur)
                return
            if i[0] == name and i[1] != password:
                print("\nWrong password")
                login()
                return  
        print("\nUsername not found")
        login()       
    else:
        print("\nWrong operation")
        login()
        
def unregistered():
    print("Choose operation")
    print("1) register")
    print("2) login")
    print("3) quit")
    operation = input()
    print('\n')
    if operation == '1':
        register()
    elif operation == '2':
        login()
    elif operation == '3':
        return
    else:
        print("\nWrong operation")
        unregistered()

unregistered()