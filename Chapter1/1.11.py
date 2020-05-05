import tkinter as tk

root = tk.Tk()


def show():
    print("You entered: ")
    print("Employee Number:" + str(employee_number.get()))
    print("Login Password: " + password.get())
    print("Rembember Me: " + str(remember_me.get()))
    print("*" * 30)


# IntVar Demo
tk.Label(root, text="Employee Number: ").grid(row=1, column=1)
employee_number = tk.IntVar()
tk.Entry(root, width=40, textvariable=employee_number).grid(
    row=1, column=2, columnspan=2
)
employee_number.set("120350")

# Demo of StringVar
tk.Label(root, text="Login Password").grid(row=2, column=1, sticky="w")
password = tk.StringVar()
tk.Entry(root, width=49, show="*", textvariable=password).grid(
    row=2, column=2, columnspan=2
)
password.set("mysecretpassword")

tk.Button(root, text="Login", command=show).grid(row=3, column=3)

# demo of boolean var
remember_me = tk.BooleanVar()
tk.Checkbutton(root, text="Remember Me", variable=remember_me).grid(row=3, column=2)
remember_me.set(True)


root.mainloop()
