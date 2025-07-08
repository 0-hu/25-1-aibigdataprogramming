def one2hund():
    s, c = 0, 1
    while c <= 100:
        s+=c
        c+=1
    print(s)

def one2hund_2():
    s, c = 0, 0
    while c < 100:
        c +=1
        s +=c
    print(s)


one2hund()
one2hund_2()