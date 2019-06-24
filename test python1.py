def user_choice():
    print("what size game board you want to draw? ")
    game_size = input()
    return game_size

def print_game_board(size):
    size = int(size)
    width = "-"*3 + " "
    length = "|"*1 + " " + "|" + " "
    print(width * size)
    for i in range(size):
        print(length*size)
        print(width*size)


def get_list():
    winner_is_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
    return(winner_is_2)


def game_move(user):
    print("player number " + str(user) + " Its your turn!, choose in which column you want to put your mark: ")
    user_column_choice = input()
    print("player number " + str(user) + " great! now choose in which row you want to put your mark: ")
    user_row_choice = input()
    return int(user_column_choice), int(user_row_choice)

def game_play():
    game_result = [[0] * 3] * 3
    test = [0, 0, 0]
    for i in range(15):
        breaking = 0
        if breaking == 1:
            break
        else:
            for x in range(3):
                if x == 2:
                    breaking = 1
                    print("tried too many times - breaking")
                    break
                a = game_move(1)
                if game_result[a[0]] == test:
                    test[a[1]] = 1
                    game_result[a[0]] = test
                    break
                else:
                    print("the player before you already put his mark there")
        if breaking == 1:
            break
        else:
            for x in range(3):
                if x == 2:
                    breaking = 1
                    print("tried too many times - breaking")
                    break
                b = game_move(2)
                if game_result[b[0]] != test:
                    test[b[1]] = 2
                    game_result[b[0]] = test
                    break
                else:
                    print("the player before you already put his mark there")



    print(game_result)


def check_winner(game_list=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], game_size=3):

    # check victory on columns
    for check in game_list:
        if check[0] == 1 and check[1] == 1 and check[2] == 1:
            print("winner_is_1")
        elif check[0] == 2 and check[1] == 2 and check[2] == 2:
            print("winner_is_2")

    # check victory on rows
    check_list_row = [0] * game_size
    for x in range(game_size):
        for i in range(game_size):
            check = game_list[i]
            check_list_row[i] = check[x]
        if check_list_row[0] == 1 and check_list_row[1] == 1 and check_list_row[2] == 1:
                print("winner_is_1")
        elif check_list_row[0] == 2 and check_list_row[1] == 2 and check_list_row[2] == 2:
                print("winner_is_2")

    # check victory on cross
    check_list_cross = [0] * game_size
    check_list_cross2 = [0] * game_size
    for x in range(game_size):
        check = game_list[x]
        check_list_cross[x] = check[x]
        check_list_cross2[x] = check[game_size-1-x]
    if check_list_cross[0] == 1 and check_list_cross[1] == 1 and check_list_cross[2] == 1:
        print("winner_is_1")
    elif check_list_cross[0] == 2 and check_list_cross[1] == 2 and check_list_cross[2] == 2:
        print("winner_is_2")
    if check_list_cross2[0] == 1 and check_list_cross2[1] == 1 and check_list_cross2[2] == 1:
        print("winner_is_1")
    elif check_list_cross2[0] == 2 and check_list_cross2[1] == 2 and check_list_cross2[2] == 2:
        print("winner_is_2")


def main():
    game_play()
    '''
    game_size = int(user_choice())
    print_game_board(game_size)
    check_winner(get_list(), game_size)
'''

main()
