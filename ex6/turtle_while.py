# for문을 활용하여 입력받은 다각형 그리기
import turtle as t

t.shape("turtle")



answer = "yes"

while True:

    n = int(t.textinput("", "3~6까지 숫자를 입력하세요."))

    if answer == "no":
        break

    if 3 <= n <= 6:
        for _ in range(n):
            t.forward(100)
            t.left(360 / n)
    else:
        t.write("잘못된 입력입니다.")

    answer = t.textinput("", "계속?(yes,no)")

    t.clear()

t.done()