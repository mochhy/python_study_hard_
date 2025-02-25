'''

1. 클래스 변수

    인스턴스 변수 : 인스턴스마다 서로 다른 값을 지니는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 :
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근 방식 - 인스턴스 접근(0)
                - 클래스 접근(x)

    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                -클래스 접근(o)




'''

# 클래스 변수 예제
# class Korean:
#     country = "한국"
#     #인스턴스 변수의 경우 생성자 내부에 있었습니다. 클래스 변수의 경우에는 이상처럼
#     # 클래스 내부에 그냥 선언하고 초기화하면 됩니다.
#
#     def __init__(self,name,age,address):
#         self.name = name                    # 인스턴스 변수1
#         self.age = age                      # 인스턴스 변수2
#         self.address = address              # 인스턴스 변수3
#
# #객체 생성
# man = Korean("안근수",38,"부산광역시 연제구")
# print(man.name)             # 객체의 속성 확인 방법
# print(man.age)              # 객체의 속성 확인 방법
# print(man.address)          # 객체의 속성 확인 방법 -> 셋 다 인스턴스 변수 확인
# # 클래스 변수 확인 방법
# print(man.country)                  # 객체명. 클래스 변수명을 통하는 접근 : 가능
# print(Korean.country)                # 객체명. 클래스 변수명을 통하는 접근 : 가능

# 객체명.클래스 변수를 통해서 클래스 변수에 접근이 가능하긴 하지만 클래스 내부의 코드를
# 들여다보기 전까지는 country라는 변수가 클래스 변수인지 인스턴스 변수인지 확인이
# 불가능하다는 문제가 있음

# 이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스 변수명으로 참조하기 보다는
# 클래스명.클래스변수명을 통해서 참조하는 것이 바람직합니다.

'''

클래스 메서드 : 클래스 변수를 사용하는 메서드

'''

# class Korean2:
#     country = "대한민국"
#
#     # 클래스 메서드 정의법
#     @classmethod                #애를 명시하면 밑의 코드가 클래스 메서드로 작성됨
#     def trip(cls,travelling_site):      #그 결과 첫번째 매개변수로 self가 아니라 cls가 자동완성
#         if cls.country == travelling_site:
#             print("국내 여행입니다.")
#         else :
#             print("해외 여행입니다.")
#
# # 클래스 메서드의 호출
# Korean2.trip("대한민국")
# Korean2.trip("미국")
# # 객체를 여기서 생성
# man2 = Korean2()
# man2.trip("일본")
#클래스 변수 때와 마찬가지로 객체명. 클래스 메서드명()으로 호출 가능
# -> 하지만 마찬가지로 얘가 인스턴스 메서드인지 클래스 메서드인지 구분할 수 없기 때문에
# 권장되는 코드 작성 요령이 아닙니다.

'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의합니다.
'''
# 클래스 정의
# class Bag
#
#     count = 0           # 클래스 변수 선언 및 초기화
#
#     def __init__(self):             # 생성자 / 인스턴스 메서드에 해당함 -> 아무 @가 없으니
#         Bag.count +=1               # 객체를 하나 생성할 때마다 클래스 변수인 count가 1씩 증가함
#         print("가방이 생산되었습니다.")       # 인스턴스 메서드가 클래스 변수를 참조할 때는 클래스명.클래스변수명으로 접근함
#
#     # 클래스 메서드 정의
#     @classmethod
#     def sell(cls):
#         print("가방이 팔렸습니다.")
#         cls.count -= 1          #클래스 메서드가 클래스 변수에 접근하기 때문에 Bag.count가 아니라 cls.count 입니다.
#
#     @classmethod
#     def remain_bag(cls):            # 클래스 변수를 main 단계에서 직접 참조하는 것이 보안상 좋지 않기 때문에
#         return cls.count            # 클래스 메서드를 생성(getter형태로) 하여 참조하는 방식
#
# print(f"현재 가방 재고 : {Bag.count}")            # 클래스 변수를 직접 참조
# print(f"현재 가방 재고 : {Bag.remain_bag()}")  # 클래스 변수를 getter를 통해 메서드르 경유하여 참조 -> 보안상 더 좋다
#
# # 객체 생성
# bag1 = Bag()        # 생성자 상기하셔야 하는데 아무런 속성이 없기 때문에 안에 argument를 채울 필요가 없습니다.
# print(f"현재 가방 재고 : {Bag.remain.bag()}") # 클래스 변수를 클래스 메서드를 통해 조작할 수 있습니다.
# bag2 = Bag()
# bag3 = Bag()
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
# bag1.sell()  # 인스턴스명.클래스메서드명()으로 호출 -> 가능했엇음 / 이 경우 사실 좀 애매
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
# Bag.sell()          # 클래스명.클래스메서드명()으로 호출 -> 더 권장되는 방식
# print(f"현재 가방 재고 : {Bag.remain_bag()}")

'''
이상의 코드에서 보면 예시이기 때문에 적합하다고 보기가 힘든데, 
인스턴스명.sell()으로 작성한다면 특정한 가방 인스턴스가 팔렸다고 볼 수 있기 때문에 가독성이 더 높은 반명
Bag.sell()으로 작성하게 된다면 어떤 가방이 팔렸는지는 모르고 그냥 가방 count 변수만 하나 줄였습니다.

저희는 코딩할 때 변수 / 메서드를 인스턴스 수준으로 작성할지 혹은 클래스 수준으로 작성할지에 대한 고민이 선행되어야만 할겁니다.

응용 예제

1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person클래스를 작성하시오.

지시사항

1. 다음과 같은 방법으로 man 과 woman 인스턴스를 생성하시오
man = person("안근수")
woman = Person("안근순")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
안근수(이)가 태어났습니다.
안근순(이)가 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f"전체 인구수 : {Person.get_population()}")

4. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
del man 
5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 안근수
'''

# class Person:
#
#     ingusu = 0              # 클래스 변수 선언 및 초기화 -> 전체 인구수이기 때매 인스턴스 변수 아님
#
#     def __init__(self,person):
#         self.person = person
#         Person.ingusu += 1
#         print(f"{self.person}(이)가 태어났습니다.")
#
#     @classmethod
#     def get_population(cls):
#         return cls.ingusu
#
#     def __del__(self):
#         Person.ingusu -= 1          # 객체가 소멸되었을 때 전체 인구수가 줄어야 한다는 점을 고려했을때 추가한게 -= 파트
#         print(f"RIP {self.person}")
#
#
# man = Person("안근수")
# print(f"전체 인구수 : {Person.get_population()}")
# woman = Person("안근순")
# print(f"전체 인구수 : {Person.get_population()}")
# del man
# print(f"전체 인구수 : {Person.get_population()}")
#
# print("프로그램이 종료되었습니다.")

'''
클래스 변수 / 클래스 메서드 활용 예제

다음 지시 사항을 일고 가겍의 매출을 구할 수 있는 Shop 클래스를 작성하시오

지시 사항
1. Shop 클래스는 다음과 같은 변수를 가지고 있다

    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 딕셔너리 요소를 가지는 리스트
    
    menu_list = [{"떡볶이": 3000},{"순대" : 4000},{"튀김" : 500 } , {"김밥" : 2000}]
     
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales("떡볶이",1)         # 떡볶이을(를) 1개 판매
Shop.sales("김밥",2)         # 김밥을(를) 2개 판매
Shop.sales("튀김",5)         # 튀김을(를) 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f"매출 : {Shop.get_total()}원")
'''
class Shop :
    total = 0
    menu_list = [{"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000}]
    menus = {"떡볶이": 3000 , "순대":4000,"튀김":500,"김밥":2000}

    @classmethod
    def sales2(cls,menu_key,account):
        for key in cls.menus:
            if key == menu_key:
                cls.total += cls.menus[key]* account


    @classmethod
    def sales(cls,menu,gasu):
        for menuname in cls.menu_list:
            for key in menuname:
                if key == menu :
                    Shop.total += menuname[key]*gasu
        print(f"{menu}을(를) {gasu}개 판매")

    @classmethod
    def get_total(cls):
        return cls.total


Shop.sales2("떡볶이",1)
Shop.sales2("김밥",2)
Shop.sales2("튀김",5)
print(f"매출 : {Shop.get_total()}원")