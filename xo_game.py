import tkinter as tk
from tkinter import messagebox
import random

# لعبة XO (Tic-Tac-Toe) بسيطة في بايثون

# تعريف المتغيرات العامة
board = [' ' for _ in range(9)]
current_player = 'X'
buttons = []

# لوحة اللعب
def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-+-+-')

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # صفوف
        [0,3,6], [1,4,7], [2,5,8], # أعمدة
        [0,4,8], [2,4,6]           # أقطار
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

def is_full():
    return all(cell != ' ' for cell in board)

def new_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for btn in buttons:
        btn.config(text='', state=tk.NORMAL)

def on_click(i):
    global current_player
    if board[i] == ' ':
        board[i] = current_player
        buttons[i].config(text=current_player)
        if check_winner(current_player):
            messagebox.showinfo('انتهت اللعبة', f'اللاعب {current_player} فاز!')
            for btn in buttons:
                btn.config(state=tk.DISABLED)
        elif is_full():
            messagebox.showinfo('انتهت اللعبة', 'تعادل!')
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def gui():
    global buttons
    root = tk.Tk()
    root.title('لعبة XO')
    frame = tk.Frame(root)
    frame.pack()
    buttons = []
    for i in range(9):
        btn = tk.Button(frame, text='', font=('Arial', 32), width=3, height=1,
                        command=lambda i=i: on_click(i))
        btn.grid(row=i//3, column=i%3)
        buttons.append(btn)
    reset_btn = tk.Button(root, text='لعبة جديدة', command=new_game)
    reset_btn.pack(pady=10)
    new_game()
    root.mainloop()

def play_rock_paper_scissors():
    def play():
        user_choice = var.get()
        comp_choice = random.choice(['حجر', 'ورقة', 'مقص'])
        result = ''
        if user_choice == comp_choice:
            result = 'تعادل!'
        elif (user_choice == 'حجر' and comp_choice == 'مقص') or \
             (user_choice == 'ورقة' and comp_choice == 'حجر') or \
             (user_choice == 'مقص' and comp_choice == 'ورقة'):
            result = 'أنت فزت!'
        else:
            result = 'الكمبيوتر فاز!'
        messagebox.showinfo('النتيجة', f'اختيارك: {user_choice}\nاختيار الكمبيوتر: {comp_choice}\n{result}')

    rps_win = tk.Toplevel()
    rps_win.title('حجر ورقة مقص')
    tk.Label(rps_win, text='اختر:', font=('Arial', 18)).pack(pady=10)
    var = tk.StringVar(value='حجر')
    for choice in ['حجر', 'ورقة', 'مقص']:
        tk.Radiobutton(rps_win, text=choice, variable=var, value=choice, font=('Arial', 16)).pack(anchor='w')
    tk.Button(rps_win, text='العب', command=play, font=('Arial', 16)).pack(pady=10)

def play_guess_number():
    def check():
        guess = entry.get()
        if not guess.isdigit():
            result_lbl.config(text='أدخل رقمًا صحيحًا!', fg='red')
            return
        g = int(guess)
        if g == number:
            result_lbl.config(text='مبروك! خمنت الرقم!', fg='green')
            btn.config(state=tk.DISABLED)
        elif g < number:
            result_lbl.config(text='أكبر!', fg='blue')
        else:
            result_lbl.config(text='أصغر!', fg='blue')
    number = random.randint(1, 50)
    win = tk.Toplevel()
    win.title('تخمين الرقم')
    tk.Label(win, text='خمن رقم من 1 إلى 50', font=('Arial', 18)).pack(pady=10)
    entry = tk.Entry(win, font=('Arial', 16))
    entry.pack(pady=5)
    btn = tk.Button(win, text='تحقق', command=check, font=('Arial', 16))
    btn.pack(pady=5)
    result_lbl = tk.Label(win, text='', font=('Arial', 16))
    result_lbl.pack(pady=10)

def play_mini_sudoku():
    # سودوكو 4x4 بسيط
    solution = [1,2,3,4,2,3,4,1,3,4,1,2,4,1,2,3]
    random.shuffle(solution)
    win = tk.Toplevel()
    win.title('سودوكو مصغر')
    tk.Label(win, text='سودوكو 4x4 - املأ الأرقام من 1 إلى 4', font=('Arial', 16)).pack(pady=5)
    entries = []
    frame = tk.Frame(win)
    frame.pack()
    for i in range(4):
        row = []
        for j in range(4):
            e = tk.Entry(frame, width=2, font=('Arial', 18), justify='center')
            e.grid(row=i, column=j, padx=2, pady=2)
            row.append(e)
        entries.append(row)
    def check():
        for i in range(4):
            for j in range(4):
                val = entries[i][j].get()
                if not val.isdigit() or not (1 <= int(val) <= 4):
                    messagebox.showinfo('خطأ', 'كل الخانات يجب أن تحتوي رقم من 1 إلى 4')
                    return
        messagebox.showinfo('ممتاز', 'تم التحقق!')
    tk.Button(win, text='تحقق', command=check, font=('Arial', 14)).pack(pady=8)

def play_snake():
    # لعبة الثعبان البسيطة بدون threading
    win = tk.Toplevel()
    win.title('الثعبان')
    c = tk.Canvas(win, width=300, height=300, bg='#222')
    c.pack()
    win.focus_force()
    c.focus_set()
    direction = [0, -1]
    snake = [(7,7), (7,8), (7,9)]
    food = [random.randint(0,14), random.randint(0,14)]
    running = [True]
    def draw():
        c.delete('all')
        for x, y in snake:
            c.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill='lime')
        c.create_oval(food[0]*20, food[1]*20, food[0]*20+20, food[1]*20+20, fill='red')
    def move():
        if not running[0]:
            return
        head = (snake[0][0]+direction[0], snake[0][1]+direction[1])
        if head in snake or not (0<=head[0]<15 and 0<=head[1]<15):
            messagebox.showinfo('انتهت اللعبة', f'النقاط: {len(snake)}')
            running[0] = False
            return
        snake.insert(0, head)
        if head == tuple(food):
            food[0], food[1] = random.randint(0,14), random.randint(0,14)
        else:
            snake.pop()
        draw()
        win.after(150, move)
    def on_key(event):
        k = event.keysym
        if k == 'Up' and direction != [0,1]: direction[0], direction[1] = 0, -1
        elif k == 'Down' and direction != [0,-1]: direction[0], direction[1] = 0, 1
        elif k == 'Left' and direction != [1,0]: direction[0], direction[1] = -1, 0
        elif k == 'Right' and direction != [-1,0]: direction[0], direction[1] = 1, 0
    win.bind('<Key>', on_key)
    draw()
    win.after(150, move)

def play_minecraft_mini():
    # لعبة بناء كتل بسيطة
    size = 10
    grid = [[0]*size for _ in range(size)]
    player = [size//2, size//2]
    win = tk.Toplevel()
    win.title('Minecraft Mini')
    win.configure(bg='#3c2f1c')
    c = tk.Canvas(win, width=400, height=400, bg='#7ec850', highlightthickness=0)
    c.pack(padx=10, pady=10)
    block_colors = {0:'#7ec850', 1:'#b97a57'}
    def draw():
        c.delete('all')
        for i in range(size):
            for j in range(size):
                color = block_colors[grid[i][j]]
                c.create_rectangle(j*40, i*40, j*40+40, i*40+40, fill=color, outline='#3c2f1c', width=2)
        # رسم اللاعب
        c.create_rectangle(player[1]*40+8, player[0]*40+8, player[1]*40+32, player[0]*40+32, fill='#3a3a3a', outline='#222', width=2)
    def move(dx, dy):
        ni, nj = player[0]+dy, player[1]+dx
        if 0 <= ni < size and 0 <= nj < size:
            player[0], player[1] = ni, nj
            draw()
    def place_block():
        grid[player[0]][player[1]] = 1
        draw()
    def remove_block():
        grid[player[0]][player[1]] = 0
        draw()
    win.bind('<Up>', lambda e: move(0,-1))
    win.bind('<Down>', lambda e: move(0,1))
    win.bind('<Left>', lambda e: move(-1,0))
    win.bind('<Right>', lambda e: move(1,0))
    win.bind('w', lambda e: move(0,-1))
    win.bind('s', lambda e: move(0,1))
    win.bind('a', lambda e: move(-1,0))
    win.bind('d', lambda e: move(1,0))
    win.bind('<space>', lambda e: place_block())
    win.bind('<BackSpace>', lambda e: remove_block())
    draw()
    tk.Label(win, text='الأسهم/WASD للحركة، Space لوضع بلوك، Backspace لإزالة بلوك', bg='#3c2f1c', fg='#fff', font=('Minecraft', 10)).pack(pady=5)

def main_menu():
    def open_xo():
        menu_win.destroy()
        gui()
    def open_rps():
        menu_win.destroy()
        play_rock_paper_scissors()
    def open_guess():
        menu_win.destroy()
        play_guess_number()
    def open_sudoku():
        menu_win.destroy()
        play_mini_sudoku()
    def open_snake():
        menu_win.destroy()
        play_snake()
    def open_minecraft():
        menu_win.destroy()
        play_minecraft_mini()
    menu_win = tk.Tk()
    menu_win.title('ألعاب ماين كرافت')
    menu_win.configure(bg='#3c2f1c')
    tk.Label(menu_win, text='🟩 ألعاب ماين كرافت 🟫', font=('Arial Black', 28), fg='#fff', bg='#3c2f1c').pack(pady=20)
    btn_style = {'font':('Arial', 18), 'width':18, 'bg':'#7ec850', 'fg':'#3c2f1c', 'activebackground':'#b97a57', 'activeforeground':'#fff', 'bd':4, 'relief':'ridge'}
    tk.Button(menu_win, text='Minecraft Mini', command=open_minecraft, **btn_style).pack(pady=7)
    tk.Button(menu_win, text='XO', command=open_xo, **btn_style).pack(pady=7)
    tk.Button(menu_win, text='حجر ورقة مقص', command=open_rps, **btn_style).pack(pady=7)
    tk.Button(menu_win, text='تخمين الرقم', command=open_guess, **btn_style).pack(pady=7)
    tk.Button(menu_win, text='سودوكو مصغر', command=open_sudoku, **btn_style).pack(pady=7)
    tk.Button(menu_win, text='الثعبان', command=open_snake, **btn_style).pack(pady=7)
    tk.Button(menu_win, text='خروج', command=menu_win.destroy, font=('Arial', 16), width=10, bg='#b97a57', fg='#fff').pack(pady=20)
    menu_win.mainloop()

if __name__ == '__main__':
    try:
        main_menu()
    except Exception as e:
        import traceback
        with open('xo_error.log', 'w', encoding='utf-8') as f:
            f.write(traceback.format_exc())
        print('حدث خطأ! تم حفظ التفاصيل في xo_error.log')
