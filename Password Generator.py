from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title('Encrypter')

q = Entry(root)
c = Entry(root)
name = Entry(root)

#Key Functions
def password_log():
    with open('Python Scripts\Personal Scripts\Password log.txt', 'a') as kl:
        data = name.get()
        kl.write(data)
        kl.write('\n')
    name.delete(0, END)

def get_encrypt_code():
    def password_format(kind):
        pass
    with open('Password Codes.txt', 'a') as ek:
        b = 0
        raw_l = q.get()
        l = int(raw_l)
        c = []
        while b < l:
            i_bit = str(randint(0, 1))
            c.append(i_bit)
            b += 1
        c2 = ''.join(c)
        ek.write(c2)
        ek.write('\n')
        label4 = Label(root, text = c2, font = ('Segoe UI Light', 11)).grid( row = 5, column = 2)
    q.delete(0, END)

    global name
    name = Entry(root, width = 30, borderwidth = 3)
    name.grid(row = 4, column = 2, sticky = W)
    label9 = Label(root, text = 'What is this key for? ', font = ('Segoe UI Light', 11)).grid(row = 4, column = 1)
    Button4 = ttk.Button(root, text='Log', font = ('Segoe UI Light', 11), padx = 10, pady = 10, command = password_log).grid(row = 5, column = 2, sticky = E)


def retrieve_key():
    d = c.get()
    key = int(d)
    l = 0

    with open('Password Codes.txt', 'r') as ek:
        while l < (key-1):
            ek.readline()
            l += 1
        k = Entry(root, width = 70)
        k.grid(row = 7, column = 0, columnspan = 2)
        k.insert(0, ek.readline())
    c.delete(0, END)

#Main Menu
def get_encrypt_code_button():
    label8 = Label(root, text = 'How long do you want your Password:', font = ('Segoe UI Light', 11)).grid(row = 3, column = 1)
    global q
    q = Entry(root, width = 5, borderwidth = 3)
    q.grid(row = 3, column = 2, sticky = W)
    Button4 = ttk.Button(root, text='Create', command = get_encrypt_code).grid(row = 3, column = 2, sticky = E)

def retrieve_key_button():
    with open('Python Scripts\Personal Scripts\Password log.txt', 'r') as kl:
        label4 = Label(root, text = kl.read(), font = ('Segoe UI Light', 11)).grid(row = 4, column = 0, sticky = W)
    label5 = Label(root, text = 'So what\'s code do you want? ', font = ('Segoe UI Light', 11)).grid(row = 3, column = 0)
    label6 = Label(root, text = '(Give the corresponding line number)', font = ('Segoe UI Light', 11)).grid(row = 5, column = 0)
    global c
    c = Entry(root, width = 5, borderwidth = 3)
    c.grid(row = 5, column = 1, sticky = W)
    Button3 = ttk.Button(root, text='Retrieve', command = retrieve_key).grid(row = 5, column = 1, sticky = E)


#Main menu
label1 = Label(root, text = '''Hello! And welcome to version 2 of my encryption code generator.
it's very easy to use as with it you can basically create, store and recall encryption codes of any length.
The codes can then be easily copy-pasted to where they need to be used.''', font = ('Segoe UI Light', 11)).grid(row = 0, column = 0, columnspan = 3)
label2 = Label(root, text = 'So, what do you want to do?', font = ('Segoe UI Light', 11)).grid(row = 1, column = 0, columnspan = 3)
label3 = Label(root, padx = 70, pady = 50).grid(row = 2, column = 1)
Button1 = Button(root, text='Retrieve Code', font = ('Segoe UI Light', 11), padx = 40, pady = 40, command = retrieve_key_button).grid(row = 2, column = 0)
Button2 = Button(root, text='Create New Code', font = ('Segoe UI Light', 11), padx = 40, pady = 40, command = get_encrypt_code_button).grid(row = 2, column = 2)


#Looping command
root.mainloop()