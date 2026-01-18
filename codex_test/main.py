def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in win_lines:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    return all(cell != " " for cell in board)


def switch_player(player):
    return "O" if player == "X" else "X"


def get_move_human(board, player):
    while True:
        raw = input(f"Ваш ход ({player}), введите 1-9: ").strip()
        if not raw.isdigit():
            print("Введите число от 1 до 9.")
            continue
        pos = int(raw) - 1
        if pos < 0 or pos > 8:
            print("Введите число от 1 до 9.")
            continue
        if board[pos] != " ":
            print("Клетка занята. Выберите другую.")
            continue
        return pos


def get_move_computer(board):
    import random

    free = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(free)


def run_game():
    board = [" "] * 9
    human = "X"
    computer = "O"
    player = human
    print("Крестики-нолики: человек против компьютера")
    print("Нумерация клеток:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board(board)
        if player == human:
            move = get_move_human(board, player)
        else:
            move = get_move_computer(board)
            print(f"Ход компьютера ({player}): {move + 1}")
        board[move] = player
        if check_winner(board, player):
            print_board(board)
            if player == human:
                print("Вы победили!")
            else:
                print("Победил компьютер.")
            break
        if is_draw(board):
            print_board(board)
            print("Ничья.")
            break
        player = switch_player(player)


if __name__ == "__main__":
    run_game()
