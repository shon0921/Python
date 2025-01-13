score_file = open("score.txt", "w", encoding="utf-8")   # 파일 생성 (쓰기 용도) write
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 파일 닫기

score_file = open("score.txt", "a", encoding="utf-8") # append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8") # read
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="") # end 줄바꿈 안하기
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")