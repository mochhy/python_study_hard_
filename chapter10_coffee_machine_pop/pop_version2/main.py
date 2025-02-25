import time
MENU = {
    "에스프레소":{
        "재료": {
            "물":50,
            "커피":18,
        },
        "가격":1.5,
    },
    "라떼":{
        "재료":{
            "물":200,
            "우유":150,
            "커피":24,
        },
        "가격":2.5,
    },
    "카푸치노":{
        "재료":{
            "물":250,
            "우유":100,
            "커피":24,
        },
        "가격":3.0,
    }
}
profit = 0
resources = {
    "물":300,
    "우유":200,
    "커피":100,
}

# 함수들 정의
def is_resources_enough(order_ingredients):
    """DocString :  함수 / 클래스/ 매서드가 어떤 작동을 하는지 ' 사람들에게' 설명해주는 기능
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후 , 음료 만들기가 가능하면
    True 반환, 아니면 False 반환
    : param : order_ingredients
    :return : True / False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item] :
            print(f"미안.😥 {item}이(가) 부족해.🥺")
            return False
        return True

def process_coins():
    """동전들을 입력받아 전체 금액을 반환하는 함수 call3()유형"""
    total = 0.0
    total += int(input("쿼터 동전을 몇개 넣을거야? >>>")) * 0.25
    total += int(input("다임 동전을 몇개 넣을거야? >>>")) * 0.1
    total += int(input("니켈 동전을 몇개 넣을거야? >>>")) * 0.05
    total += int(input("페니 동전을 몇개 넣을거야? >>>")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아 동전이 가격보다 높으면 True, 아니면 False 반환"""
    charge = money_received - drink_cost
    if charge < 0 :
        print(f"동전이 충분하지 않아. 금액 ${money_received}을 반환할게.")
        return False
    else :
        global profit
        profit += drink_cost
        print(f"잔돈 ${charge}을 반환할게!")
        return True

def simsim(dri):
    asd = dri + "가 만들어지는중... 조금만 기다려줘!"
    for i in asd:
        print(i, end = '')
        time.sleep(0.2)
    print("\n")
    return 0

is_on = True
while is_on:
    choice = input("☕어떤 음료를 마실거야?☕ 에스프레소 / 라떼 / 카푸치노 >>>>")
    if choice == "off" :
        is_on = False
        print("자판기가 종료되었어.~(>_<。)＼")
    elif choice == "report" :
        print(f"물 : {resources["물"]}ml")
        print(f"우유 : {resources["우유"]}ml")
        print(f"커피 : {resources["커피"]}g")
        print(f"돈 : ${profit}")
    elif choice in ["에스프레소","라떼","카푸치노"]:
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]):
            money_received = process_coins()
            if is_transaction_successful(money_received,drink["가격"]):
                for ite in drink["재료"]:
                    resources[ite] -= drink["재료"][ite]
                simsim(choice)
                print(f"{choice}가 나왔어! 맛있게 먹어!😄")
    else :
        print("잘못 입력되었어.😦 다시 입력해줘!😉")