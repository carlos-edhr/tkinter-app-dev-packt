import tkinter as tk

root = tk.Tk()

# absolute positioning
tk.Button(root, text="Absolute placement").place(x=20, y=10)
# Relative positioning
tk.Button(root, text="Relative").place(
    relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor="ne"
)

root.mainloop()
