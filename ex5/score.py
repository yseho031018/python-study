# 90이상 A 80이상 B 70이상 C 60이상 D 그외 F
score = int(input("점수 : "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")