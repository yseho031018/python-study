# 연습문제 9번
# circle()로 원을 그릴 수 있다 배운 내용을 토대로 오륜기를 그려보자 색상 : 파노검초빨
import turtle as t
t.shape("turtle")
t.speed(0)

# 시작위치 변경
t.up()
t.goto(-150, 80)
t.down()

t.width(5)

# 파란색 원
t.color("blue")
t.circle(50)

# 위치 변경
t.up()
t.goto(-100, 30)
t.down()
# 노란색 원
t.color("yellow")
t.circle(50)

# 위치 변경
t.up()
t.goto(-40, 80)
t.down()
# 검정색 원
t.color("black")
t.circle(50)

# 위치 변경
t.up()
t.goto(20, 30)
t.down()
# 초록색 원
t.color("green")
t.circle(50)

# 위치 변경
t.up()
t.goto(80, 80)
t.down()
# 빨간색 원
t.color("red")
t.circle(50)

t.done()