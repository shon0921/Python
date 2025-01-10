from random import *
users = range(1,21)
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users,4)

print("치킨 당첨자 : "+str(winners[0]))
print("커피 당첨자 : "+str(winners[1:4]))