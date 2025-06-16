import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title('برنامج رسم بسيط')
        self.color = '#000000'
        self.last_x, self.last_y = None, None
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        color_btn = tk.Button(root, text='اختر لون', command=self.choose_color)
        color_btn.pack(side=tk.LEFT, padx=10, pady=5)
        clear_btn = tk.Button(root, text='مسح الكل', command=self.clear)
        clear_btn.pack(side=tk.LEFT, padx=10, pady=5)
    def paint(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=4, capstyle=tk.ROUND)
        self.last_x, self.last_y = event.x, event.y
    def reset(self, event):
        self.last_x, self.last_y = None, None
    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
    def clear(self):
        self.canvas.delete('all')

if __name__ == '__main__':
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
