# Q1. 조건문의 참과 거짓
a = "Life is too short, you need python"

if "wife" in a: # 거짓
    print("wife") 
elif "python" in a and "you" not in a: # 거짓
    print("python")
elif "shirt" not in a: # 참이 나와 전체 조건문을 빠져나옴
    print("1. shirt")
elif "need" in a: # 참이지만 위에 결과에 참이 나와 실행 안됨
    print("need")
else: # 참이지만 위에 결과에 참이 나와 실행 안됨
    print("none")

# Q2. 3 의 배수의 합
i = 0
num = 0
while i < 1000:
    i += 1
    if i % 3 == 0:
        num += i     
    
print("2. 3의 배수의 합 :",num)

# Q3. 별 표시하기
star = 0
print("3. 별표시하기 :")
while star < 5:
    star += 1
    print(star * "*")

# Q4. 1 부터 100 까지 출력
print("4. 1부터 100까지 :")
for i in range(1, 101):
    print("{:d}".format(i), end=' ')
print()
# Q5. 평균점수 구하기
point = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]   
total = 0
for i in point:
    total = total + i

print("5. A 학급의 평균점수 :",total / len(point))

# Q6. 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print("6. 리스트 컴프리헨션 :",result)