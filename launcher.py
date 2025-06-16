import tkinter as tk
import subprocess
import sys
import os

root = tk.Tk()
root.title('مشغل التطبيقات')
root.geometry('500x400')
root.configure(bg='#23272e')

# عنوان كبير مع ظل
header = tk.Label(root, text='✨ مركز الألعاب والإبداع ✨', font=('Arial Black', 26, 'bold'), fg='#00ff99', bg='#23272e')
header.pack(pady=(30,10))
shadow = tk.Label(root, text='✨ مركز الألعاب والإبداع ✨', font=('Arial Black', 26, 'bold'), fg='#111', bg='#23272e')
shadow.place(x=4, y=34)

btn_style = {'font':('Arial Rounded MT Bold', 18), 'width':22, 'bg':'#2ecc71', 'fg':'#fff', 'activebackground':'#27ae60', 'activeforeground':'#fff', 'bd':6, 'relief':'groove', 'cursor':'hand2'}

apps = [
    ('🎮 الألعاب المتنوعة', 'xo_game.py'),
    ('🟩 ماين كرافت 2D', 'minecraft_2d.py'),
    ('🎨 برنامج الرسم', 'paint_app.py'),
]

frame = tk.Frame(root, bg='#23272e')
frame.pack(pady=20)

def run_app(filename):
    python_exe = sys.executable
    app_path = os.path.join(os.path.dirname(__file__), filename)
    subprocess.Popen([python_exe, app_path])

for i, (label, file) in enumerate(apps):
    btn = tk.Button(frame, text=label, command=lambda f=file: run_app(f), **btn_style)
    btn.grid(row=i, column=0, pady=18, padx=10)

# فوتر عصري
footer = tk.Label(root, text='by GitHub Copilot', font=('Arial', 12, 'italic'), fg='#aaa', bg='#23272e')
footer.pack(side=tk.BOTTOM, pady=10)

exit_btn = tk.Button(root, text='خروج', command=root.destroy, font=('Arial', 16, 'bold'), width=12, bg='#e74c3c', fg='#fff', activebackground='#c0392b', bd=4, relief='ridge', cursor='hand2')
exit_btn.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
