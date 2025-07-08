# 입력 받은 점수가 90점 이상은 'A', 80점 이상은 'B' 70점 이상은 'C', 60이상은 'D' 그 이외는 모두 F

score = int(input())

print("이번 학기 점수: ", score)
print("등급: ", end='')

if score >= 90:
    print ("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
elif score >= 60:
    print ("D")
else:
    print("F")