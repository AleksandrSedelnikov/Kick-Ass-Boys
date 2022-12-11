from fileinput import filename
from multiprocessing.resource_sharer import stop
from re import A
import os
from tkinter import *
from tkinter import filedialog
from turtle import back, bgcolor
from pathlib import Path
#import script другой файл скрипта, не тот что загрузил Даня
import tkinter as tk
import threading
import webbrowser
import os
from tkinter.filedialog import askopenfilename
#from PIL import Image

window = Tk()
window.title("Программа для проверки сайтов")
window.geometry('960x480')
window.resizable(width=False, height=False)
global background
global src_file
global protocol
global noprotocol
global check_l
global access_data
global name
dir = os.path.abspath(os.curdir)
background = PhotoImage(file = dir + r"\background.png")
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def click_btn():
    global filename
    filename = filedialog.askopenfilename()
    if (filename != '' and Path(filename).suffix == '.txt'):
        btn.configure(bg = 'green', fg= 'white')
        btn["text"] = f"Файл загружен"
        btn2["state"] = ACTIVE
        return filename
    else:
        btn.configure(bg = 'red', fg= 'white')
        btn["text"] = f"Неверный формат файла"
        btn2["state"] = DISABLED
        return ''

def thread(fn):
        def execute(*args, **kwargs):
            threading.Thread(target=fn, args=args, kwargs=kwargs, daemon= True).start()
        return execute

@thread   
def click_btn1():
    btn2["text"] = f"Проверка..."
    btn["state"] = DISABLED
    btn.configure(bg = 'white', fg= 'black')
    btn2["state"] = DISABLED
    access_data = script.main_script(filename)
    protocol = access_data[0][1]
    noprotocol = access_data[0][0]
    if (access_data):
        btn2['text'] = f'Тест завершён'
        second_window = tk.Toplevel(window)
        second_window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
        second_window.title("Результат теста")
        second_window.geometry('960x480')
        second_window.resizable(width=False, height=False)
        background1_label = Label(second_window, image=background)
        background1_label.place(x=0, y=0, relwidth=1, relheight=1)
        def coordinates(x,y):
            if (y == 3):
                script.save_data(filename)
            if (y == 2):
                webbrowser.open('http://' +access_data[1][x], new=0, autoraise=True)
            if (y == 1):
                screenshot = Image.open("img/" + access_data[1][x] + ".png")
                screenshot.show("img/" + access_data[1][x] + ".png")
            if (y == 0):
                print(access_data[2][x])
        #Удачные
        tk1 = tk.Label(second_window,width= 10, height= 1, text="Успешно:", font='Times 11').grid(row = 0, column=0, padx = 0, pady = 5)
        for i in range(protocol):
            tk.Label(second_window,width= 10, height= 1, text=access_data[1][i], font='Times 11').grid(row = i+1, column=0, padx = 15, pady = 5)
            for k in range(3):
                tk.Button(second_window, width= 5, height= 1,text = k+1 ,command=lambda x=i,y=k: coordinates(x,y)).grid(row=i+1,column=k+1, padx = 3, pady = 5)
        k = 0
        #Неудачные
        j = i+1
        tk2 = tk.Label(second_window,width= 10, height= 1, text="Неуспешно:", font='Times 11').grid(row = i+2, column=0, padx = 15, pady = 5)
        for i in range(j,j+noprotocol):
            tk.Label(second_window,width= 10, height= 1, text=access_data[1][i], font='Times 11').grid(row = i+3, column=0, padx = 15, pady = 5)
            for k in range(3):
                tk.Button(second_window, width= 5, height= 1,text = k+1,command=lambda x=i,y=k: coordinates(x,y)).grid(row=i+3,column=k+1, padx = 0, pady = 5)
        tk.Button(second_window, width = 25, height = 5, text= 'Сохранить результат', relief = 'flat',command=lambda x=i+1,y=k+1: coordinates(x,y)).grid(row =i+4,column= k+2, padx = 15, pady= 5)

@thread
def click_btn3():
    new_window = tk.Toplevel(window)
    var = BooleanVar()
    var1 = BooleanVar()
    var2 = BooleanVar()
    var3 = BooleanVar()
    var4 = BooleanVar()
    var5 = BooleanVar()
    var6 = IntVar()
    result = [1,1,1,1,1,1,1]
    new_window.protocol("WM_DELETE_WINDOW", lambda: new_window.destroy())
    new_window.title("Тестовое окно")
    new_window.geometry('320x320')
    new_window.resizable(width=False, height=False)
    background2_label = Label(new_window, image=background)
    background2_label.place(x=0, y=0, relwidth=1, relheight=1)
    def click_cb():
        if var.get():
            result[0] = 1
        else:
            result[0] = 0
    def click_cb1():
        if var1.get():
            result[1] = 1
        else:
            result[1] = 0
    def click_cb2():
        if var2.get():
            result[2] = 1
        else:
            result[2] = 0
    def click_cb3():
        if var3.get():
            result[3] = 1
        else:
            result[3] = 0
    def click_cb4():
        if var4.get():
            result[4] = 1
        else:
            result[4] = 0
    def click_cb5():
        if var5.get():
            result[5] = 1
        else:
            result[5] = 0
    def click_scale(val):
        v = int(float(val))
        result[6] = v
    def click_btn4():
        print(result)
    cb = Checkbutton(new_window,text="Параметр 1", variable=var ,command=click_cb)
    cb.select()
    cb.place(x=50, y=10)
    cb1 = Checkbutton(new_window,text="Параметр 2", variable=var1 ,command=click_cb1)
    cb1.select()
    cb1.place(x=50, y=60)
    cb2 = Checkbutton(new_window,text="Параметр 3", variable=var2 ,command=click_cb2)
    cb2.select()
    cb2.place(x=50, y=110)
    cb3 = Checkbutton(new_window,text="Параметр 4", variable=var3 ,command=click_cb3)
    cb3.select()
    cb3.place(x=50, y=160)
    cb4 = Checkbutton(new_window,text="Параметр 5", variable=var4 ,command=click_cb4)
    cb4.select()
    cb4.place(x=50, y=210)
    cb5 = Checkbutton(new_window,text="Параметр 6", variable=var5 ,command=click_cb5)
    cb5.select()
    cb5.place(x=160, y=10)
    scale = Scale(new_window,from_=0, to=1000, command=click_scale)
    scale.place(x = 210, y = 60)
    btn4 = Button(new_window,width= 25, height= 2, text="Сохранить настройки", relief='flat', command=click_btn4)
    btn4.place(x=80, y = 250)
    return 0

btn = Button(window,width= 25, height= 5, text="Выбор файла с сайтами",command=click_btn,relief = 'flat') 
btn.grid(column=1, row=1, padx = 70, pady = 300) 
btn2 = Button(window ,width= 25, height= 5, text="Начать тестирование",state = DISABLED, command=click_btn1,relief = 'flat')  
btn2.grid(column=3, row=1, padx = 65, pady = 300)
btn3 = Button(window ,width= 25, height= 5, text="Тест", command=click_btn3 ,relief = 'flat')  
btn3.grid(column=2, row=1, padx = 70, pady = 300)
window.mainloop()