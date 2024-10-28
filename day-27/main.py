from tkinter import *

window = Tk()
window.minsize(500, 600)
# window.title("Testing tkinter")
# my_1st_label = Label(window, text="Tis is my first label" , font=("Helvetica", 20, "bold"))
# my_1st_label.pack()
#
# label_2 = Label(window, text="New text", font=("Helvetica", 24, "bold"))
# label_2.pack()
#
# #button
# def clicked_button():
#     label_2["text"] = input.get()
# button = Button(window, text="Click Me", command=clicked_button)
# button.pack()
#
#
# #entry
# input = Entry(window)
# input.pack()

window.title('tkinter grid test')

label_1 = Label(window, text="Label 1")
label_1.grid(column=0, row=0)

button_1 = Button(window, text="Button")
button_1.grid(column=1, row=1)

button_2 = Button(window, text="New Button")
button_2.grid(column=2, row=0)

entry_1 = Entry(window)
entry_1.grid(column=3, row=2)


window.mainloop()