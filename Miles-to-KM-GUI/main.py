from tkinter import *

#window and title
window = Tk()
window.title('M to KM')
window.config(padx=5, pady=5)
window.minsize(width=225, height=75)

#entry label
label = Label(text='Miles')
label.grid(column=2, row=0)

#entry
entry = Entry()
entry.grid(column=1, row =0)

#result part 1
result1 = Label(text='is equal to')
result1.grid(column=0, row= 2)
#result part 2 RESULTS INT
result2 = Label(text=f'___')
result2.grid(column=1, row= 2)
#result part 3
result1 = Label(text='KM')
result1.grid(column=2, row= 2)
# result = Label(text=f'is equal to ___ Kilometers')
# result.grid(column=0, row=2)

#Button Calculate Function
def calculate():
    miles = int(entry.get())
    if miles is None:
        return None
    else:
        kilometers = round(miles * 1.60934, 2)
        result2.config(text=f'{kilometers}')
#Button
button = Button(text='Calculate', command=calculate)
button.grid(column=1, row =3)



print(type(entry))
window.mainloop()