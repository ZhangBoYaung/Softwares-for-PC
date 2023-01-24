import tkinter

def qingkong(*x):
    for xx in x:
        xx.kuang.delete(0,tkinter.END)

def cuozi(*x):
    for xx in x:
        xx.kuang.insert(0,shuoming[1])

class Suanji(object):
    def __init__(self,wenben='鸡有多少只',ji=True,tou=True):
        self.tou=tou
        self.ji=ji
        self.wenben=wenben
        tkinter.Label(kj_jttl, text=self.wenben, font=('宋体', 30)).pack()
        self.kuang = tkinter.Entry(kj_jttl, font=('黑体', 25))
        self.kuang.pack()
    def du(self):
        shumu = int(self.kuang.get())
        return shumu
    def xiugai(self):
        self.kuang.delete(0,tkinter.END)
        list1 = ji_tu()
        if self.ji:
            self.kuang.insert(0,list1['ji'])
        else:
            self.kuang.insert(0,list1['tu'])
    def touhetui(self):
        list1 = tou_tui()
        self.kuang.delete(0,tkinter.END)
        if self.tou:
            self.kuang.insert(0,list1['tou'])
        else:
            self.kuang.insert(0,list1['tui'])

def baocuo():
    qingkong(JI,TU,Tou,Tui)
    cuozi(JI,TU,Tou,Tui)

def tou_tui():
    x = JI.du()
    y = TU.du()
    if 0 <= x == int(x) and 0 <= y == int(y):
        x=int(x)
        y=int(y)
    else:
        baocuo()
    list1 = {'tou':x+y,'tui':x*2+y*4}
    return list1

def ji_tu():
    x = Tou.du()
    y = Tui.du()
    tu = (y-2*x)/2
    ji = x -tu
    if int(tu)== tu >=0  and int(ji)==ji >= 0 :
        tu=int(tu)
        ji=int(ji)
    else:
        baocuo()
    list1 = {'ji':ji,'tu':tu}
    return list1

def jisuan():
    try:
        JI.xiugai()
        TU.xiugai()
    except:
        baocuo()

def suanji():
    try:
        Tou.touhetui()
        Tui.touhetui()
    except:
        baocuo()

def an(a,t,f,c):
    return tkinter.Button(a,text=t,font=('Times',f),command=c)


class Anniu(object):
    def anxia_fanhui(self):
        kj1.pack()
        fhan.place_forget()
        kj_jttl.pack_forget()

    def anxia1(self):
        kjsc()
        kj1.pack_forget()
        fanhui()
        global JI,TU,Tou,Tui,shuoming
        ck.title('鸡兔同笼_鸡兔同笼问题')
        wenzi1 = open('txt/text1.txt', 'r', encoding='utf-8')
        shuoming = eval(wenzi1.read())
        JI = Suanji()
        TU = Suanji(wenben='兔有多少只', ji=False)
        anniu = tkinter.Button(kj_jttl, text='计算头和腿', command=suanji)
        anniu.pack()
        Tou = Suanji(wenben='头有多少颗')
        Tui = Suanji(wenben='腿有多少条', tou=False)
        anniu2 = tkinter.Button(kj_jttl, text='计算鸡和兔', command=jisuan)
        anniu2.pack()

    def anxia2(self):
        ...

def main():
    global anniu1 , anniu2
    anniu1 = an(kj1, '鸡兔同笼问题', 20, anniu.anxia1)
    anniu1.pack()
    anniu2 = an(kj1,'唐僧取经问题',20,anniu.anxia2)
    anniu2.pack()

def kjsc():
    global kj_jttl
    kj_jttl = tkinter.Frame(ck)
    kj_jttl.pack()

def fanhui():
    global fhan
    fhan = an(ck,'返回',20,anniu.anxia_fanhui)
    fhan.place(x=30,y=40,anchor='nw')

anniu = Anniu()
ck = tkinter.Tk()
kj_jttl = None
JI = TU = Tou = Tui = shuoming = None
anniu1 = anniu2 = fhan =  None
ck.geometry('700x700')
ck.iconbitmap('img/000.ico')
tpwj = tkinter.PhotoImage(file='img/000.png')
tp1 = tkinter.Label(ck,image=tpwj)
tp1.pack()
kj1 = tkinter.Frame(ck)
kj1.pack()
main()
ck.mainloop()