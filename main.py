import tkinter as tk


# Настройка игр
WIDTH = 400  # Ширина игрового поля
HEIGHT = 400  # Высота игрового поля

# Создание главного окна
root = tk.Tk()
root.title('Змейка | Счёт: 0')
root.resizable(False, False)

# Создание холста для рисования
canvas = tk.Canvas(
    root,  # Родительское окно
    width=WIDTH,  # Ширина поля
    height=HEIGHT,  # Высота поля
    bg='black',  # Цвет фона (чёрный)
    highlightthickness=0  # Убираем границу
)
canvas.pack()  # Размещаем canvas в окне

# Начальное состояние игры
snake = [(100, 100), (90, 100), (80, 100)]
direction = "Right"
food = None
score = 0
game_over = False
# Запуск главного цикла программы
root.mainloop()
