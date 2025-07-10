# 2에서 10까지의 정수 중 모든 소수를 출력하는 프로그램 작성

for x in range(2,11):
    isPrime=True
    for i in range(2,x//2+1):
        if x%i==0:
            isPrime=False
            break
    if isPrime:
        print(x)
