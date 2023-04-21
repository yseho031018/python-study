# Q1. 평균 점수 구하기
korean = 80
math = 75
english = 55

total_average = ((korean + math + english) / 3)
print("1. 총 평균은 : ",total_average)

# Q2. 홀수 짝수 판별
number = 13

if number % 2 == 0:
    print("2. 짝수 입니다!")
else:
    print("2. 홀수 입니다!")

# Q3. 주민등록번호 나누기
rrn = "881120-1068234"
print('3. 19{}년 {}월 {}일 뒷자리 : {}'.format(rrn[0:2], rrn[2:4] , rrn[4:6], rrn[7:14]))

# Q4. 주민등록번호 인덱싱
pin = "881120-1068234"
print("4. 성별을 나타내는 숫자 :",pin[7:8])

# Q5. 문자열 바꾸기
a = "a:b:c:d"
print("5. 변환 :",a.replace(":","#"))

# Q6. 리스트 역순 정렬하기
list = [1,3,5,4,2]
list.reverse()
print("6. 리스트 역순 :",list)

# Q7. 리스트를 문자열로 만들기
list2 = ['Life', 'is', 'too', 'short']
print("7. 문자열 :"," ".join(list2))

# Q8. 튜플 더하기
tuple = (1, 2, 3)
print("8. 튜플 더하기 : ",tuple + (4,))

# Q9. 딕셔너리의 키
a = dict()
# a[[1]] = 'python' 
# 리스트는 값이 변할 수 있기 때문에 Key로 쓸 수 없다.
print("9. 딕셔너리의 키 :",a)

# Q10. 딕셔너리 POP
a = {'A':90, 'B':80, 'C':70}
print("10. B에 해당되는 값 :",a.pop('B'))

# Q11. 리스트에서 중복 제거하기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

print("11. 중복 숫자 제거 :",set(a))

# Q12. 파이썬 변수
a = b = [1, 2, 3]
a[1] = 4
print("12. 파이썬 변수 :",b) # 두 개의 객체가 같기 때문에 a가 변하면 b도 변한다
