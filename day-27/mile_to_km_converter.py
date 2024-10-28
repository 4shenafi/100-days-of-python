from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

def mile_to_km():
    mile_value = float(mile_entry.get())
    output_label['text'] = mile_value * 1.609

mile_entry = Entry(window)
mile_entry.grid(row=0, column=1)

label_1 = Label(window, text='Mile to Km')
label_1.grid(row=1, column=0)

output_label = Label(window, text='0')
output_label.grid(row=2, column=1)

label_2 = Label(window, text='Mile')
label_2.grid(row=0, column=2)

label_2 = Label(window, text='KM')
label_2.grid(row=2, column=2)

button_1 = Button(window, text='Convert', command=mile_to_km)
button_1.grid(row=3, column=1)

window.mainloop()