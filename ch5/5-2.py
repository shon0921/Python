cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5])   #없으면 에러
# print(cabinet.get(5)) # 에러가 나지 없고 None으로 대체
print(cabinet.get(5, "사용 가능")) # 없으면 값 대체
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}  # 문자열 써도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 값 변경
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"] # 값 삭제
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 값 비우기
print(cabinet)