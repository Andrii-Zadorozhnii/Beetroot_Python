import turtle

# Настройки экрана
screen = turtle.Screen()
screen.bgcolor("black")

# Создаем черепаху
earth = turtle.Turtle()
earth.shape("turtle")
earth.speed(10)


# Рисуем сетку координат
def draw_grid():
    earth.penup()
    earth.goto(-200, 200)
    earth.pendown()
    earth.color("white")
    for i in range(21):
        earth.penup()
        earth.goto(-200, 200 - 20 * i)
        earth.pendown()
        earth.forward(400)
    earth.right(90)
    for i in range(21):
        earth.penup()
        earth.goto(-200 + 20 * i, 200)
        earth.pendown()
        earth.forward(400)
    earth.right(90)


# Рисуем Землю
def draw_earth(radius):
    earth.penup()
    earth.goto(0, -radius)
    earth.pendown()
    earth.color("blue")
    earth.begin_fill()
    earth.circle(radius)  # Рисуем круг
    earth.end_fill()


# Рисуем континенты и острова
def draw_continents():
    earth.penup()
    earth.goto(-60, 50)  # Сначала рисуем континент
    earth.pendown()
    earth.color("green")
    earth.begin_fill()
    earth.circle(30)  # Пример континента
    earth.end_fill()

    earth.penup()
    earth.goto(40, -70)  # Остров
    earth.pendown()
    earth.color("dark green")
    earth.begin_fill()
    earth.circle(15)  # Остров
    earth.end_fill()

    earth.penup()
    earth.goto(100, 100)  # Еще один остров
    earth.pendown()
    earth.color("dark green")
    earth.begin_fill()
    earth.circle(10)  # Маленький остров
    earth.end_fill()


# Рисуем Землю с сеткой и континентами
def draw_planet():
    draw_grid()
    draw_earth(150)
    draw_continents()


# Главная функция
draw_planet()

# Завершаем работу
earth.hideturtle()
screen.mainloop()
