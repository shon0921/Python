class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):       # super 사용시 처음 받는 것만 사용됨
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()