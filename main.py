from tkinter import *
from classifier import classifier


def createWindow():
    root = Tk()
    root.title('Классификатор текста по категориям грехов')
    root.geometry('600x400+{}+{}'.format(root.winfo_screenwidth() // 2 - 300, root.winfo_screenheight() // 2 - 200))
    root.resizable(False, False)
    root['bg'] = 'black'

    text = Text(width=50, height=10)
    text.pack()

    frame = Frame()
    frame.pack()

    def displayText():
        document = text.get(1.0, END)
        label['text'] = classifier(document)

    b_get = Button(frame, text='Отправить', command=displayText)
    b_get.pack(side=LEFT)

    def deleteText():
        text.delete(1.0, END)

    b_delete = Button(frame, text='Очистить', command=deleteText)
    b_delete.pack(side=LEFT)

    label = Label()
    label['text'] = 'Здесь будет написан ваш грех'
    label.pack()

    root.mainloop()


createWindow()
