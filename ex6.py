# 연습문제 6번
# 터틀 그래픽에서 color() 함수를 호출하면 거북이가 그리는 선의 색상을 변경할 수 있다.
import turtle as t
t.shape("turtle")

# 시작위치 변경
t.up()
t.goto(-50, 0)
t.down()

# 선 색상을 blue로 변경
t.color("blue")

# 모양 그리기
t.fd(100)

t.done()