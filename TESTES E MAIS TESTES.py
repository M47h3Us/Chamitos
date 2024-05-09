import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Label por baixo da linha")
label.pack()

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Desenha uma linha no canvas após o label
canvas.create_line(0, 0, 200, 100, fill="red")

root.mainloop()