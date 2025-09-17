# 연습문제 4번
# 터틀 그래픽에서 거북이를 이동시킬때에는 forward() left() right() 함수를 사용한다
import turtle as t
t.shape("turtle")

# 시작위치 변경
t.up()
t.goto(-150, 0)
t.down()

# 지그재그 선긋기
t.forward(100)
t.left(90)
t.fd(100)
t.right(90)
t.fd(100)
t.right(90)
t.fd(100)
t.left(90)
t.fd(100)

t.done()