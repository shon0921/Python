with open("study.txt", "w", encoding="utf-8") as study_file:    # 쓰기
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:    # 불러오기
    print(study_file.read())