a=(input("enter key"))
dict={"id=1,name=abc"}
if a in dict.keys():
    print(f"'key'{a}/{dict}")
    print(dict(a))
else:
    print("error")