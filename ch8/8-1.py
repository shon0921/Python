import sys

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)    # 표준 에러로 처리

# 시험성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 8칸 띄고 왼쪽 정렬 , 4칸 띄고 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003. ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3의 크기 없는 공간 0으로 채우기

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.") # 문자열 형태로 저장되고 출력