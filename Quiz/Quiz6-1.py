from random import *

cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5<=time<=15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
    i += 1

print("총 탑승 승객 : "+str(cnt)+ " 분")