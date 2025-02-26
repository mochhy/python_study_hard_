''''''
'''


    4. with 문
        close() 메서드를 자동으로 호출할 수 있도록 하는 명령어

    형식 :
with open (파일명, 모드) as 파일객체:
    파일 처리 코드

'''

'''
2. 파일 출력
    1) 텍스트 파일 생성하고 작성하기
'''

# file = open("hello.txt","wt")
# file.write("hello")
# file.close()
'''
텍스트 파일에 내용 추가하기
'''
# file = open("hello.txt","at")
# file.write("\nIt's windy and cold today.")
# file.close()

'''
기본예제

오늘의 스케줄을 입력하면 그 내용을 모두 파일에 보관하는 프로그램을 작성할 예정입니다. 스케줄을 입력하지 ㅇ낳고
enter 을 누르면 프로그램을 종료합니다. 생성되는 파일의 이름은 현재 날짜이고, 확장자는 txt 입니다.
"2020-10-22.txt" 와 같은 형식을 갖추고 있습니다.
'''

# import time
# file = open(time.strftime("%Y-%m-%d")+".txt","at")
# end_of_schedule = False
# while not end_of_schedule:
#     schedule = input("오늘의 스케줄을 입력하세요.>>>")
#     if schedule :
#         file.write(schedule + "\n")
#     else:
#         end_of_schedule = True
#         print("종료되었습니다.")
# print("오늘의 날짜에 스케줄을 추가했습니다.")
# file.close()
'''
빈값(null/None)의 경우 기본적으로 조건식에서 False로 판명됨.

3. 파일 입력(input)
    1) 텍스트 파일 읽기
        1-1) read() 메서드
        형식 :
        file.read(size)
'''
# file = open("2025-02-26.txt","rt")
#
# schedules = file.read()
#
# print(schedules)
# file.close()
'''
파일과 동일한 모습으로 출력하기 위해서 print() 함수의 자동 줄바꿈 방지를 위한 end='' 속성을 추가
read() 메서드를 통해 전체를 읽으려면 메모리 공간이 많이 필요합니다. 읽어야 할 파일이 크다면 일부만 읽어들이는
작업을 반복하는 반복문을 통해 파일 전체를 읽도록 구현하는 편이 좋습니다.
'''
# file = open("2025-02-26.txt","rt")
# end_of_text = False
# while not end_of_text:
#     str = file.read(30)
#     print(str)
#     if not str:             #str = None이라면 이라고 해석됨
#         break
#     print(str,end='')
# file.close()
'''
이상의 코드는 30바이트씩 가지고 오게 되는데, 첫 번째 30 바이트의 결과값 이후에 자동으로 개행이 일어납니다
(print()함수의 기본 기능 때문에). 그래서 이 부분을 파일과 콘솔에 정보가 동일하도록 end= ''를 적용한 사례입니다.

    2) readline() 메서드
        텍스트 파일을 한 죽씩 읽어서 처리하는 메서드
        만약 파일이 종료되어 더 읽어들이 ㄷ이터가 없다면 빈 문자열("")을 읽어들입니다.
        반복문을 이용해서 여러번 읽어들여야 할 때 (한줄씩) 파일 전체를 읽을 수 있습니다.
'''
# file = open("2025-02-26.txt","rt")
# str = file.readline()
# print(str)
#
# file.close()

# file = open("2025-02-26.txt","rt")
# end_of_text = False
# while not end_of_text:
#     str = file.readline()
#     if not str :
#         end_of_text = True
#     print(str,end='')
# file.close()
'''
        3) readlines()메서드
            전체 라인을 읽어들여서 각 라인 단위로(개행 단위로) '리스터' 에 저장하는 메서드
'''
# with open("2025-02-26.txt","rt") as file:
#     lines = file.readlines()
#     # print(lines[0],end='')
#     # print(lines[1],end='')
#     # print(lines[2], end='')
#     # print(lines[3], end='')
#     for line in lines:
#         print(line,end='')

'''
나라별 수도를 순차적으로 반복시켜  nation 리스트에 사전에 미리 저장해두었습니다.
nation 리스트의 내용을 이해하여 다음과 같은 nation.txt 파일을 '생성' 하세요

실행 예

생성된 nation.txt 파일의 내용은 다음과 같습니다.
Greece - Athene
Germany - Berlin
South Korea - Seoul
USA - Washington D.C
'''

nation = ["Greece","Athene","Germany","Berlin","South Korea","Seoul","USA","Washington D.C"]
# file = open("nation.txt","wt")
# for i in range(len(nation)):
#     if (i+1)%2 == 0 :
#         file.write(nation[i]+"\n")
#     else :
#         file.write(nation[i]+" - ")
# file.close()

with open("nation2.txt","wt") as file:
    for i in range(0,len(nation),2):
        file.write(nation[i]+" - "+ nation[i+1] + "\n")
file.close()