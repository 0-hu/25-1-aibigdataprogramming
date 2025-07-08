#9부터 1까지 숫자를 줄이면서 홀수만 곱하는 코드

mul = 1
for k in range(9, 0, -2):
	print('%d ' % k, end = '')
	mul = mul * k
print('\nmul =', mul)