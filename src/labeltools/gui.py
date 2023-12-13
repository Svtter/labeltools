import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("labeltools")

# 创建图像
image = ImageTk.PhotoImage(Image.open("./resources/001.jpg"))
label = tk.Label(root, image=image)
label.pack()

# 创建按钮
subf2 = tk.Frame(master=root)
for i, text in zip(range(2), ["prev", "next"]):
    frame = tk.Frame(master=subf2)
    frame.grid(row=0, column=i, padx=10)
    btn = tk.Button(frame, text=text)
    btn.pack()

subf2.pack()

# 创建提交按钮

subf3 = tk.Frame(master=root)
f = tk.Frame(master=subf3)
f.grid(row=0, column=0, padx=10)
entry = tk.Entry(master=f)
entry.pack()

f = tk.Frame(master=subf3)
f.grid(row=0, column=1, padx=10)
submit_button = tk.Button(f, text="submit")
submit_button.pack()
subf3.pack()

root.mainloop()
