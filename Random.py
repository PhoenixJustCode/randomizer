from tkinter import *
from random import *

root = Tk()
poeple = []
root.title('Рандомайзер by Phoenix')
lf1 = LabelFrame(root, text='Имя,Никнейм или Числа')
lf2 = LabelFrame(root, text='Случайный выбор')
lf3 = LabelFrame(root, text='Список участвующих')
lf4 = Label(root, text='Cоздатель : Phoenix')
lf5 = Label(root, text='Telegram : @phoenix_wb')

e1 = Entry(lf1)
l1 = Label(lf2)
b1 = Button(root, text='Добавить в список', bg='green')
b2 = Button(root, text='Выбрать', bg='red')
t = Text(lf3, bg='white', width=40, height=20)


def AddMan(event=None):
    global poeple
    a = poeple.append(e1.get())
    t.insert(END, e1.get() + '\n')
    e1.delete(0, END)


b1['command'] = AddMan
e1.bind('<Return>', AddMan)  # Привязка к клавише Enter
e1.bind('<space>', AddMan)  # Привязка к клавише Space


def ChoiceMan():
    global poeple
    if poeple:
        man = choice(poeple)
        l1['text'] = man


b2['command'] = ChoiceMan

lf4.pack()
lf5.pack()
lf1.pack()
e1.pack()
b1.pack()
lf2.pack(side=BOTTOM)
b2.pack(side=BOTTOM)
l1.pack()
lf3.pack()
t.pack()
root.mainloop()
