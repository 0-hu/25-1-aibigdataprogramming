#가위바위보 게임
import random

def checkState(number):
    if number == 0:
        return '가위'
    elif number == 1:
        return '바위'
    elif number == 2:
        return '보'

com = random.randrange(3)
user = int(input('가위0 바위1 보2 선택: '))

userData = checkState(user)
comData = checkState(com)
print(f'user = {userData}, com = {comData}')

if user == com:
    print('비겼습니다!')
elif (com+1) % 3 == user:
# elif (com-user + 1) % 3 == 0:
    print('user 승!')
else:
    print('com 승!')