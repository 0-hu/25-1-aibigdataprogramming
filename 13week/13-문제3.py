#동일 원소의 위치 찾기
s=[7,8,8,7,5,6,8,9,8] # 원본 데이터

n=s.count(8)
L=[]; p=0
for _ in range(n):
    p=s.index(8,p)
    L.append(p)
    p+=1
print(L)
print(p)
