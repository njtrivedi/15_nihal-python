def add(a,b):
    print(a+b)

def sub(a,b):
        print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)
                
                
def select():
        print("+","-","*","/")
choice=(input("enter any choice"))
num1=int(input("enter any num"))
num2=int(input("enter any value"))

if choice=="+":
      add(num1,num2)
elif choice=="-":
      sub(num1,num2)
elif choice=="*":
    mul(num1,num2)
elif choice=="/":
      div(num1,num2)
      select()








'''def sum(a,b):
    print(f"{a}+{b}={a+b}")
    def sub(a,b):
        print(f"{a}-{b}={a-b}")
def mul():
    print(f"{a}*{b}={a*b}")'''
          
