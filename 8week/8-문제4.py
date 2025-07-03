# 임의의 정수를 입력받아 짝수인지 홀수인지를 판단하여 출력한다.

n=int(input())

if n % 2==0: # if n % 2 != 1:
    print("짝수")
else:
    print("홀수")