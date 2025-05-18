import tkinter as tk
import random


# Настройка игр
WIDTH = 400  # Ширина игрового поля
HEIGHT = 400  # Высота игрового поля
DIRECTIONS = ["Up", "Down", "Left", "Right"]
CELL_SIZE = 10  # Размер одной клетки змейки и еды
DELAY = 100  # Скорость игры (задержка между движениями змейки в мс)

# Создание главного окна
root = tk.Tk()
root.title("Змейка | Счёт: 0")
root.resizable(False, False)

# Создание холста для рисования
canvas = tk.Canvas(
    root,  # Родительское окно
    width=WIDTH,  # Ширина поля
    height=HEIGHT,  # Высота поля
    bg="black",  # Цвет фона (чёрный)
    highlightthickness=0,  # Убираем границу
)
canvas.pack()  # Размещаем canvas в окне

# Начальное состояние игры
snake = [(100, 100), (90, 100), (80, 100)]
direction = "Right"
food = None
score = 0
game_over = False


# Функция генерации еды
def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)


# Создание первой еды
food = create_food()


# Отрисовка еды
def draw_food():
    canvas.create_rectangle(
        food[0], food[1], food[0] + CELL_SIZE, food[1] + CELL_SIZE, fill="red"
    )

# Отрисовка змейки
def draw_snake():
    for segment in snake:
        canvas.create_rectangle(
            segment[0], segment[1],  # Верхний левый угол
            segment[0] + CELL_SIZE,  # Нижний правый угол (x)
            segment[1] + CELL_SIZE,  # Нижний правый угол (y)
            fill="green",            # Цвет заливки
            outline="darkgreen"      # Цвет обводки
        )

# Движение змейки
def move_snake():
    head_x, head_y = snake[0]

    if direction == "Up":
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == "Down":
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == "Left":
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == "Right":
        new_head = (head_x + CELL_SIZE, head_y)

    snake.insert(0, new_head)
    snake.pop()

# Обработка клавиш
def on_key_press(event):
    global direction
    key = event.keysym
    if key in DIRECTIONS:
        if (key == "Up" and direction != "Down" or
            key == "Down" and direction != "Up" or
            key == "Left" and direction != "Right" or
            key == "Right" and direction != "Left"):
            direction = key

root.bind("<KeyPress>", on_key_press)

# Игровой цикл
def game_loop():
    global snake, food, score
    move_snake()
    canvas.delete("all")
    draw_food()
    draw_snake()
    root.after(DELAY, game_loop)


# Первоначальная отрисовка
draw_food()
root.after(DELAY, game_loop)

# Запуск главного цикла программы
root.mainloop()
