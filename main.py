import tkinter as tk


# Настройка игр
WIDTH = 400  # Ширина игрового поля
HEIGHT = 400  # Высота игрового поля

# Создание главного окна
root = tk.Tk()
root.title('Змейка | Счёт: 0')
root.resizable(False, False)

canvas = tk.Canvas(
    root,  # Родительское окно
    width=WIDTH,  # Ширина поля
    height=HEIGHT,  # Высота поля
)
# Запуск главного цикла программы
root.mainloop()
