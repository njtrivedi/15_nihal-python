a=list()
b=list()
def unique_element():
    for i in a:
        print(i)
        for i in b:
            print(i)
            if a==b:
                i.append(a)
                i.append(b)
                return a
            return b
            
                
print(f"[1,2,2,2,3,3,4,5]")
print(f"[1,1,2,2,2,3,4,5]")
unique_element()

