# 사용자에게 두개의 정수를 입력받아 변수로 저장
# 두개 정수의 합, 차, 곱, 나누기, 몫, 나머지 산술 결과값을
# 화면에 출력하기

num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력(첫번째 값보다 작은값) : "))

print("-----------결과값--------------")
print("합 :", num1 + num2)
print("차 :", num1 - num2)
print("곱 :", num1 * num2)
print(f"나누기 : {num1 / num2:.2f}")
print(f"몫 : {num1 // num2:.2f}")
print(f"나머지 : {num1 % num2:.2f}")



