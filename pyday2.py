def deposit():
    pass
def withdraw():
    pass
def check_balance():
    pass
def view_transaction():
    pass
def menu():
    print("[c]heck balance")
    print("[d]epoist")
    print("[w]ithdraw")
    print("[v]iew transections")
    print("change [p]in")

print("---------------welcome to the atm---------------")
acc_num = ionput("enter the pin:")

if acc_num in data and data[acc_num]['pin']==pin:
    print("login successful")
    while true:
        menu()
        ch = input("enter your choice:").lower()
        if ch=='d':
            check_balance(acc_num)
        elif ch=='d':
            deposit(acc_num)
        elif ch=='w':
            withdraw(acc_num)
        elif ch=='v':
            view_transactions(acc_num)
        elif ch=='p':
            change_pin(acc_num)
        elif ch=='e':
            print("--------------thankyou---------------")
            break
        else:
             print("enter the valid choice")

else:
    print("invalid login")
            
        
                            
