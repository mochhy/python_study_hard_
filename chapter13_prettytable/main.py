'''

외부 패키지의 설치

좌측 상단 메뉴버튼(햄버거) -> file -> settings(설정 : ctrl + alt + s)
좌측 리스트에서 project : 프로젝트명으로 되어있는 부분 클릭
-> python interpreter
-> 좌상단에 + 눌러서 필요한 패키지 검색 및 설치

'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

table = PrettyTable()
table.field_names = ["번호","이름","타입"]
for i in range(len(pokemon_data)):              # 26 0번지 ~ 25번지
    table.add_row(pokemon_data[i])

# 데이터를 그대로 집어넣는 것을 하드코딩 이라고함

print(table)