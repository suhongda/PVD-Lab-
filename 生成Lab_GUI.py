from tkinter import *
from tkinter.ttk import *
import numpy as np
import random

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

from matplotlib.figure import Figure

#from 生成Lab import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_frame_箱形图容器 = Frame_箱形图容器(self)
        self.tk_label_frame_L参数容器 = Frame_L参数容器(self)
        self.tk_label_frame_a参数容器 = Frame_a参数容器(self)
        self.tk_label_frame_b参数容器 = Frame_b参数容器(self)

    def __win(self):
        self.title("Lab生成")
        # 设置窗口大小、居中
        width = 700
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

class Frame_箱形图容器(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_图 = self.__tk_图()

    def __frame(self):
        self.place(x=10, y=400, width=680, height=195)

    def __tk_图(self):
        f = Figure(dpi=100)
        a = f.add_subplot(111)
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        return a

class Frame_L参数容器(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_L_层均值标签 = self.__tk_label_L_层均值标签()
        self.tk_input_L_层均值输入框 = self.__tk_input_L_层均值输入框()
        self.tk_button_L确定按钮 = self.__tk_button_L确定按钮()
        self.tk_label_最值差标签 = self.__tk_label_最值差标签()
        self.tk_input_均值差输入 = self.__tk_input_均值差输入()
        self.tk_input_中值差输入 = self.__tk_input_中值差输入()
        self.tk_input_最值差输入 = self.__tk_input_最值差输入()
        self.tk_label_均值差标签 = self.__tk_label_均值差标签()
        self.tk_label_中值差标签 = self.__tk_label_中值差标签()
        self.tk_input_小1输入 = self.__tk_input_小1输入()
        self.tk_input_大2输入 = self.__tk_input_大2输入()
        self.tk_label_小1标签 = self.__tk_label_小1标签()
        self.tk_label_大2标签 = self.__tk_label_大2标签()
        self.tk_label_小2标签 = self.__tk_label_小2标签()
        self.tk_label_大1标签 = self.__tk_label_大1标签()
        self.tk_input_大1输入 = self.__tk_input_大1输入()
        self.tk_input_小2输入 = self.__tk_input_小2输入()
        self.tk_label_每层数标签 = self.__tk_label_每层数标签()
        self.tk_input_每层数输入 = self.__tk_input_每层数输入()

    def __frame(self):
        self.configure(text="L")
        self.place(x=10, y=5, width=220, height=390)

    def __tk_label_L_层均值标签(self):
        label = Label(self, text="层\n均\n值")
        label.place(x=20, y=0, width=30, height=200)
        return label

    def __tk_label_小1标签(self):
        label = Label(self, text="小1")
        label.place(x=10, y=204, width=30, height=24)
        return label

    def __tk_label_小2标签(self):
        label = Label(self, text="小2")
        label.place(x=185, y=204, width=30, height=24)
        return label

    def __tk_label_大2标签(self):
        label = Label(self, text="大2")
        label.place(x=10, y=230, width=30, height=24)
        return label

    def __tk_label_大1标签(self):
        label = Label(self, text="大1")
        label.place(x=185, y=230, width=30, height=24)
        return label

    def __tk_label_最值差标签(self):
        label = Label(self, text="最值差")
        label.place(x=5, y=260, width=45, height=24)
        return label

    def __tk_label_均值差标签(self):
        label = Label(self, text="均值差")
        label.place(x=5, y=290, width=45, height=24)
        return label

    def __tk_label_中值差标签(self):
        label = Label(self, text="中值差")
        label.place(x=5, y=320, width=45, height=24)
        return label

    def __tk_label_每层数标签(self):
        label = Label(self, text="每层数")
        label.place(x=168, y=290, width=45, height=24)
        return label

    def __tk_button_L确定按钮(self):
        btn = Button(self, text="确定")
        btn.place(x=10, y=345, width=200, height=24)
        return btn

   #        ——————输入——————

    def __tk_input_L_层均值输入框(self):
        ipt = Text(self)
        ipt.place(x=50, y=0, width=150, height=200)
        return ipt

    def __tk_input_小1输入(self):
        ipt = Entry(self)
        ipt.place(x=36, y=207, width=70, height=20)
        ipt.insert(0, '-0.6')
        return ipt

    def __tk_input_小2输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=207, width=70, height=20)
        ipt.insert(0, '-0.4')
        return ipt

    def __tk_input_大2输入(self):
        ipt = Entry(self)
        ipt.place(x=36, y=233, width=70, height=20)
        ipt.insert(0, '0.4')
        return ipt

    def __tk_input_大1输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=233, width=70, height=20)
        ipt.insert(0, '0.5')
        return ipt

    def __tk_input_最值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=260, width=55, height=24)
        ipt.insert(0, '0.75')
        return ipt

    def __tk_input_均值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=290, width=55, height=24)
        ipt.insert(0, '0.02')
        return ipt

    def __tk_input_中值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=320, width=55, height=24)
        ipt.insert(0, '0.01')
        return ipt

    def __tk_input_每层数输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=290, width=55, height=24)
        ipt.insert(0, '10')
        return ipt

class Frame_a参数容器(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_a_层均值标签 = self.__tk_label_a_层均值标签()
        self.tk_input_a_层均值输入框 = self.__tk_input_a_层均值输入框()
        self.tk_button_a确定按钮 = self.__tk_button_a确定按钮()
        self.tk_label_最值差标签 = self.__tk_label_最值差标签()
        self.tk_input_均值差输入 = self.__tk_input_均值差输入()
        self.tk_input_中值差输入 = self.__tk_input_中值差输入()
        self.tk_input_最值差输入 = self.__tk_input_最值差输入()
        self.tk_label_均值差标签 = self.__tk_label_均值差标签()
        self.tk_label_中值差标签 = self.__tk_label_中值差标签()
        self.tk_input_小1输入 = self.__tk_input_小1输入()
        self.tk_input_大2输入 = self.__tk_input_大2输入()
        self.tk_label_小1标签 = self.__tk_label_小1标签()
        self.tk_label_大2标签 = self.__tk_label_大2标签()
        self.tk_label_小2标签 = self.__tk_label_小2标签()
        self.tk_label_大1标签 = self.__tk_label_大1标签()
        self.tk_input_大1输入 = self.__tk_input_大1输入()
        self.tk_input_小2输入 = self.__tk_input_小2输入()
        self.tk_label_每层数标签 = self.__tk_label_每层数标签()
        self.tk_input_每层数输入 = self.__tk_input_每层数输入()

    def __frame(self):
        self.configure(text="a")
        self.place(x=240, y=5, width=220, height=390)

    def __tk_label_a_层均值标签(self):
        label = Label(self, text="层\n均\n值")
        label.place(x=20, y=0, width=30, height=200)
        return label

    def __tk_label_小1标签(self):
        label = Label(self, text="小1")
        label.place(x=10, y=204, width=30, height=24)
        return label

    def __tk_label_小2标签(self):
        label = Label(self, text="小2")
        label.place(x=185, y=204, width=30, height=24)
        return label

    def __tk_label_大2标签(self):
        label = Label(self, text="大2")
        label.place(x=10, y=230, width=30, height=24)
        return label

    def __tk_label_大1标签(self):
        label = Label(self, text="大1")
        label.place(x=185, y=230, width=30, height=24)
        return label

    def __tk_label_最值差标签(self):
        label = Label(self, text="最值差")
        label.place(x=5, y=260, width=45, height=24)
        return label

    def __tk_label_均值差标签(self):
        label = Label(self, text="均值差")
        label.place(x=5, y=290, width=45, height=24)
        return label

    def __tk_label_中值差标签(self):
        label = Label(self, text="中值差")
        label.place(x=5, y=320, width=45, height=24)
        return label

    def __tk_label_每层数标签(self):
        label = Label(self, text="每层数")
        label.place(x=168, y=290, width=45, height=24)
        return label

    def __tk_button_a确定按钮(self):
        btn = Button(self, text="确定")
        btn.place(x=10, y=345, width=200, height=24)
        return btn

   #        ——————输入——————

    def __tk_input_a_层均值输入框(self):
        ipt = Text(self)
        ipt.place(x=50, y=0, width=150, height=200)
        return ipt

    def __tk_input_小1输入(self):
        ipt = Entry(self)
        ipt.place(x=36, y=207, width=70, height=20)
        ipt.insert(0, '-0.06')
        return ipt

    def __tk_input_小2输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=207, width=70, height=20)
        ipt.insert(0, '-0.04')
        return ipt

    def __tk_input_大2输入(self):
        ipt = Entry(self)
        ipt.place(x=36, y=233, width=70, height=20)
        ipt.insert(0, '0.04')
        return ipt

    def __tk_input_大1输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=233, width=70, height=20)
        ipt.insert(0, '0.05')
        return ipt

    def __tk_input_最值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=260, width=55, height=24)
        ipt.insert(0, '0.075')
        return ipt

    def __tk_input_均值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=290, width=55, height=24)
        ipt.insert(0, '0.02')
        return ipt

    def __tk_input_中值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=320, width=55, height=24)
        ipt.insert(0, '0.01')
        return ipt

    def __tk_input_每层数输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=290, width=55, height=24)
        ipt.insert(0, '10')
        return ipt

class Frame_b参数容器(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_b_层均值标签 = self.__tk_label_b_层均值标签()
        self.tk_input_b_层均值输入框 = self.__tk_input_b_层均值输入框()
        self.tk_button_b确定按钮 = self.__tk_button_b确定按钮()
        self.tk_label_最值差标签 = self.__tk_label_最值差标签()
        self.tk_input_均值差输入 = self.__tk_input_均值差输入()
        self.tk_input_中值差输入 = self.__tk_input_中值差输入()
        self.tk_input_最值差输入 = self.__tk_input_最值差输入()
        self.tk_label_均值差标签 = self.__tk_label_均值差标签()
        self.tk_label_中值差标签 = self.__tk_label_中值差标签()
        self.tk_input_小1输入 = self.__tk_input_小1输入()
        self.tk_input_大2输入 = self.__tk_input_大2输入()
        self.tk_label_小1标签 = self.__tk_label_小1标签()
        self.tk_label_大2标签 = self.__tk_label_大2标签()
        self.tk_label_小2标签 = self.__tk_label_小2标签()
        self.tk_label_大1标签 = self.__tk_label_大1标签()
        self.tk_input_大1输入 = self.__tk_input_大1输入()
        self.tk_input_小2输入 = self.__tk_input_小2输入()
        self.tk_label_每层数标签 = self.__tk_label_每层数标签()
        self.tk_input_每层数输入 = self.__tk_input_每层数输入()

    def __frame(self):
        self.configure(text="b")
        self.place(x=470, y=5, width=220, height=390)

    def __tk_label_b_层均值标签(self):
        label = Label(self, text="层\n均\n值")
        label.place(x=20, y=5, width=30, height=200)
        return label

    def __tk_label_小1标签(self):
        label = Label(self, text="小1")
        label.place(x=10, y=204, width=30, height=24)
        return label

    def __tk_label_小2标签(self):
        label = Label(self, text="小2")
        label.place(x=185, y=204, width=30, height=24)
        return label

    def __tk_label_大2标签(self):
        label = Label(self, text="大2")
        label.place(x=10, y=230, width=30, height=24)
        return label

    def __tk_label_大1标签(self):
        label = Label(self, text="大1")
        label.place(x=185, y=230, width=30, height=24)
        return label

    def __tk_label_最值差标签(self):
        label = Label(self, text="最值差")
        label.place(x=5, y=260, width=45, height=24)
        return label

    def __tk_label_均值差标签(self):
        label = Label(self, text="均值差")
        label.place(x=5, y=290, width=45, height=24)
        return label

    def __tk_label_中值差标签(self):
        label = Label(self, text="中值差")
        label.place(x=5, y=320, width=45, height=24)
        return label

    def __tk_label_每层数标签(self):
        label = Label(self, text="每层数")
        label.place(x=168, y=290, width=45, height=24)
        return label

    def __tk_button_b确定按钮(self):
        btn = Button(self, text="确定")
        btn.place(x=10, y=345, width=200, height=24)
        return btn

   #        ——————输入——————

    def __tk_input_b_层均值输入框(self):
        ipt = Text(self)
        ipt.place(x=50, y=0, width=150, height=200)
        return ipt

    def __tk_input_小1输入(self):
        ipt = Entry(self)
        ipt.place(x=36, y=207, width=70, height=20)
        ipt.insert(0, '-0.5')
        return ipt

    def __tk_input_小2输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=207, width=70, height=20)
        ipt.insert(0, '-0.4')
        return ipt

    def __tk_input_大2输入(self):
        ipt = Entry(self)
        ipt.place(x=36, y=233, width=70, height=20)
        ipt.insert(0, '0.2')
        return ipt

    def __tk_input_大1输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=233, width=70, height=20)
        ipt.insert(0, '0.4')
        return ipt

    def __tk_input_最值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=260, width=55, height=24)
        ipt.insert(0, '0.55')
        return ipt

    def __tk_input_均值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=290, width=55, height=24)
        ipt.insert(0, '0.02')
        return ipt

    def __tk_input_中值差输入(self):
        ipt = Entry(self)
        ipt.place(x=50, y=320, width=55, height=24)
        ipt.insert(0, '0.01')
        return ipt

    def __tk_input_每层数输入(self):
        ipt = Entry(self)
        ipt.place(x=110, y=290, width=55, height=24)
        ipt.insert(0, '10')
        return ipt

# 层均值处理
def meanValueProcessing (data, character):    # 层均值处理
    x=data.get('0.0', 'end')
    character=str(character)
    with open(character, 'w') as f:
        f.write(x)
    y = list(np.loadtxt(character))
    return y

# 参数处理
def parameterProcessing(data):               # 参数处理
    x1 = float(data.tk_input_小1输入.get())
    x2 = float(data.tk_input_小2输入.get())
    x3 = float(data.tk_input_大2输入.get())
    x4 = float(data.tk_input_大1输入.get())
    x5 = float(data.tk_input_最值差输入.get())
    x6 = float(data.tk_input_均值差输入.get())
    x7 = float(data.tk_input_中值差输入.get())
    x8 = float(data.tk_input_每层数输入.get())
    return [x1, x2, x3, x4, x5, x6, x7, x8]

#中位数
def get_median(data):           #中位数
   data = sorted(data)
   size = len(data)
   if size % 2 == 0: # 判断列表长度为偶数
    median = (data[size//2]+data[size//2-1])/2
    data[0] = median
   if size % 2 == 1: # 判断列表长度为奇数
    median = data[(size-1)//2]
    data[0] = median
   return data[0]

def maximum (x1, x2, x3, x4, data):        # 范围
    i=1
    d_min = random.uniform(x1, x2) + data
    d_max = random.uniform(x3, x4) + data
    return [d_min,d_max]            # L范围

def generate_bata (data,最小=0.0, 最大=0.0, 最值差=0.0, 均值差=0.0, 中值差=0.0, 每层个数=0.0):
    i=1
    倍数 = 1000
    d1=[]
    while i == 1:
        d1 = np.random.randint(最小 * 倍数, 最大 * 倍数, int(每层个数)) / 倍数
        csxx = abs(min(d1) - max(d1))  # 最值差
        css = abs(data - np.mean(d1))  # 平均值比较
        median1 = abs(data - get_median(d1))  # 中值比较
        # print('最值差',csxx,'平均值比较',css,'中值比较',median1)
        if csxx > 最值差:
            # print('最值差', csxx)
            if css < 均值差:
                if median1 < 中值差:
                    i = 0
    return d1

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def colour_L(self, evt):
        L_层均值=meanValueProcessing(self.tk_label_frame_L参数容器.tk_input_L_层均值输入框, 'L_层均值')    # 层均值处理
        n层数=len(L_层均值)
        l=parameterProcessing(self.tk_label_frame_L参数容器)       # 参数处理
        L_范围_小1 =l[0]
        L_范围_小2 =l[1]
        L_范围_大2 =l[2]
        L_范围_大1 =l[3]
        #print(L_范围_小1,L_范围_小2,L_范围_大2,L_范围_大1)
        L_最值差 =l[4]
        L_均值差 =l[5]
        L_中值差 =l[6]
        #print(L_最值差,L_均值差,L_中值差)
        L_每层个数 = l[7]
        D1 = []   # 用于Excel保存
        D2 = []   # 用于箱形图
        D3 = []   # 生成数据的均值
        for dX in L_层均值 :
            range = maximum(L_范围_小1, L_范围_小2, L_范围_大2, L_范围_大1, dX)    # 生成范围
            bataa = generate_bata(dX, 最小=range[0], 最大=range[1],
                                  最值差=L_最值差, 均值差=L_均值差, 中值差=L_中值差,
                                  每层个数=L_每层个数)  # 生成数据
            D1 = np.hstack((D1, bataa))  # 合并
            D3 = np.hstack((D3, np.mean(bataa)))
            if dX == L_层均值[0]:
                D2 = bataa
            else:
                D2 = np.vstack((D2, bataa))
        #print(D2)
        ceng=list(np.arange(1, n层数 + 1, 1))
        gif图=Frame_箱形图容器(self).tk_图
        gif图.plot(ceng, D3)           # 均值连线
        gif图.boxplot(list(D2))        # 箱形图数据集
        gif图.set_xticklabels(ceng)    # 箱形图标签



    def colour_a(self, evt):
        a_层均值=meanValueProcessing(self.tk_label_frame_a参数容器.tk_input_a_层均值输入框, 'a_层均值')    # 层均值处理
        a=parameterProcessing(self.tk_label_frame_a参数容器)       # 参数处理
        print(a_层均值,a)
        a_范围_小1 =a[0]
        a_范围_小2 =a[1]
        a_范围_大2 =a[2]
        a_范围_大1 =a[3]
        a_最值差 =a[4]
        a_均值差 =a[5]
        a_中值差 =a[6]
        a_每层个数 = a[7]


    def colour_b(self, evt):
        b_层均值=meanValueProcessing(self.tk_label_frame_b参数容器.tk_input_b_层均值输入框, 'b_层均值')    # 层均值处理
        b=parameterProcessing(self.tk_label_frame_b参数容器)       # 参数处理
        print(b_层均值,b)
        b_范围_小1 =b[0]
        b_范围_小2 =b[1]
        b_范围_大2 =b[2]
        b_范围_大1 =b[3]
        b_最值差 =b[4]
        b_均值差 =b[5]
        b_中值差 =b[6]
        b_每层个数 = b[7]


    def __event_bind(self):
        self.tk_label_frame_L参数容器.tk_button_L确定按钮.bind('<Button>', self.colour_L)
        self.tk_label_frame_a参数容器.tk_button_a确定按钮.bind('<Button>', self.colour_a)
        self.tk_label_frame_b参数容器.tk_button_b确定按钮.bind('<Button>', self.colour_b)


if __name__ == "__main__":
    win = Win()
    win.mainloop()

