from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x691")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 691,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    501.0, 345.5,
    image=background_img)

r_indicator=PhotoImage(file='right_indicator.png')
r_indicator_lable = Label(image=r_indicator)
b1=Button(window,image=r_indicator,command=btn_clicked,bg="black")
b1.place(
    x = 648.89, y = 627,
    width = 70,
    height = 50)
l_indicator=PhotoImage(file='leeft_idicator.png')
l_indicator_lable = Label(image=l_indicator)
b2=Button(window,image=l_indicator,command=btn_clicked,bg="black")
b2.place(
    x = 285, y = 627,
    width = 70,
    height = 50)
upper=PhotoImage(file='upper.png')
upper_lable = Label(image=upper)
b3=Button(window,image=upper,command=btn_clicked,bg="black")
b3.place(
    x = 413.7, y = 627,
    width = 70,
    height = 50)
dipper=PhotoImage(file='dipper.png')
dipper_lable = Label(image=dipper)
b4=Button(window,image=dipper,command=btn_clicked,bg="black")
b4.place(
    x = 515.56, y = 627,
    width = 70,
    height = 50)


window.resizable(False, False)
window.mainloop()
