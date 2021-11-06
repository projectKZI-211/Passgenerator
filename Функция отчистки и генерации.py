import random

def delete():     #Функция очистки поля
    password_text.delete('1.0',END)
    

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'   #Библиотека символов
x=0   #Переменная счёта паролей
def generate():   #Функция генерации паролей
    for n in range(int(num_ent.get())):
        password =''
        global x
        x += 1
        for i in range(int(len_ent.get())):
            password += random.choice(chars)
        password_text.insert(END,"Пароль" + '  ' + str(x) + ': ' + password + "\n")