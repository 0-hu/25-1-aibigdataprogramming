# 주사위 2개를 던졌을 때, 합이 6이 되는 경우 전부 출력

for a in range(1, 7):
    for b in range(1, 7):
        if a + b == 6 :
            print(f"첫 번째 주사위={a} 두 번째 주사위={b}")