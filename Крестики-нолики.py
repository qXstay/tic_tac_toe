# Создаем пустое игровое поле
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Функция для вывода игрового поля
def print_board():
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]}")
        print("---------")

# Функция для проверки победы
def check_win():
    # Проверяем строки
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    # Проверяем столбцы
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # Проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Функция для получения хода от игрока
def get_move(player):
    print(f"Игрок {player}, ваш ход.")
    while True:
        row = input("Введите номер строки (1, 2, 3): ")
        col = input("Введите номер столбца (1, 2, 3): ")
        if row in ['1', '2', '3'] and col in ['1', '2', '3']:
            row, col = int(row) - 1, int(col) - 1
            if board[row][col] == " ":
                return row, col
            else:
                print("Эта клетка уже занята!")
        else:
            print("Неверный ввод, попробуйте еще раз.")

# Основной цикл игры
current_player = "X"
while True:
    print_board()
    row, col = get_move(current_player)
    board[row][col] = current_player
    if check_win():
        print_board()
        print(f"Поздравляем! Игрок {current_player} выиграл!")
        break
    if not any(" " in row for row in board):
        print_board()
        print("Игра окончена ничьей!")
        break
    current_player = "O" if current_player == "X" else "X"