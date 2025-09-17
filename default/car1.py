import turtle as t

t.shape("turtle")
t.color("black")

# 1. 가로 400, 세로 200 크기의 빨간색 자동차 몸통 그리기
t.penup()
t.goto(-200, -100)
t.pendown()

t.fillcolor("blue")
t.begin_fill()

t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)

t.end_fill()

# 2. 가로 200, 세로 100 크기의 노란색 자동차 뚜껑 그리기
t.up()
t.goto(-100, 100)
t.down()

t.fillcolor("yellow")
t.begin_fill()

t.fd(200)
t.left(90)
t.fd(100)
t.left(90)
t.fd(200)
t.left(90)
t.fd(100)
t.left(90)

t.end_fill()

# 3. 반지름 50의 검은색 타이어 두개 그리기
t.up()
t.goto(-100, -150)
t.down()

t.fillcolor("black")
t.begin_fill()
t.circle(50)

t.done()