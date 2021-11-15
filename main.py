from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Генератор паролей")
root.resizable(width=False, height=False)   # запрет на изменение размера окна приложения
w = (root.winfo_screenwidth())//2-225      # Размещение окна по центру экрана
h = (root.winfo_screenheight())//2-162
root.geometry("450x324+{}+{}".format(w, h))

#Функция сохранения паролей в файл
def save():
    file=filedialog.asksaveasfilename(filetypes=(('TXT files', '*.txt'), ('ALL files', '*.*')), defaultextension='')
    f=open(file,'w')
    f.write(password_text.get(1.0,END))
    f.close()from tkinter import filedialog

# Виджеты приложения
password_text = Text(root, height=14, width=30)

generate_btn = Button(text='Сгенерировать')
delete_btn = Button(text='Очистить')
save_btn = Button(text='Сохранить')

num_lbl = Label(text='Количество паролей')
num_ent = Entry(width=10, justify=CENTER)

len_lbl = Label(text='Длина паролей')
len_ent = Entry(width=10, justify=CENTER)

# Расположение виджетов в окне приложения
scrollbar = Scrollbar(root, command=password_text.yview)
num_lbl.grid(row=0, column=0, padx=30, pady=5, sticky='w')
num_ent.grid(row=0, column=1, padx=30, pady=5, sticky='w')
len_lbl.grid(row=1, column=0, padx=30, pady=5, sticky='w')
len_ent.grid(row=1, column=1, padx=30, pady=5, sticky='w')
generate_btn.grid(row=3, column=0, padx=30, pady=5, sticky='e')
delete_btn.grid(row=3, column=1, padx=30, pady=5, sticky='w')
save_btn.grid(row=3, column=2, padx=50, pady=5, sticky='w')
scrollbar.grid(row=4, column=1, sticky='nes')
password_text.grid(row=4, column=0, sticky='nsew', columnspan=2)
password_text.configure(yscrollcommand=scrollbar.set)

root.mainloop()
