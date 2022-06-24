from tkinter import *
from tkinter import messagebox, ttk
from random import choice, shuffle
from datetime import datetime
import string
import os


root = Tk()
root.title('Password Generator')

q = Entry(root)
r = Entry(root)
name = Entry(root)
encrypt = []
retrieve = []
row = 0

a = IntVar(encrypt, 0)
b = IntVar(encrypt, 0)
d = IntVar(encrypt, 0)

#Search for files
def find(filename):
    for rt, dirs, files in os.walk('C:'):
        if filename in files:
            return os.path.join(rt, filename)

#Retrieve Functions
def retrieve_key():
    d = r.get()
    key = int(d)
    l = 0

    with open(find('Password Codes which there should only be one of.txt'), 'r') as pc:
        while l < (key-1):
            pc.readline()
            l += 1
        Label(retrieve, text = 'Here You Go', font = ('Segoe UI Light', 11)).grid(row = row + 5, column = 1)
        k = ttk.Entry(retrieve)
        k.grid(row = row + 6, column = 0, columnspan = 3, pady = 10, padx = 10, sticky = W + E)
        k.insert(0, pc.readline())
    r.delete(0, END)

#Create password
def password_log():
    with open(find('Password log.txt'), 'a') as kl:
        data = name.get()
        kl.write(data)
        kl.write('\n')
    name.delete(0, END)
    encrypt.destroy()

def create_password():
    with open(find('Password Codes which there should only be one of.txt'), 'a') as ek:
        para_list = [a.get(), b.get(), d.get()]
        raw_l = q.get()
        l = int(raw_l)
        c1 = []
        c2 = []
        c3 = []
        divisor = 0
        char, num, sym = para_list
        for x in para_list:
            if x == 1:
                divisor += 1
        if char == 1:
            n = l/divisor
            t = 0
            while t < n:
                bit = choice(string.ascii_letters)
                c1.append(bit)
                t += 1
        if num == 1:
            n = l/divisor
            t = 0
            while t < n:
                bit = str(choice(range(0, 9)))
                c2.append(bit)
                t += 1
        if sym == 1:
            n = l/divisor
            t = 0
            while t < n:
                bit = choice(['!','@','#','$','%','^','&','*','_','+','=','-','{','[','(',')',']','}',';',':',',','.','<','>','/','?'])
                c3.append(bit)
                t += 1
        if char == 0 and num == 0 and sym == 0:
            response = messagebox.showerror('No Parameters', 'You didn\'t select any parameters')
            if response == 1:
                set_password_parameters()
            else:
                set_password_parameters()
            return
        c = c1 + c2 + c3
        shuffle(c)
        del c[l:]
        c_fin = ''.join(c)
        ek.write(c_fin)
        ek.write('\n')
        Label(encrypt, text = '3', font = ('Segoe UI Light', 11)).grid(row = 7, column = 0, padx = 10, pady = 10)
        Label(encrypt, text = 'Your Password is ', font = ('Segoe UI Light', 11)).grid(row = 7, column = 1, pady = 10, sticky = W)
        q3 = ttk.Entry(encrypt)
        q3.grid(row = 7, column = 2, padx = (0, 10), pady = 10, sticky = W)
        q3.insert(0, c_fin)

    with open('Python Scripts\Personal Scripts\Password log.txt', 'a') as dl:
        timestamp = '{:%Y-%m-%d %H:%M:%S} '.format(datetime.now())
        dl.write(timestamp)

    global name
    Label(encrypt, text = 'What is this key for? ', font = ('Segoe UI Light', 11)).grid(row = 8, column = 1, pady = 10, sticky = W)
    name = ttk.Entry(encrypt)
    name.grid(row = 8, column = 2, padx = (0, 10), pady = 10, sticky = W)
    ttk.Button(encrypt, text='Log', command = password_log).grid(row = 9, column = 2, padx = (0, 10), pady = (0, 10), sticky = E)
    ttk.Button(encrypt, text = 'Previous', command = set_password_parameters).grid(row = 9, column = 1, pady = (0, 10), sticky = W)

    Label(encrypt, text = '2', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 3, column = 0, padx = 10, pady = (10, 5))
    c = ttk.Checkbutton(encrypt, text = 'Letters', state = DISABLED)
    h = ttk.Checkbutton(encrypt, text = 'Numbers', state = DISABLED)
    e = ttk.Checkbutton(encrypt, text = 'Symbols', state = DISABLED)
    c.grid(row = 3, column = 1, pady = (10, 0), sticky = W)
    h.grid(row = 4, column = 1, sticky = W)
    e.grid(row = 5, column = 1, sticky = W)
    ttk.Button(encrypt, text = 'Next', state = DISABLED).grid(row = 5, column = 2, padx = (0, 10), pady = (0, 10), sticky = E)

def set_password_parameters():
    Label(encrypt, text = '2', font = ('Segoe UI Light', 11)).grid(row = 3, column = 0, padx = 10, pady = 10)
    global a
    global b
    global d
    a = IntVar(encrypt, 0)
    b = IntVar(encrypt, 0)
    d = IntVar(encrypt, 0)

    c = ttk.Checkbutton(encrypt, text = 'Letters', variable = a)
    h = ttk.Checkbutton(encrypt, text = 'Numbers', variable = b)
    e = ttk.Checkbutton(encrypt, text = 'Symbols', variable = d)
    c.grid(row = 3, column = 1, pady = (10, 0), sticky = W)
    h.grid(row = 4, column = 1, sticky = W)
    e.grid(row = 5, column = 1, pady = (7, 0), sticky = W)
    ttk.Button(encrypt, text = 'Next', command = create_password).grid(row = 6, column = 2, padx = (0, 10), pady = 10, sticky = E)
    ttk.Button(encrypt, text = 'Previous', command = create_password_button_func).grid(row = 6, column = 1, pady = 10, sticky = W)

    #Disabled items
    Label(encrypt, text = '3', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 7, column = 0, padx = 10, pady = 10)
    Label(encrypt, text = 'Your Password is ', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 7, column = 1, pady = 10, sticky = W)
    q3 = ttk.Entry(encrypt, state = DISABLED)
    q3.grid(row = 7, column = 2, padx = (0, 10), pady = 10, sticky = W)
    Label(encrypt, text = 'What is this key for? ', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 8, column = 1, pady = 10, sticky = W)
    name = ttk.Entry(encrypt, state = DISABLED)
    name.grid(row = 8, column = 2, padx = (0, 10), pady = 10, sticky = W)
    ttk.Button(encrypt, text='Log', state = DISABLED).grid(row = 9, column = 2, padx = (0, 10), pady = (0, 10), sticky = E)
    Label(encrypt, pady = 2).grid(row = 9, column = 1, pady = (0, 10), sticky = W + E)

    Label(encrypt, text = '1', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 0, column = 0, padx = 10, pady = 10)
    Label(encrypt, text = 'How long do you want your Password:', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 0, column = 1, columnspan = 2, pady = 10, sticky = W)

    q = ttk.Scale(encrypt,value = 0, from_ = 0, to = 256, orient = HORIZONTAL, state = DISABLED)
    q.grid(row = 1, column = 1, columnspan = 2, padx = (0, 10), pady = 10, sticky = W + E)
    ttk.Button(encrypt, text = 'Next', state = DISABLED).grid(row = 2, column = 2, padx = (0, 10), pady = (0, 10),sticky = E)

def create_password_button_func():
    Label(encrypt, text = '1', font = ('Segoe UI Light', 11)).grid(row = 0, column = 0, padx = 10, pady = 10)
    Label(encrypt, text = 'How long do you want your Password:', font = ('Segoe UI Light', 11)).grid(row = 0, column = 1, columnspan = 2, pady = 10, sticky = W)
    global q
    def slider_value(value):
        flt_v = float(q.get())
        int_v = int(flt_v)
        str_v = str(int_v)
        Label(encrypt, text = str_v).grid(row = 2, column = 1)
    q = ttk.Scale(encrypt,value = 0, from_ = 0, to = 256, orient = HORIZONTAL, command = slider_value)
    q.grid(row = 1, column = 1, columnspan = 2, padx = (0, 10), pady = 10, sticky = W + E)
    ttk.Button(encrypt, text = 'Next', command = set_password_parameters).grid(row = 2, column = 2, padx = (0, 10), pady = (0, 10),sticky = E)

    #Disabled items
    Label(encrypt, text = '2', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 3, column = 0, padx = 10, pady = 10)
    c = ttk.Checkbutton(encrypt, text = 'Letters', state = DISABLED)
    h = ttk.Checkbutton(encrypt, text = 'Numbers', state = DISABLED)
    e = ttk.Checkbutton(encrypt, text = 'Symbols', state = DISABLED)
    c.grid(row = 3, column = 1, pady = (10, 0), sticky = W)
    h.grid(row = 4, column = 1, sticky = W)
    e.grid(row = 5, column = 1,  pady = (7, 0), sticky = W)
    ttk.Button(encrypt, text = 'Next', state = DISABLED).grid(row = 6, column = 2, padx = (0, 10), pady = 10, sticky = E)
    Label(encrypt, pady = 2).grid(row = 6, column = 1, pady = 10, sticky = W + E)

    Label(encrypt, text = '3', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 7, column = 0, padx = 10, pady = 10)
    Label(encrypt, text = 'Your Password is ', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 7, column = 1, pady = 10, sticky = W)
    q3 = ttk.Entry(encrypt, state = DISABLED)
    q3.grid(row = 7, column = 2, padx = (0, 10), pady = 10, sticky = W)
    Label(encrypt, text = 'What is this key for? ', font = ('Segoe UI Light', 11), state = DISABLED).grid(row = 8, column = 1, pady = 10, sticky = W)
    name = ttk.Entry(encrypt, state = DISABLED)
    name.grid(row = 8, column = 2, padx = (0, 10), pady = 10, sticky = W)
    ttk.Button(encrypt, text='Log', state = DISABLED).grid(row = 9, column = 2, padx = (0, 10), pady = (0, 10), sticky = E)

#Main Menu
def create_password_button():
    global encrypt
    encrypt = Tk()
    encrypt.title('Create your Password')
    encrypt.geometry('305x397')

    create_password_button_func()

def retrieve_key_button():
    global retrieve
    retrieve = Tk()
    retrieve.title('Retreive Password')
    global row
    row = 1
    lineno = 1
    lf = LabelFrame(retrieve, text = 'Saved Passwords:', font = ('Segoe UI Light', 11))
    Label(retrieve).grid(row = 0, column = 0)
    with open(find('Password log.txt'), 'r') as pl:
        for line in pl:
            Label(retrieve, text = lineno, font = ('Segoe UI Light', 11)).grid(row = row, column = 0,padx = 5, sticky = W)
            Label(lf, text = line.rstrip(), font = ('Segoe UI Light', 11)).grid(row = row, column = 1, sticky = W)
            row += 1
            lineno += 1
    lf.grid(row = 0, column = 1, rowspan = row + 1, sticky = W)
    Label(retrieve, text = 'So what\'s code do you want?             ', font = ('Segoe UI Light', 11)).grid(row = row + 1, column = 1, pady = (10, 0), sticky = W)
    Label(retrieve, text = 'Line number: ', font = ('Segoe UI Light', 11)).grid(row = row + 2, column = 1, sticky = E)
    global r
    r = ttk.Entry(retrieve, width = 5)
    r.grid(row = row + 2, column = 2, padx = (0, 10), sticky = W)
    Button3 = ttk.Button(retrieve, text='Retrieve', command = retrieve_key).grid(row = row + 4, column = 1, columnspan = 2, padx = (0, 9), sticky = E)


#Main menu
Label(root, text = 'Welcome to version 3 of my Password Generator', font = ('Segoe UI Light', 16)).grid(row = 0, column = 0, columnspan = 3)
Label(
    root,
    text = 
    '''
    With it you can basically, 
    -Create
    -Store
    -Recall
    multiple passwords of up to 256 characters.

    They can then be easily copy-pasted to where they need to be used.
    
    So, what do you want to do?
    ''',
    justify = 'left',
    font = ('Segoe UI Light', 11)
).grid(row = 2, column = 0, columnspan = 3, padx = 10)
Button(root, relief = 'groove', text = 'Retrieve Password', font = ('Segoe UI Light', 11), padx = 30, pady = 20, command = retrieve_key_button).grid(row = 3, column = 0, padx = 10, pady = (0, 10), sticky = W)
Button(root, relief = 'groove', text = 'Create New Password', font = ('Segoe UI Light', 11), padx = 20, pady =20, command = create_password_button).grid(row = 3, column = 2, padx = 10, pady = (0, 10), sticky = E)


#Looping command
root.mainloop()