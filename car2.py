import turtle as t

t.shape("turtle")
t.color("black")

# 1. 가로 200, 세로 200 크기의 빨간색 집 몸통 그리기
t.penup()
t.goto(-100, -100)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()

t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)

t.end_fill()

# 2. 초록새 세모 지붕 만들기
t.penup()
t.goto(-100, 100)
t.pendown()

t.fillcolor("green")
t.begin_fill()

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.end_fill()


# 반지름 30 바퀴 그리기
t.penup()
t.goto(-50, -150)
t.pendown()

t.fillcolor("brown")
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(50, -150)
t.pendown()

t.begin_fill()
t.circle(25)
t.end_fill()


t.done()