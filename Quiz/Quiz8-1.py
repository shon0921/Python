for a in range(1,51):
    file = open("{0}주차.txt".format(a), "w", encoding="utf-8")
    file.write("- X 주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :")
    file.close()