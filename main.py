from tkinter import *
from tkinter import filedialog
import random
from PIL import Image, ImageTk

root = Tk()
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>_'   #Библиотека символов

root.title("Генератор паролей")
root.resizable(width=False, height=False)   # запрет на изменение размера окна приложения
w = (root.winfo_screenwidth())//2-275      # Размещение окна по центру экрана
h = (root.winfo_screenheight())//2-165
root.geometry("550x330+{}+{}".format(w, h))

#Функция сохранения паролей в файл
def save():
    file=filedialog.asksaveasfilename(filetypes=(('TXT files', '*.txt'), ('ALL files', '*.*')), defaultextension='')
    if(file != ''):
        f=open(file,'w')
        f.write(password_text.get(1.0,END))
        f.close()

#Функция очитски поля
def delete():
    global x
    x = 0
    password_text.delete('1.0', END)

#Функция генерации паролей
x=0   #Переменная счёта паролей
def generate():
    chars_gen = chars_text.get(1.0, 'end-1c')
    try:
        for n in range(int(num_ent.get())):
            password =''
            global x
            x += 1
            for i in range(int(len_ent.get())):
                password += random.choice(chars_gen)
            password_text.insert(END, "Пароль" + ' ' + str(x) + ': ' + password + "\n")
    except ValueError:
        password_text.insert(END, "Не введена длина или количество паролей\n")
    except IndexError:
        password_text.insert(END, "Алфавит пуст\n")
        x -= 1

#Функция изменения алфавита
def alphabetChange():
    global chars
    chars = ''
    if(chk_sml_value.get()):
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if(chk_big_value.get()):
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if(chk_numb_value.get()):
        chars +='1234567890'
    if(chk_sim_value.get()):
        chars += '+-/*!&$#?=@<>_'
    chars_text.delete('1.0', END)
    chars_text.insert(END, chars)

#Область дизайна графического интерфейса
canv = Canvas(root, width=550, height=330)
canv.place(x = 0, y = 0)
img = Image.open("design/bg.png")
bg = ImageTk.PhotoImage(img)
canv.create_image(0, 0, anchor=NW, image=bg)
canv.create_rectangle(28, 4,179, 27, outline="Blue")
canv.create_rectangle(28, 36, 179, 59, outline="Blue")
canv.create_rectangle(357, 101, 512, 202, outline="Blue")
canv.create_rectangle(336, 206, 539, 229, outline="Blue")

# Виджеты приложения
password_text = Text(root, height=14, width=37, font="Verdana 9")

generate_btn = Button(text='Сгенерировать', command=generate, font="Verdana 10", bg='DeepSkyBlue')
delete_btn = Button(text='Очистить', command=delete, font="Verdana 10", bg='DeepSkyBlue')
save_btn = Button(text='Сохранить', command=save, font="Verdana 10", bg='DeepSkyBlue')

num_lbl = Label(text='Количество паролей', width = 18, font="Verdana 10", fg='MidnightBlue', justify=CENTER, bg = "LightCyan")
num_ent = Entry(width=10, justify=CENTER, font="Verdana 10")

len_lbl = Label(text='Длина паролей', width = 18, font="Verdana 10", fg='MidnightBlue', justify=CENTER, bg = "LightCyan")
len_ent = Entry(width=10, justify=CENTER, font="Verdana 10")

chk_sml_value = BooleanVar()
chk_big_value = BooleanVar()
chk_numb_value = BooleanVar()
chk_sim_value = BooleanVar()

chk_sml_value.set(True)
chk_big_value.set(True)
chk_numb_value.set(True)
chk_sim_value.set(True)

chk_sml = Checkbutton(root, var=chk_sml_value, command=alphabetChange, bg = "LightCyan")
sml_lbl = Label(text='Маленькие буквы', width = 15, font="Verdana 10", fg='MidnightBlue', justify=CENTER, anchor="w", bg = "LightCyan")
chk_big = Checkbutton(root, var=chk_big_value, command=alphabetChange, bg = "LightCyan")
big_lbl = Label(text='Заглавные буквы', width = 15, font="Verdana 10", fg='MidnightBlue', justify=CENTER, anchor="w", bg = "LightCyan")
chk_numb = Checkbutton(root, var=chk_numb_value, command=alphabetChange, bg = "LightCyan")
numb_lbl = Label(text='Цифры', width = 15, font="Verdana 10", fg='MidnightBlue', justify=CENTER, anchor="w", bg = "LightCyan")
chk_sim = Checkbutton(root, var=chk_sim_value, command=alphabetChange, bg = "LightCyan")
sim_lbl = Label(text='Знаки', width = 15, font="Verdana 10", fg='MidnightBlue', justify=CENTER, anchor="w", bg = "LightCyan")

chars_lbl = Label(text='Символы генерации паролей', font="Verdana 10", fg='MidnightBlue', justify=CENTER, bg = "LightCyan")
chars_text = Text(root, height=5, width=15, font="Verdana 10")
chars_text.insert(END, chars)

scrollbar_pasw = Scrollbar(root, command=password_text.yview)
scrollbar_chrs = Scrollbar(root, command=password_text.yview)

# Расположение виджетов в окне приложения
num_lbl.grid(row=0, column=0, pady=5, sticky='e')
num_ent.grid(row=0, column=1, padx=(10, 30), pady=5, sticky='w')
len_lbl.grid(row=1, column=0, pady=5, sticky='e')
len_ent.grid(row=1, column=1, padx=(10, 30), pady=5, sticky='w')
generate_btn.grid(row=2, column=0, padx=30, pady=5, sticky='e')
delete_btn.grid(row=2, column=1, padx=(40, 5), pady=5, sticky='w')
save_btn.grid(row=2, column=3, columnspan=2, padx=50, pady=5, sticky='w')
scrollbar_pasw.grid(row=3, column=2, rowspan=6, padx = (0, 10), pady = (0, 10), sticky='nws')
password_text.grid(row=3, column=0, padx = (10, 0), pady = (0, 10), sticky='nsew', columnspan=2, rowspan=6)
password_text.configure(yscrollcommand=scrollbar_pasw.set)
chk_sml.grid(row=3, column=3, padx = (15, 0), sticky='nes')
sml_lbl.grid(row=3, column=4, sticky='nws')
chk_big.grid(row=4, column=3, sticky='nes')
big_lbl.grid(row=4, column=4, sticky='nws')
chk_numb.grid(row=5, column=3, sticky='nes')
numb_lbl.grid(row=5, column=4, sticky='nws')
chk_sim.grid(row=6, column=3, sticky='nes')
sim_lbl.grid(row=6, column=4, sticky='nws')
chars_lbl.grid(row=7, column=3, columnspan=3, padx = (0, 10), pady = (5, 0), sticky='sew')
chars_text.grid(row=8, column=3, columnspan=2, padx = (4, 0), pady = (5, 10), sticky='nsew')
chars_text.configure(yscrollcommand=scrollbar_chrs.set)
scrollbar_chrs.grid(row=8, column=5, pady = (5, 10), padx = (0, 10), sticky='nws')

root.mainloop()
