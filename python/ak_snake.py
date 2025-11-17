import turtle
import random

# Game constants
w = 500
h = 500
food_size = 10
delay = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()
pen.color("green")

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()

snake = []
snake_dir = ""
food_position = ()

def reset():
    global snake, snake_dir, food_position
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    draw_snake()
    screen.update()
    screen.ontimer(move_snake, delay)  # THIS LINE STARTS THE GAME!

def draw_snake():
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

def move_snake():
    global snake_dir, food_position

    if not snake_dir:
        return

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_dir][0]
    new_head[1] += offsets[snake_dir][1]

    if new_head[0] > w / 2:
        new_head[0] -= w
    elif new_head[0] < -w / 2:
        new_head[0] += w
    if new_head[1] > h / 2:
        new_head[1] -= h
    elif new_head[1] < -h / 2:
        new_head[1] += h

    if new_head in snake[:-1]:
        reset()
        return

    snake.append(new_head)

    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
    else:
        snake.pop(0)

    draw_snake()
    screen.update()
    screen.ontimer(move_snake, delay)

def get_random_food_position():
    x = random.randint(int(-w / 2 + food_size), int(w / 2 - food_size))
    y = random.randint(int(-h / 2 + food_size), int(h / 2 - food_size))
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_up, "w")
screen.onkey(go_left, "a")
screen.onkey(go_down, "s")
screen.onkey(go_right, "d")

# Start the game
reset()
turtle.done()