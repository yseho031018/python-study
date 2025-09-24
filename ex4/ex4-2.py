# 3개 종류 커피 단가 입력받기
americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input("아메리카노 판매 개수 : "))
cafelattes = int(input("카페라떼 판매 개수 : "))
capucinos = int(input("카푸치노 판매 개수 : "))

# 종류에 상관없이 1잔의 커피 재료비 1000원으로 가정해서 총재료비 계산
material_cost = 1000 # 재료비
coffee_num = americanos + cafelattes + capucinos # 주문한 커피 개수
total_cost = americano_price + cafelatte_price + capucino_price # 총매출액
total_material = material_cost * coffee_num # 총 재료비
net_profit = total_cost - total_material

# 화면에 총매출액, 총재료비 순수익 출력하기
print("총매출액 : ", total_cost)
print("총재료비 : ", total_material)
print("순수익 : ", net_profit)