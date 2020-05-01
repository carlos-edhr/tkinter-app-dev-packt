import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)

# Side and fill options
tk.Label(frame, text="Pack Demo of side and fill").pack()
tk.Button(frame, text="A").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text="B").pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text="C").pack(side=tk.RIGHT, fill=tk.NONE)
tk.Button(frame, text="D").pack(side=tk.TOP, fill=tk.BOTH)
frame.pack()

# Expand options
tk.Label(root, text="Pack demo of expand").pack()
tk.Button(root, text="I do not expand.").pack()
tk.Button(root, text="I do not fill x but I expand.").pack(expand=1)
tk.Button(root, text="I fill x and expand").pack(fill=tk.X, expand=1)

root.mainloop()
