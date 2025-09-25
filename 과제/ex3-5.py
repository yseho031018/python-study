# 연습문제 5 : 사용자로부터 두 개의 정수를 받아서 정수의 합, 정수의 차, 정수의 곱, 정수의 평균, 큰 수, 작은 수를 계산하여
# 화면에 출력하는 프로그램을 작성하라. 파이썬이 제공하는 내장 함수 max(x, y), min(x, y)을 사용해보자.

x = int(input("x: "))
y = int(input("y: "))

print(f"두수의 합: {x+y}")
print(f"두수의 차: {x-y}")
print(f"두수의 곱: {x*y}")
print(f"두수의 평균: {(x+y)/2:.1f}")
print(f"큰수: {max(x,y)}")
print(f"작은수: {min(x,y)}")

