# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주소"}
print(menu, type(menu))

menu = list(menu)       # 리스트로 변경
print(menu, type(menu))

menu = tuple(menu)      # 튜플로 변경
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))