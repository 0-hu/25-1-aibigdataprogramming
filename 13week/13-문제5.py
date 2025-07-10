#1에서 20까지의 정수중 3또는 7의 배수가 아닌 수를 출력 예제
nums=[]
for x in range(1,21):
    if x%3==0 or x%7==0:
        continue
    nums.append(x)
print(nums)
