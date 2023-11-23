from collections import Counter
a={'a':11,'b':22,'c':33,'d':44}
b={'a':12,'b':23,'c':45,'d':56}

c= Counter(a) + Counter(b)

print(dict(c))