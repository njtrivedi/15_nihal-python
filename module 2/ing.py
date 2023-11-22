word=(input("enter word:"))
def add_suffix(word):
    if(len(word))<3:
        result=word
    elif word[:-3]=='ing':
        result=word+"ly"
    else:
        print("error")
add_suffix(word)















'''n=int(input("enter num of str:"))
a=input("enter string:")
#a.split().count()
count=0
for i in range(n):
        print(i)
        if a>=count:
            print(f"{a} / {count}")
        else:
              print('error')'''



