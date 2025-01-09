python = "Python is Amazing"
print(python.lower()) # 소문자로 변환
print(python.upper()) # 대문자로 변환
print(python[0].isupper())  # 첫 글자가 대문자인지 ture
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) # 해당 문자 변경

index = python.index("n") # 해당 문자가 어디 있는지 확인
print(index)
index = python.index("n",index + 1)  # 시작 위치 설정하고 자르기
print(index)

print(python.find("Java")) # 똑같이 찾기 (없으면 -1)
# print(python.index("Java")) # 찾기 (없으면 에러)

print("hi")
print(python.count("n")) # 몇번 나오는지 계산