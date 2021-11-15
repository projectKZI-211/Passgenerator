from tkinter import filedialog

def save():
    file=filedialog.asksaveasfilename(filetypes=(('TXT files', '*.txt'), ('ALL files', '*.*')), defaultextension='')
    f=open(file,'w')
    f.write(password_text.get(1.0,END))
    f.close()


