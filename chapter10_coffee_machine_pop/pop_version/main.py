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
# print(MENU)
# print(MENU["라떼"]["재료"]["우유"]+1)
# # 카푸치노의 가격을 콘솔에 출력하시오
# # 에스프레소의 물 양을 콘솔에 출력하시오
# print(MENU["카푸치노"]["가격"])
# print(MENU["에스프레소"]["재료"]["물"])

# resources에서 에스프레소 두 잔을 뽑았을 때, 남는 물, 우유, 커피랑 연산하고, 그 결과를 콘솔에 출력하시오.
# resources["물"] -= MENU["에스프레소"]["재료"]["물"]*2
# resources["커피"] -= MENU["에스프레소"]["재료"]["커피"]*2
# print(resources)

# 이상을 진행했을 때 커피 두 잔이 자판기에서 나왔기 때문에 자판기에는 돈이 들어가있음
# 자판기 profit 변수에 적절한 가격을 대입하시오.

# profit += MENU["에스프레소"]["가격"]*2
# choice = input("어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>>>")
# off 라고 입력되면 종료될것
# report라고 입력되면 resources와 profit을 참조하여 manual과 같은 방식으로 콘솔에 출력될 것
# 잘못 입력 했을 경우 잘못 입력하셨습니다라는 안내문이 출력될 것

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
    # 쿼터, 다임, 니켈, 페니. 네 종류의 동전
    # 쿼터 = 0.25달러
    # 다임 = 0.1달러
    # 니켈 = 0.05달러
    # 페니 = 0.01달러
    # quarters, dimes, nickels, penniese
    # quarters = int(input("쿼터 동전은 몇개를 넣을거야? >>>")) * 0.25
    # dimes = int(input("다임 동전은 몇개를 넣을거야? >>>")) * 0.1
    # nickels = int(input("니켈 동전은 몇개를 넣을거야? >>>")) * 0.05
    # penniese = int(input("페니 동전은 몇개를 넣을거야? >>>")) * 0.01
    #
    # return quarters+ dimes+ nickels+penniese
    # 지역변수 축약

    total = 0.0
    total += int(input("쿼터 동전을 몇개 넣을거야? >>>")) * 0.25
    total += int(input("다임 동전을 몇개 넣을거야? >>>")) * 0.1
    total += int(input("니켈 동전을 몇개 넣을거야? >>>")) * 0.05
    total += int(input("페니 동전을 몇개 넣을거야? >>>")) * 0.01

    return total


#들어온 동전 금액과 가격을 비교하는 함수를 정의
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
    print(\n)
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
                print(f"{choice}가 나왔어! 맛있게 먹어!")
        # 1. 자원이 충분한지 확인
        # 2. T 라면 돈을 받아서 계산
        # 3. T라면 음료를 만들고 resources dict에 있는 수량 감소 / profit에 음료 가격만큼 더하기.

    else :
        print("잘못 입력되었어.😦 다시 입력해줘!😉")