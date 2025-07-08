height=float(input('키를 입력하시오[cm]: '))
weight=float(input('몸무게를 입력하시오[kg]: '))
bmi=weight/(height/100)**2

if bmi >= 40:
    print(f"BMI={bmi}, 고도비만입니다.")
elif bmi >= 35:
    print(f"BMI={bmi}, 중등도비만입니다.")
elif bmi >= 30:
    print(f"BMI={bmi}, 경도비만입니다.")
elif bmi >= 25:
    print(f"BMI={bmi}, 과체중입니다.")
elif bmi >= 18.5:
    print(f"BMI={bmi}, 정상입니다.")
else:
    print(f"BMI={bmi}, 저체중입니다.")
