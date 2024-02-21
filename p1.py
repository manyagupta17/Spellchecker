from textblob import TextBlob
from tkinter import*

def correct_spelling():
    getdata= enter1.get()
    corr= TextBlob(getdata)
    data=corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)


def mainwindow():
    global enter1, enter2
    win = Tk()
    win.geometry("500x350")
    win.resizable(False,False)
    win.config(bg="Pink")
    win.title("spellcheck")

    label1=Label(win,text="Incorrect Spelling",font=("Time New Roman", 25), bg="white", fg="black")
    label1.place(x=100,y=20,height=50,width=300)
    
    enter1=Entry(win,font=("Times New Roman", 25))
    enter1.place(x=50, y=80, height=50, width=400)

    label2=Label(win,text="Correct Spelling",font=("Time New Roman", 25), bg="white", fg="black")
    label2.place(x=100,y=140,height=50,width=300)

    enter2=Entry(win,font=("Times New Roman", 25))
    enter2.place(x=50, y=200, height=50, width=400)

    button = Button(win,text="Done",font=("Time New Roman", 25), bg="white", command= correct_spelling )
    button.place(x=200, y=260, height=50, width=100)
    win.mainloop()  

mainwindow()