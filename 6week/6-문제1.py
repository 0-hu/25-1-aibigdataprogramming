#자리수 분리
val = int(input("세자리 정수를 입력하세요:"))

val_100 = val//100
val_10 = (val//10)%10
val_1 = val%10

print('백자리: ', val_100, '십자리: ', val_10,'일자리: ', val_1)