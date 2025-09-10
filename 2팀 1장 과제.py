# 연습문제 4번
# 터틀 그래픽에서 거북이를 이동시킬때에는 forward() left() right() 함수를 사용한다
import turtle as t
t.shape("turtle")

# 시작위치 변경
t.up()
t.goto(-150, 0)
t.down()

# 지그재그 선긋기
t.fd(100)
t.left(90)
t.fd(100)
t.right(90)
t.fd(100)
t.right(90)
t.fd(100)
t.left(90)
t.fd(100)

t.clear()

# 연습문제 5번
# 터틀 그래픽에서 width() 함수를 호출하면 거북이가 그리는 선의 두께를 두껍게 할수있다.

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

t.clear()

# 연습문제 6번
# 터틀 그래픽에서 color() 함수를 호출하면 거북이가 그리는 선의 색상을 변경할 수 있다.
import turtle as t
t.shape("turtle")
t.width(1)

# 시작위치 변경
t.up()
t.goto(-50, 0)
t.down()

# 선 색상을 blue로 변경
t.color("blue")

# 모양 그리기
t.right(90)
t.fd(100)

t.clear()

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

t.clear()

# 연습문제 8번
# 거북이가 이동할 때 선이 그려지지 않게 하려면 t.up으로 팬을 들고 t.down()으로 팬을 내려놓을 수 있다.
import turtle as t
t.shape("turtle")

# 시작위치 변경
t.up()
t.goto(-50, -100)
t.down()

# 모양 그리기
t.fd(100)

# 팬 위치 이동
t.up()
t.goto(-50, 100)
t.down()

t.fd(100)



t.clear()

# 연습문제 9번
# circle()로 원을 그릴 수 있다 배운 내용을 토대로 오륜기를 그려보자 색상 : 파노검초빨
import turtle as t
t.shape("turtle")
t.speed(10)

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

t.clear()

# 실습문제 1번
# 자동차 그리기
import turtle as t
t.shape("turtle")

t.width(1)
t.color("black")

# 팬 위치 이동
t.up()
t.goto(-100, 0)
t.down()

# 자동차 뚜겅 그리기
t.fillcolor("yellow")
t.begin_fill()
t.fd(200)
t.left(90)
t.fd(100)
t.left(90)
t.fd(200)
t.left(90)
t.fd(100)
t.end_fill()

# 팬 위치 이동
t.up()
t.goto(-200, -200)
t.down()

# 자동차 몸통 사각형 그리기
t.left(90)
t.fillcolor("red")
t.begin_fill()
t.fd(400)
t.left(90)
t.fd(200)
t.left(90)
t.fd(400)
t.left(90)
t.fd(200)
t.end_fill()

# 팬 위치 이동
t.up()
t.goto(-100, -250)
t.down()

# 자동차 바퀴 그리기
t.left(90)
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(150, -200)
t.down()

# 자동차 바퀴 그리기
t.left(90)
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

t.done()

#실습문제 2번
#자동차 그릭 2
