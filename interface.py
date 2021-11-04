from tkinter import *
root = Tk()
root.title("Генератор паролей")
root.resizable(width=False, height=False)   #запрет на изменение размера окна приложения
w=(root.winfo_screenwidth())//2-225      #Размещение окна по центру экрана
h=(root.winfo_screenheight())//2-162
root.geometry("450x324+{}+{}".format(w,h))

#Виджеты приложения
password_text = Text(root,height=14, width=30)

generate_btn=Button(text='Сгенерировать')
delete_btn=Button(text='Очистить')
save_btn=Button(text='Сохранить')

num_lbl=Label(text='Количество паролей')
num_ent=Entry(width=10, justify=CENTER)

len_lbl=Label(text='Длина паролей')
len_ent=Entry(width=10, justify=CENTER)

#Расположение виджетов в окне приложения
scrollbar=Scrollbar(root, command=password_text.yview)
num_lbl.grid(row=0, column=0)
num_ent.grid(row=0, column=1)
len_lbl.grid(row=1, column=0)
len_ent.grid(row=1, column=1)
generate_btn.grid(row=3, column=0)
delete_btn.grid(row=3, column=1)
save_btn.grid(row=3, column=2)
scrollbar.grid(row=4, column=3, sticky='nes')
password_text.grid(row=4, column=0, sticky='nsew', columnspan=3)
password_text.configure(yscrollcommand=scrollbar.set)

root.mainloop()