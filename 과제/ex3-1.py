# 연습문제 1 : 수학에서 나타나는 수식을 파이썬의 수식 형태로 바꾸어보자
import math

# (a)
x = 10
a = x**4 - 9*x**3 + x**2
print(f"(a) {a}")

# (b)
r = 5
b = (4/3) * math.pi * r**3
print(f"(b) {b:.2f}")

# (c)
a = 1; b = -5; c = 6
d = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
print(f"(c) {d}")