""" r = []
c = []
n=int(input("Enter Loop Sequance:"))
#answer=False

for x in range(n):
    A = int(input("enter value a:"))
    B = int(input("enter value b:"))
    r.append(A)
    c.append(B)

print(r,c)

t=set(r)
y=set(c)

d=t.intersection(y)
print(list(d))


set(A)
set(B)

list(A)
list(B)
# print("Is matching member ?",answer)

A=set()
B=set()
print(A.intersection(B))
   """
n=str(658)
n1=str(245)
n2=str(258)

for i in n:
    if i in n1 and n2:
        print(i,"is a common number")