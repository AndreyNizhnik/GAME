import tkinter

# ---------------------------- USER INTERFACE SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title("Tic Tac Toe Game v1.012")
window.config(padx=50, pady=50, bg="light grey")
window.wm_minsize(width=400, height=500)

color = ["navy blue", "green"]
tick = ["X", "O"]
turn = 0
button_list = []

def check_winner(status):
    game_over = False
    win = 0
    # Test 1
    for c in range(0, 3):
        for r in range(0, 3):
            if button_list[c][r].cget("text") == status:
                win +=1
        if win == 3:
            print(f"WINNER! TEST 1 = {status, c, r, win}")
            button_list[c][r].config(bg="light green")
            button_list[c][r-1].config(bg="light green")
            button_list[c][r-2].config(bg="light green")
            game_over = True
            return game_over
            win = 0
        else:
            win = 0
    # Test 2
    for r in range(0, 3):
        for c in range(0, 3):
            if button_list[c][r].cget("text") == status:
                win += 1
        if win == 3:
            print(f"WINNER! TEST 2 = {status, c, r, win}")
            button_list[c][r].config(bg="light green")
            button_list[c-1][r].config(bg="light green")
            button_list[c-2][r].config(bg="light green")
            game_over = True
            return game_over
            win = 0
        else:
            win = 0
    # Test 3
    for i in range(0,3):
        if button_list[i][i].cget("text") == status:
            win += 1
    if win == 3:
        print(f"WINNER! TEST 3 = {status, c, r, win}")
        button_list[i][i].config(bg="light green")
        button_list[i-1][i-1].config(bg="light green")
        button_list[i-2][i-2].config(bg="light green")
        game_over = True
        return game_over
        win = 0
    else:
        win = 0
    # Test 4
    for i in range(0, 3):
        if button_list[i][(2-i)].cget("text") == status:
            win += 1
    if win == 3:
        print(f"WINNER! TEST 4 = {status, c, r, win}")
        button_list[i][2-i].config(bg="light green")
        button_list[i-1][2-i+1].config(bg="light green")
        button_list[i-2][2-i+2].config(bg="light green")
        game_over = True
        return game_over
        win = 0
    else:
        win = 0


def click(c, r):
    if (check_winner(status="X") != True) and (check_winner(status="O") != True):
        global turn
        if button_list[c][r].cget("text") == "":
            button_list[c][r].config(fg=color[turn], text=tick[turn])
            turn += 1
            if (turn % 2) == 0:
                turn = 0
            else:
                turn = 1
        if check_winner(status="X"):
            print("Winner is 'X'")
        if check_winner(status="O"):
            print("Winner is 'O'")


def clear():
    global turn
    turn = 0
    for c in range(0, 3):
        for r in range(0, 3):
            button_list[c][r].config(fg="black", text="", bg="light blue")


def create_buttons():
    for c in range(0, 3):
        button_column_list = []
        for r in range(0, 3):
            button = tkinter.Button()
            button.grid(column=c, row=r)
            button.config(font=("Arial", 34, "bold"), height=2, width=5, padx=0, pady=0,
                          bg="light blue", fg="black",
                          command=lambda c=c, r=r: click(c, r))
            button_column_list.append(button)
        button_list.append(button_column_list)

    canvas = tkinter.Canvas(width=50, height=50, bg="light grey", highlightthickness=0)
    canvas.grid(column=0, row=3, columnspan=3)

    button_reset = tkinter.Button(text="Reset", font=("Arial", 26, "bold"), command=clear)
    button_reset.grid(column=1, row=4)
    button_reset.config(padx=0, pady=0, height=1, width=5, fg="black", bg="mediumseagreen")


create_buttons()



window.mainloop()
