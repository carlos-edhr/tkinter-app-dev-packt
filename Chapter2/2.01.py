from tkinter import Tk, Menu

root = Tk()

PROGRAM_NAME = " Footprint Editor "

root.title(PROGRAM_NAME)
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
# all file menu-items will be added here
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=file_menu)
menu_bar.add_cascade(label="View", menu=file_menu)
menu_bar.add_cascade(label="About", menu=file_menu)
root.config(menu=menu_bar)


root.mainloop()
