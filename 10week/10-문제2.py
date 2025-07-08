배송지=input("(현재는 korea와 us만 가능):")
가격=int(input("상품의가격:"))

if 배송지 == "us":
    if 가격 >= 100000:
        # print("배송비 = 0")
        shipping_cost = 0
    else:
        # print("배송비 = 8000")
        shipping_cost = 8000
elif 배송지 == "korea":
    if 가격 >= 20000:
        # print("배송비 = 0")
        shipping_cost = 0
    else:
        # print("배송비 = 3000")
        shipping_cost = 3000
else:
    print("잘못된 국가 코드 입력입니다.")

print("배송비 =", shipping_cost)