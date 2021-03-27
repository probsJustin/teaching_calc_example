import tkinter as tk
import gui

root = tk.Tk(className="calculator example")
root.geometry("400x400")
app = gui.GUI(master=root)
app.mainloop()


