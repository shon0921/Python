from itertools import count

a = "http://naver.com"
print(a)
a=a[7:]
print(a)
a=a[:5]
print(a)

print(a[0:3]+str(len(a))+str(a.count("e"))+"!")