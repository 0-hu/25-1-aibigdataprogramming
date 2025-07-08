# x, y, z = map(int, input("3개의 정수를 입력하시오:").split())

num = input("3개의 정수를 입력하시오: ").split()
x,y,z = map(int, num)

if x > y: # x가 y보다 큰 분기
    if y > z : print(f'최대값 = {x}, 최소값 = {z}')
    elif x > z: print(f'최대값 = {x}, 최소값 = {y}')
    else : print(f'최대값 = {z}, 최소값 = {y}')
else: #y>x 이면서 y==x인 경우 분기
    if x > z : print(f'최대값 = {y}, 최소값 = {z}')
    elif y > z: print(f'최대값 = {y}, 최소값 = {y}')
    else : print(f'최대값 = {z}, 최소값 = {x}')


