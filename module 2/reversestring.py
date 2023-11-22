def reverse():
    str=input("enter string:")

    for i in str:
        print(i)
        if str%13==0:
            result=(f"{str}")
        elif str==1:
            result=str
        else:
            print("error")
reverse()
