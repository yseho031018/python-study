# 사용자로부터 초를 입력받아 이를 시간, 분, 초로 변환하여 출력

# 사용자로부터 입력받기
input_sec = int(input("변환할 초를 입력하세요 : "))

# 시간 변환
original_input_sec = input_sec
hour = input_sec // (60*60)

min = input_sec // 60
sec = input_sec % 60

print("입력한", original_input_sec, "초는", hour, "시간", min, "분", sec, "초입니다.")

# 소스를 더블클릭해서 실행한 경우에 실행창이 자동으로 닫히는 것을 방지
input()