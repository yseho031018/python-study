# 0~9까지의 숫자를 이용하여서 간단한 산수 퀴즈를 출제하는 프로그램을 만들어봅시다.
import random

print("산술 퀴즈에 오신 것을 환영합니다. (종료는 !)\n")

# 연산자를 선택할 수 있는 리스트 생성
op_list = ["+", "-", "/", "*"]

# 문제는 특정 조건을 작동하지 않는다면 무한 생성
while True:
    # num1과 num2는 1부터 10까지 랜덤으로 값을 생성
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    # op는 먼저 만든 op_list 리스트에서 랜덤으로 하나를 가져옴
    op = random.choice(op_list)

    # 나누기를 대비해서 num1이 num2보다 작다면 서로 값을 바꾼다
    if num1 < num2:
        num1, num2 = num2, num1

    # 사용자의 값을 입력받고 종료할때를 대비하여 문자열로 입력받음
    user_input = input(f"{num1} {op} {num2} : ")

    # !를 입력하여 무한반복문 종료
    if user_input == "!":
        print("종료!")
        break

    # 계산을 위해 입력받은 값을 int로 변경
    result = int(user_input)

    # answer에 문제 정답을 구함
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "/":
        answer = num1 // num2
    elif op == "*":
        answer = num1 * num2

    # 입력받은 정답과 구한 정답이 같다면 정답 아니면 틀림
    if result == answer:
        print("정답!")
    else:
        print("틀림!")
