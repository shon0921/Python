class SoldError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                      .format(waiting,order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

