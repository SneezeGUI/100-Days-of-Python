from tkinter import *

#window and title
window = Tk()
window.title('M to KM')
window.config(padx=20, pady=20)
window.minsize(width=225, height=150)

#entry label
label = Label(text='Miles')
label.grid(column=1, row=0)

#entry
entry = Entry()
entry.grid(column=0, row =0)

result = Label(text=f'is equal to ___ Kilometers')
result.grid(column=0, row=2)

#Button Calculate Function
def calculate():
    miles = int(entry.get())
    if miles is None:
        return None
    else:
        kilometers = round(miles * 1.60934, 2)
        result.config(text=f'is equal to {kilometers} Kilometers')
#Button
button = Button(text='Calculate', command=calculate)
button.grid(column=0, row =3)



print(type(entry))
window.mainloop()