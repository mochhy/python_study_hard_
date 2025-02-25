'''
과제

은행 계좌를 관리하는 BankAccount 클래스 작성하시오. 이 클래스는 계좌 소유자 이름, 계좌 변호, 잔액을 인스턴스 변수로 가집니다.

지시사항.
     1. BankAccount 클래스를 정의하고 '생성자를 통해' owner , account_num, balance를 초기화하시오.
     2. 각 인스턴스 변수에 대한 setter / getter를 정의하시오.
     3. 입금 기능을 하는 인스턴스 매서드(deposit())를 구현하시오 -> 입금 금액을 입력 받아 잔액을 증가시킵니다.
        -> 입금 금액이 0원 이하라면 입금이 불가능하도록 로직을 작성해야 합니다.
     4. 출금 기능을 하는 인스턴스 메서드(withdraw())를 구현하시오 -> 출금 금액을 입력 받아 잔액을 감소시킵니다.
        -> 잔액 빼기 출금금액이 0원 미만이라면 출금이 불가능하도록 로직을 작성해야 합니다.
    5. 계좌 정보를 출력하는 인스턴스 메서드 print_account_info()를 구현하시오. -> 실행 예 참조
    6. 두 개의 계좌를 생성하고, 입금과 출금을 수행한 후 계좌 정보를 출력하시오.

실행 예

계좌 소유자 : 홍길동
계좌 번호 : 123-456-789
현재 잔액 : 100000원

계좌 소유자 : 심사임당
계좌 번호 : 987-654-321
현재 잔액 : 500000원

50000원이 입금되었습니다. 현재 잔액 : 150000원                # account1에 대한 입금(오만원)
잔액이 부족하여 출금할 수 없습니다.                           # account1에서 200000원 출금 시도 실패 사례(이십만원)
100000원이 출금되었습니다. 현재 잔액 : 50000원                # account1에 대한 출금 (십만원 출금 성공)


100000원이 출금되었습니다. 현재 잔액 : 400000원               # account2에 대한 출금 (십만원 출금)
200000원이 입금되었습니다. 현재 잔액 : 600000원               # account2에 대한 입금 (이십만원 입금)

최종 계좌 정보


'''

class BankAccount :
    def __init__(self,owner,account_num,balance):
        self.owner = owner
        self.account_num = account_num
        self.balance = balance

    def set_owner(self,owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def set_account_num(self,account_num):
        self.account_num = account_num

    def get_account_num(self):
        return self.account_num

    def set_balance(self,balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, balance):
        if balance <= 0 :
            print("입금 불가한 금액입니다.")
            return
        self.balance += balance
        print(f"{balance}원이 입금되었습니다. 현재 잔액 : {self.balance}")

    def withdraw(self, balance):
        if balance < 0 :
            print("출금할 수 없는 금액입니다.")
            return
        if self.balance < balance :
            print("잔액이 부족하여 출금할 수 없습니다.")
            return
        self.balance -= balance
        print(f"{balance}원이 출금되었습니다. 현재 잔액 : {self.balance}")


    def print_account_info(self):
        print(f"계좌 소유자 : {self.owner}")
        print(f"계좌 번호 : {self.account_num}")
        print(f"현재 잔액 : {self.balance}")


account1 = BankAccount("홍길동","123-456-789",100000)
account1.print_account_info()
account1.deposit(50000)
account1.withdraw(200000)
account1.withdraw(100000)
account1.print_account_info()

account2 = BankAccount("심사임당","987-654-321",500000)
account2.print_account_info()
account2.withdraw(100000)
account2.deposit(200000)
account2.print_account_info()