import travel.thailand      # 파일명?만 가능
trip_to = travel.thailand.ThailandPackage()     # 패키지 넣기
trip_to.detail()

from travel.thailand import ThailandPackage     # 전부 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()  # __all__
trip_to.detail()