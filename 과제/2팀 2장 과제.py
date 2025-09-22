import turtle as t

# 자동차 크기 지정
size1 = int(input("자동차 몸체 x축길이 "))
size2 = int(input("자동차 몸체 y축길이 "))
size3 = int(input("자동차 창문 x축길이 "))
size4 = int(input("자동차 창문 y축길이 "))
size5 = int(input("자동차 바퀴 반지름 "))

# 자동차 색상 지정
color1 = input("자동차 몸체 색깔 ")
color2 = input("자동차 창문 색깔 ")
color3 = input("자동차 바퀴 색깔 ")

# 펜 위치 지정
t.penup()
t.goto(-size1/2, -size2/2)
t.pendown()

# 커서는 거북이 모양으로 색상은 검정색 두께는 1
t.shape("turtle")
t.color("black")
t.width(1)

# 색상은 지정한 변수로 함
t.fillcolor(color1)
t.begin_fill()

# 자동챠 몸통 그리기
t.forward(size1)
t.left(90)
t.forward(size2)
t.left(90)
t.forward(size1)
t.left(90)
t.forward(size2)
t.left(90)

t.end_fill()

# 펜 위치 변경
t.up()
t.goto(-size3/2, size2/2)
t.down()

# 색상은 지정한 변수로 함
t.fillcolor(color2)
t.begin_fill()

# 자동차 몸통 그리기
t.fd(size3)
t.left(90)
t.fd(size4)
t.left(90)
t.fd(size3)
t.left(90)
t.fd(size4)
t.left(90)

t.end_fill()

# 펜 위치 변경
t.up()
t.goto(-size1/4, -size2/2 - size5)
t.down()

# 자동차 바퀴 그리기
t.fillcolor(color3)
t.begin_fill()
t.circle(size5)
t.end_fill()

t.up()
t.goto(size1/4, -size2/2 - size5)
t.down()

t.fillcolor(color3)
t.begin_fill()
t.circle(size5)
t.end_fill()

# 만든 자동차를 지운후 사이즈를 1.5배 증가 시킴
t.clear()

size1 *= 1.5
size2 *= 1.5
size3 *= 1.5
size4 *= 1.5
size5 *= 1.5

# 펜 위치 지정
t.penup()
t.goto(-size1/2, -size2/2)
t.pendown()

# 커서는 거북이 모양으로 색상은 검정색 두께는 1
t.shape("turtle")
t.color("black")
t.width(1)

# 색상은 지정한 변수로 함
t.fillcolor(color1)
t.begin_fill()

# 자동챠 몸통 그리기
t.forward(size1)
t.left(90)
t.forward(size2)
t.left(90)
t.forward(size1)
t.left(90)
t.forward(size2)
t.left(90)

t.end_fill()

# 펜 위치 변경
t.up()
t.goto(-size3/2, size2/2)
t.down()

# 색상은 지정한 변수로 함
t.fillcolor(color2)
t.begin_fill()

# 자동차 몸통 그리기
t.fd(size3)
t.left(90)
t.fd(size4)
t.left(90)
t.fd(size3)
t.left(90)
t.fd(size4)
t.left(90)

t.end_fill()

# 펜 위치 변경
t.up()
t.goto(-size1/4, -size2/2 - size5)
t.down()

# 자동차 바퀴 그리기
t.fillcolor(color3)
t.begin_fill()
t.circle(size5)
t.end_fill()

t.up()
t.goto(size1/4, -size2/2 - size5)
t.down()

t.fillcolor(color3)
t.begin_fill()
t.circle(size5)
t.end_fill()

t.done()