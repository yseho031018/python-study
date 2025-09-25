import time

# 1970년이후 올라온 초가 실수로 반환됨
fseconds = time.time()
total_sec = int(fseconds)

# 흘러온 초를 분으로 바꾸고, 현재 몇분인지 계산
total_min = total_sec // 60
minute = total_min % 60

# 흘러온 분을 시간으로 바꾸고, 현재 몇시인지 계산
total_hour = total_min // 60
hour = total_hour % 24

# 5. 형식에 맞춰 결과를 출력합니다.
print(f"현재시간(GMT) : {hour}시 {minute}분")