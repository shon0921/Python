# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + " 이예요")
hobby = "공놀이"                                           # 콤마 사용하면 str 안써도 그대로 출력됨
print(name + "는 " ,age ,"살이며, ",hobby,"을 아주 좋아해요") # str로 정수는 문자열 변경 해줘야함
print(name+"는 어른일까요? "+str(is_adult))