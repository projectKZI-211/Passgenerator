from tkinter import *
from tkinter import filedialog
import random
root = Tk()
root.title("Генератор паролей")
root.resizable(width=False, height=False)   # запрет на изменение размера окна приложения
w = (root.winfo_screenwidth())//2-258      # Размещение окна по центру экрана
h = (root.winfo_screenheight())//2-169
root.geometry("516x338+{}+{}".format(w, h))

#Функция сохранения паролей в файл
def save():
    file=filedialog.asksaveasfilename(filetypes=(('TXT files', '*.txt'), ('ALL files', '*.*')), defaultextension='')
    f=open(file,'w')
    f.write(password_text.get(1.0,END))
    f.close()

#Функция очитски поля
def delete():     #Функция очистки поля
    global x
    x = 0
    password_text.delete('1.0',END)

#Функция генерации паролей
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'   #Библиотека символов
x=0   #Переменная счёта паролей
def generate():   #Функция генерации паролей
    for n in range(int(num_ent.get())):
        password =''
        global x
        x += 1
        for i in range(int(len_ent.get())):
            password += random.choice(chars)
        password_text.insert(END, "Пароль" + ' ' + str(x) + ': ' + password + "\n")

# Виджеты приложения
password_text = Text(root, height=14, width=30)

generate_btn = Button(text='Сгенерировать', command=generate)
delete_btn = Button(text='Очистить', command=delete)
save_btn = Button(text='Сохранить', command=save)

num_lbl = Label(text='Количество паролей')
num_ent = Entry(width=10, justify=CENTER)

len_lbl = Label(text='Длина паролей')
len_ent = Entry(width=10, justify=CENTER)

chk_sml = Checkbutton()
sml_lbl = Label(text='Маленькие буквы')
chk_big = Checkbutton()
big_lbl = Label(text='Заглавные буквы')
chk_numb = Checkbutton()
numb_lbl = Label(text='Цифры')
chk_sim = Checkbutton()
sim_lbl = Label(text='Знаки')

chars_lbl = Label(text='Символы генерации паролей:')
chars_text = Text(root, height=5, width=15)

scrollbar_pasw = Scrollbar(root, command=password_text.yview)
scrollbar_chrs = Scrollbar(root, command=password_text.yview)

# Расположение виджетов в окне приложения
num_lbl.grid(row=0, column=0, padx=30, pady=5, sticky='w')
num_ent.grid(row=0, column=1, padx=30, pady=5, sticky='w')
len_lbl.grid(row=1, column=0, padx=30, pady=5, sticky='w')
len_ent.grid(row=1, column=1, padx=30, pady=5, sticky='w')
generate_btn.grid(row=2, column=0, padx=30, pady=5, sticky='e')
delete_btn.grid(row=2, column=1, padx=30, pady=5, sticky='w')
save_btn.grid(row=2, column=3, columnspan=2, padx=50, pady=5, sticky='w')
scrollbar_pasw.grid(row=3, column=2, rowspan=6, sticky='nws')
password_text.grid(row=3, column=0, sticky='nsew', columnspan=2, rowspan=6)
password_text.configure(yscrollcommand=scrollbar_pasw.set)
chk_sml.grid(row=3, column=3, sticky='nes')
sml_lbl.grid(row=3, column=4, sticky='nws')
chk_big.grid(row=4, column=3, sticky='nes')
big_lbl.grid(row=4, column=4, sticky='nws')
chk_numb.grid(row=5, column=3, sticky='nes')
numb_lbl.grid(row=5, column=4, sticky='nws')
chk_sim.grid(row=6, column=3, sticky='nes')
sim_lbl.grid(row=6, column=4, sticky='nws')
chars_lbl.grid(row=7, column=3, columnspan=2, sticky='nws')
chars_text.grid(row=8, column=3, columnspan=2, pady=5, sticky='nsew')
chars_text.configure(yscrollcommand=scrollbar_chrs.set)
scrollbar_chrs.grid(row=8, column=5, sticky='nws')

root.mainloop()
