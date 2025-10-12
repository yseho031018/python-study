# 사용자에게 3 ~ 6 중 숫자를 입력받아 해당 다각형을 그리기
import turtle as t
t.shape("turtle")

n = int(t.textinput("","3~6까지 숫자를 입력하세요."))
angle = 360 / n

if n == 3:
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
elif n == 4:
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
elif n == 5:
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
else:
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
t.done()

t.done()