import random as r

userwin=0
comwin=0

for k in range(3):
    com = r.randrange(2)
    use = int(input('\n홀 0, 짝 1 입력: '))
    
    if com == use:
        print("사용자 승")
        userwin = userwin+1
    else:
        print("컴퓨터 승")
        comwin = comwin+1

print("\nuserwin = ", userwin, "comwin = ", comwin)