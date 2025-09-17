# 연습문제 5번
# 터틀 그래픽에서 width() 함수를 호출하면 거북이가 그리는 선의 두께를 두껍게 할수있다.
import turtle as t
t.shape("turtle")

# 시작위치 변경
t.up()
t.goto(-50, 0)
t.down()

# 선 굵기 10으로 변경
t.width(10)

# 모양 그리기
t.fd(100)
t.left(90)
t.fd(100)

t.done()