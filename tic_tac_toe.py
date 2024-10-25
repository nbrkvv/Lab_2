import tkinter as tk
from tkinter import messagebox

# Размеры окна и клеток
CELL_SIZE = 100
WINDOW_WIDTH = CELL_SIZE * 3
WINDOW_HEIGHT = CELL_SIZE * 3

# Список для хранения состояния каждой клетки
board = [[0 for _ in range(3)] for _ in range(3)]

# Текущий игрок (1 - Крестик, -1 - Нолик)
current_player = 1

def draw_x(canvas, row, col):
    x1 = col * CELL_SIZE + 10
    y1 = row * CELL_SIZE + 10
    x2 = (col + 1) * CELL_SIZE - 10
    y2 = (row + 1) * CELL_SIZE - 10
    canvas.create_line(x1, y1, x2, y2, width=4)
    canvas.create_line(x2, y1, x1, y2, width=4)

def draw_o(canvas, row, col):
    center_x = (col + 0.5) * CELL_SIZE
    center_y = (row + 0.5) * CELL_SIZE
    radius = CELL_SIZE / 2 - 20
    canvas.create_oval(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius, width=4)

def on_click(event):
    global current_player
    
    # Определяем координаты клетки
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    
    if board[row][col] == 0:
        # Помещаем символ текущего игрока в клетку
        board[row][col] = current_player
        
        # Рисуем крестик или нолик
        if current_player == 1:
            draw_x(canvas, row, col)
        else:
            draw_o(canvas, row, col)
            
        # Проверяем, есть ли победитель
        winner = check_winner()
        if winner != 0:
            end_game(winner)
        elif is_board_full():
            end_game(0)
        else:
            # Меняем текущего игрока
            current_player *= -1

def check_winner():
    # Проверка строк
    for i in range(3):
        if abs(sum(board[i])) == 3:
            return board[i][0]
    
    # Проверка столбцов
    for j in range(3):
        if abs(sum([board[i][j] for i in range(3)])) == 3:
            return board[0][j]
    
    # Проверка диагоналей
    if abs(sum([board[i][i] for i in range(3)])) == 3:
        return board[0][0]
    if abs(sum([board[i][2-i] for i in range(3)])) == 3:
        return board[0][2]
    
    return 0

def is_board_full():
    for row in board:
        if 0 in row:
            return False
    return True

def end_game(winner):
    if winner == 1:
        result_text = "Победили X!"
    elif winner == -1:
        result_text = "Победили O!"
    else:
        result_text = "Ничья!"
    
    # Выводим сообщение о результате игры
    messagebox.showinfo("Результат игры", f"{result_text}\nХотите сыграть еще раз?")
    
    # Сбрасываем игру
    reset_game()

def reset_game():
    global current_player
    current_player = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = 0
    canvas.delete("all")

# Создаем главное окно
root = tk.Tk()
root.title("Крестики-Нолики")
root.iconbitmap(default="toe.ico")

# Создаем холст для рисования
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='white')
canvas.pack()

# Привязываем событие клика мыши к функции on_click
canvas.bind("<Button-1>", on_click)

# Запускаем главный цикл
root.mainloop()