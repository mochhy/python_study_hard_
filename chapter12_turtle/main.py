# tultle 이라는 모듈을 사용, Turtle,Screen 클래스를 import 해야함

from turtle import Turtle,Screen

t = Turtle()            # Turtle 클래스의 객체 생성, 이름 t
screen = Screen()               # Screen 클래스의 객체 생성
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
# for _ in range(10):               # 그냥 반복 10번하고 변수 사용 안해서 _사용
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)
#
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(6):
#     t.forward(100)
#     t.left(60)
import random
color = ["white","blue","red","yellow","orange","green","purple","pink","silver","sienna"]
# colors = [0]
# for _ in range(255):
#     colors.append(_)

# 1. draw_figures(num)을 정의하시오.
# 2. num이 3 미만이라면 " 도형을 그릴 수 없습니다" 가 출력되고 메서드를 종료하시오.
# 3. 3 이상이라면 해당 메서드가 실행될 수 있도록 하시고
# 4. 반복문을 통해 draw_figures를 호출해 삼각형부터 십각형까지 그리는데,
# 5. 도형마다 색깔이 다를 수 있도록 작성하시오.

# def draw_figures(num):
#     if num < 3 :
#         print("도형을 그릴 수 없습니다")
#         return
#     t.pencolor(random.choice(color))
#     for _ in range(i):
#         dotted_line()
#         t.left(360/i)
#
# def dotted_line():
#     for ii in range(10):
#         t.pendown()
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         # t.color(random.choice(colors),random.choice(colors),random.choice(colors))
#
# for i in range(3,11):
#     draw_figures(i)
# for i in range(3,7):
#     for _ in range(i):
#         dotted_line()
#         t.left(360/i)
t.speed(0)

# for i in range(36):
#     t.color(random.choice(color))
#     t.circle(100)
#     t.left(10)
#

    # 이상의 네 줄의 코드를 응용하여 draw_spiogragh(size_of_gap)로 함수화 하십쇼

def draw_spiogragh(size_of_gap):
    for _ in range(360 // size_of_gap):
        t.color(random.choice(color))
        t.circle(100)
        t.left(size_of_gap)

draw_spiogragh(2)

# screen.listen()
#
# def up():
#     t.setheading(90)
#     t.forward(10)
# def down():
#     t.setheading(270)
#     t.forward(10)
# def right():
#     t.setheading(0)
#     t.forward(10)
# def left():
#     t.setheading(180)
#     t.forward(10)
#
# screen.onkey(key="Up",fun=up)
# screen.onkey(key="Down",fun=down)
# screen.onkey(key="Right",fun=right)
# screen.onkey(key="Left",fun=left)



screen.exitonclick()