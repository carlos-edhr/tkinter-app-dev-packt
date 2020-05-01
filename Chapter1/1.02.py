import tkinter as tk
root = tk.Tk()

tk.Label(root, text="I am label widget").pack()
button = tk.Button(root, text="I am button")
button.pack()



root.mainloop()