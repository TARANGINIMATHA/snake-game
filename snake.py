from turtle import *
from random import randrange

food = (0, 0)
snake = [(10, 0)]
aim = (0, -10)

def change(x, y):
    "Change snake direction."
    global aim
    aim = (x, y)

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head[0] < 190 and -200 < head[1] < 190

def move():
    global snake, food 
    "Move snake forward one segment."
    head = (snake[-1][0] + aim[0], snake[-1][1] + aim[1])

    if not inside(head) or head in snake:
        penup()
        goto(head)
        pendown()
        fillcolor('red')
        begin_fill()
        for _ in range(4):
            forward(10)
            right(90)
        end_fill()
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food_x = randrange(-15, 15) * 10
        food_y = randrange(-15, 15) * 10
        food = (food_x, food_y)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        penup()
        goto(body)
        pendown()
        fillcolor('black')
        begin_fill()
        for _ in range(4):
            forward(10)
            right(90)
        end_fill()

    penup()
    goto(food)
    pendown()
    fillcolor('green')
    begin_fill()
    for _ in range(4):
        forward(10)
        right(90)
    end_fill()
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10),'Down')

move()
        
