from fileinput import filename
import os
import csv
from tkinter import *
from tkinter import filedialog
from pathlib import Path
#import script1
import script
import tkinter as tk
import threading
import webbrowser
import os
global result 
result = [1,1,1,1,0]

window = Tk()
window.title("Программа для проверки сертификатов сайтов")
window.geometry('960x480')
window.resizable(width=False, height=False)
global count_res
count_res = 0
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
    if (filename != '' and Path(filename).suffix == '.csv'):
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
    access_data = script1.main_script(filename)
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
                script1.save_data(filename)
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
    btn["state"] = DISABLED
    btn2["state"] = DISABLED
    btn3["state"] = DISABLED
    def active_window():
        btn["state"] = ACTIVE
        btn2["state"] = ACTIVE
        btn3["state"] = ACTIVE
        new_window.destroy()
    new_window.protocol("WM_DELETE_WINDOW", lambda: active_window())
    new_window.title("Параметры тестирования")
    new_window.geometry('320x320')
    new_window.resizable(width=False, height=False)
    background2_label = Label(new_window, image=background)
    background2_label.place(x=0, y=0, relwidth=1, relheight=1)
    MenuBttn = Menubutton(new_window, text = "Выбрать", relief = RAISED,state=DISABLED)
    Menu1 = Menu(MenuBttn, tearoff = 0)
    Var1 = IntVar()
    Var2 = IntVar()
    Var3 = IntVar()
    Menu1.add_checkbutton(label = "sha256", variable = Var1)
    Menu1.add_checkbutton(label = "sha1", variable = Var2)
    Menu1.add_checkbutton(label = "md5", variable = Var3)
    MenuBttn["menu"] = Menu1
    MenuBttn.place(x=200, y=140)
    if (os.path.exists("configuration.txt")):
        f = open("configuration.txt", "r")
        result1 = f.readline()
        f.close()
        result1 = result1[1:-1]
        result1 = result1.replace(",", "")
        count = 0
        for i in range(len(result1)):
            if ((result1[i] != " ") and count < 6):
                if (count == 0):
                    if (result1[i] == "1"):
                        result[count] = 1
                    else:
                        result[count] = 0
                    count += 1
                elif (count == 1):
                    if (result1[i] == "1"):
                        result[count] = 1
                    else:
                        result[count] = 0
                    count += 1
                elif (count == 2):
                    if (result1[i] == "1"):
                        result[count] = 1 
                    else:
                        result[count] = 0
                    count += 1
                elif (count == 3):
                    if (result1[i] == "1"):
                        result[count] = 1
                        MenuBttn["state"] = ACTIVE
                    else:
                        result[count] = 0
                        MenuBttn["state"] = DISABLED
                    count += 1
            elif (count == 4):
                value = int(result1[i:])
                result[count] = value
                count += 1
    else:
        value = 0
    var = BooleanVar()
    var1 = BooleanVar()
    var2 = BooleanVar()
    var3 = BooleanVar()
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
            MenuBttn["state"] = ACTIVE
            result[3] = 1
        else:
            result[3] = 0
            MenuBttn["state"] = DISABLED
    def click_scale(val):
            v = int(float(val))
            if (v == 0):
                scale["label"] = f"Истечёт через: не выбрано"
            else:
                scale["label"] = f"Истечёт через: {v} дней"
            result[4] = v
    def click_btn4():
        f = open('configuration.txt', 'w')
        f.write(str(result))
        f.close()
        pcrypto = [0,0,0]
        if (result[3] == 1):
            if (Var1.get() == True):
                pcrypto[0] = 1
            else:
                pcrypto[0] = 0
            if (Var2.get() == True):
                pcrypto[1] = 1
            else:
                pcrypto[1] = 0
            if (Var3.get() == True):
                pcrypto[2] = 1
            else:
                pcrypto[2] = 0
            result[3] = pcrypto
        else:
            result[3] = pcrypto
        print(result)
        active_window()
        btn2["state"] = ACTIVE
        new_window.destroy()
        return result
    cb = Checkbutton(new_window,text="Самоподписанный", variable=var ,command=click_cb)
    cb.place(x=15, y=10)
    if (result[0] == 1):
        cb.select()
    else:
        cb.deselect()
    cb1 = Checkbutton(new_window,text="Истёкший срок действия", variable=var1 ,command=click_cb1)
    cb1.place(x=15, y=60)
    if (result[1] == 1):
        cb1.select()
    else:
        cb1.deselect()
    cb2 = Checkbutton(new_window,text="Длительный срок", variable=var2 ,command=click_cb2)
    cb2.place(x=15, y=110)
    if (result[2] == 1):
        cb2.select()
    else:
        cb2.deselect()
    cb3 = Checkbutton(new_window,text="Шифрование", variable=var3 ,command=click_cb3)
    cb3.place(x=200, y=110)
    if (result[3] == 1):
        cb3.select()
    else:
        cb3.deselect()
    scale = Scale(new_window,width=8,length=305,from_=0, to=397, command=click_scale,orient = HORIZONTAL,label="Истечёт через: не выбрано",relief=FLAT)
    scale.set(value)
    scale.place(x = 5, y = 190)
    btn4 = Button(new_window,width= 25, height= 2, text="Сохранить настройки", relief='flat', command=click_btn4)
    btn4.place(x=70, y = 250)

@thread
def click_btn5():
    global count_res
    if (count_res == 0):
        btn2["text"] = f"Проверка..."
        btn2["state"] = DISABLED
        btn6["state"] = DISABLED
        count_res += 1
        access = script.checker("151.101.193.69", result[0], result[1], result[2], result[3], result[4])
        if (access != ""):
            btn2["text"] = f"Результат"
            btn6["state"] = ACTIVE
            btn2["state"] = ACTIVE
    else:
        btn2["state"] = DISABLED
        btn6["state"] = DISABLED
        if (os.path.exists("result.txt")):
            os.system('result.txt')
            btn2["state"] = ACTIVE
            btn6["state"] = ACTIVE
        else:
            btn2["text"] = f"Начать тестирование"
            btn2["state"] = ACTIVE
            btn6["state"] = DISABLED
            count_res = 0
def click_btn6():
    global count_res
    count_res = 0
    f = open('result.txt', 'w')
    f.close()
    btn2["text"] = f"Начать тестирование"
    btn6["state"] = DISABLED

btn = Button(window,width= 25, height= 5, text="Выбор файла с сайтами",command=click_btn,relief = 'flat') 
btn.grid(column=1, row=1, padx = 70, pady = 300) 
btn2 = Button(window ,width= 25, height= 5, text="Начать тестирование", command=click_btn5,relief = 'flat', state = DISABLED)  
btn2.grid(column=3, row=1, padx = 65, pady = 300)
btn3 = Button(window ,width= 25, height= 5, text="Параметры тестирования", command=click_btn3 ,relief = 'flat')  
btn3.grid(column=2, row=1, padx = 70, pady = 300)
btn6 = Button(window ,width= 10, height= 1, text="cбросить", command=click_btn6 ,relief = 'flat',state=DISABLED)  
btn6.place(x=770,y=390)
window.mainloop()