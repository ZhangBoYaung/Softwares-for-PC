"""
张博洋的项目：鸡兔同笼;
"""

import tkinter as tk
import zipfile
main = tk.Tk()
class Suanji(object):
    def __init__(self,wenben='鸡有多少只🐔'):
        self.wenben=wenben
        tk.Label(main, text=self.wenben, font=('宋体', 20), bg='lightblue').pack()
        self.kuang = tk.Entry(main, font=('黑体', 25))
        self.kuang.pack()
    def du(self):
        ji = int(self.kuang.get())
main['background']='lightblue'
main.geometry('700x700')
main.title('鸡兔同笼2.0')
main.iconbitmap('img/000.ico')
PI = tk.PhotoImage(file='img/000.png')
tupian = tk.Label(main,image=PI,bg='lightblue')
tupian.pack()
biaoti = tk.Label(main,text='鸡兔同笼',font=('楷体',80),bg='lightblue')
biaoti.pack()
wenzi1 = open('txt/text1.txt','r',encoding='utf-8')
shuoming = eval(wenzi1.read())
JI = Suanji()
TU = Suanji(wenben='兔有多少只🐰')
xiaozi = tk.Label(main,text=shuoming,font=('宋体',20),bg='lightblue')
xiaozi.pack()
main.mainloop()