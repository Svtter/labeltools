import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

# 创建标签
label = tk.Label(root, text="labeltools")
label.pack()

# 创建图像
image = ImageTk.PhotoImage(Image.open("./resources/001.jpg"))
label = tk.Label(root, image=image)
label.pack()

# 创建按钮
prev_button = tk.Button(root, text="prev")
next_button = tk.Button(root, text="next")
prev_button.pack()
next_button.pack()

# 创建提交按钮
submit_button = tk.Button(root, text="submit")
submit_button.pack()

root.mainloop()
