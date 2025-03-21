from tkinter import *

window = Tk()
window.title("Miles to Kilometers converter")
window.minsize(width= 500, height= 300)
window.config(padx= 20, pady= 20)

label = Label(text= "Miles is equal to ", font= ("Arial", 15, "normal"))
label.grid(column= 2, row= 0)

miles_ip = Entry(width= 10)
miles_ip.grid(column= 1, row= 0)

km_label = Label(text= "0 Km", font= ("Arial", 15, "normal"))
km_label.grid(column= 3, row= 0)
def calculation():
    result = round(float(miles_ip.get()) * 1.609, 2)
    km_label.config(text= f"{result} Km")

button = Button(text= "Calculate", command= calculation)
button.grid(column=2, row= 2)
window.mainloop()