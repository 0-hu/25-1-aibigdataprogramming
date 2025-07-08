#가위바위보 게임
import random

com = random.randrange(3)
user = int(input('가위0 바위1 보2 선택: '))
print(f'user = {user}, com = {com}')

if user == com:
    print('비겼습니다!')
elif (com+1) % 3 == user:
# elif (com-user + 1) % 3 == 0:
    print('user 승!')
else:
    print('com 승!')