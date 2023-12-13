import tkinter as tk


class App:
    def __init__(self) -> None:
        self.window = tk.Tk()

    def run(self):
        self.draw()
        self.window.mainloop()

    def draw_label(self, text):
        frame = tk.Frame()
        label = tk.Label(master=frame, text=text)
        label.pack()
        frame.pack()

    def draw(self):
        self.draw_label("I'm from Frame A.")
        self.draw_label("I'm from Frame B.")


if __name__ == "__main__":
    App().run()
