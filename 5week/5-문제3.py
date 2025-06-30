val_1=int(input("첫 번째 정수를 입력 : "))
val_2=int(input("두 번째 정수를 입력 : "))
val_3=int(input("세 번째 정수를 입력 : "))

result = val_1 + val_2 + val_3
avg = result/3

print('총 합 : %6d' % result)
print('평 균 : %7.2f' % avg)