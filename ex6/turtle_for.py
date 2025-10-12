# for문을 활용하여 입력받은 다각형 그리기
import turtle as t

t.shape("turtle")

n = int(t.textinput("", "3~6까지 숫자를 입력하세요."))

if 3 <= n <= 6:
    for _ in range(n):
        t.forward(100)
        t.left(360 / n)
else:
    t.write("잘못된 입력입니다.")

t.done()