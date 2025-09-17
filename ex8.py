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



t.done()