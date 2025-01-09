jumin = "991202-1234567"
print("성별"+ jumin[7]) # 슬라이싱 해당 숫자만 출력
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (1까지)
print("월 : " +jumin[2:4])
print("일 : " +jumin[4:6])

print("생년월일 : " +jumin[:6]) # 시작은 0빼도됨
print("뒤 7자리 : " + jumin[7:]) # 끝도 빼도됨
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지