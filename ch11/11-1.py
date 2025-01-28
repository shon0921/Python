import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 떄

import theater_module as mv     # mv 로만 모듈 호출 가능 (별명)
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *    # 더 줄이기
# from random import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning     # 필요한 것만 사용
price(3)
price_morning(4)
# price_soldier(5) 에러

from theater_module import price_soldier as price   # 필요한 것만, 별명
price(5)