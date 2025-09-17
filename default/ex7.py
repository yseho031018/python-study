# 연습문제 7번
# shape() 함수를 사용하여 거북이 모양을 사각형, 삼각형, 원으로 변경할 수 있다
import turtle as t
t.shape("square")

# 시작위치 변경
t.up()
t.goto(-50, 0)
t.down()

# 모양 그리기
t.fd(100)

t.done()