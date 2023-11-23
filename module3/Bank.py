


class bank:
    def bank_system():
        n=int(input("enter num of details"))
        a=input("enter name")
        b=int(input("enter account num:"))
        c=input("enter account type")
        if 'name'and 'accnum'and 'accttype'!='valid':
                print (f"{a}/{b}/{c}")
        elif a!=b and b!=c:
                print("invalid details")
        else:
                print("error")
    def deposit():
        n=int(input("enter deposit num"))
       
        if (len(n))>=deposit:
            print("the deposit num of")
        elif n==deposit:
            print("this is valid value")
        else:
            print("error")
def withdraw():
        n1=int(input("enter withdraw num"))
        print("withdraw")
        for i in range(n1):
            x1=int(input("enter value:"))
            print(i)
            if withdraw>=n1:
                print(f"{n1}")
            elif withdraw==n1:
                print("this valid num")
            else:
                print("error")
account=bank()
account.bank_system()
account.deposit()
account.withdraw()







