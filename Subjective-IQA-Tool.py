import tkinter as tk
from PIL import Image, ImageTk
import os

FilePath = './example_image'

PngList = os.listdir(FilePath)


def show(event):
    s = 'Value of the slider' + str(var.get())
    lb.config(text=s)
    enTextJumNum.delete(0.0, tk.END)
    enTextJumNum.insert(tk.INSERT, str(nIndex))

    enTextDiscuss.delete(0.0, tk.END)
    strDiscuss = PngList[nIndex - 1].split('.')[0] + ".png" + ":" + str(var.get())
    enTextDiscuss.insert(tk.INSERT, strDiscuss)


def Writediscuss(strdiscuss):
    f = open("./result/score.txt", 'a', encoding='utf8')
    f.write(strdiscuss)
    f.close()


def resize(nX, nY):
    xNew = 1920
    yNew = 1080
    return (xNew, yNew)


root = tk.Tk()
root.geometry('2560x1440')
root.title('Subjective-IQA-tool')

img = Image.open('./welcome.jpg')
img = img.resize((1800, 450))
photo = ImageTk.PhotoImage(img)
imglabel = tk.Label(root, image=photo)
imglabel.place(x=300, y=150)

nIndex = 0


def submit():
    global nIndex
    enTextJumNum.delete(0.0, tk.END)
    enTextJumNum.insert(tk.INSERT, str(nIndex))

    enTextDiscuss.delete(0.0, tk.END)
    strDiscuss = PngList[nIndex].split('.')[0] + ".png" + ":"
    enTextDiscuss.insert(tk.INSERT, strDiscuss)

    print(PngList[nIndex])

    strPng = FilePath + '\\' + PngList[nIndex]

    global photo
    global imglabel
    photo = ImageTk.PhotoImage(file=strPng)
    photoNew = Image.open(strPng).resize(resize(photo.width(), photo.height()))
    photo = ImageTk.PhotoImage(photoNew)
    imglabel.config(image=photo)
    nIndex = nIndex + 1


def jumpTo():
    global nIndex
    nIndex = int(enTextJumNum.get('0.0', 'end'))
    print(nIndex)
    submit()


# 上一个
def pre():
    global nIndex
    nIndex = nIndex - 2
    print(nIndex)
    submit()


# 上一个
def home():
    global nIndex
    nIndex = 0
    print(nIndex)
    submit()


# 写入评分
def writeDiscuss():
    strDiscuss = enTextDiscuss.get('0.0', 'end')

    Writediscuss(strDiscuss)


def onEventNext(e):
    submit()


def onEventPre(e):
    pre()


var = tk.DoubleVar()
scl = tk.Scale(root, orient=tk.HORIZONTAL, length=1000,
               from_=0, to=100, label='please drag', tickinterval=10, resolution=0.1, variable=var)

scl.bind('<ButtonRelease-1>', show)
scl.pack()
lb = tk.Label(root, text='')
lb.pack()

enTextJumNum = tk.Text(root)
enTextJumNum.place(x=2380, y=270, height=50, width=125)
enTextJumNum.insert(tk.INSERT, '0')

btnjump = tk.Button(root, text="Dump and count", command=jumpTo)
btnjump.place(x=2250, y=270, height=50, width=120)

btnNext = tk.Button(root, text="Next image", command=submit)
btnNext.place(x=1950, y=20, height=50, width=100)

btnPre = tk.Button(root, text="Previous image", command=pre)
btnPre.place(x=1825, y=20, height=50, width=100)

btnPre = tk.Button(root, text="Begin Test", command=home)
btnPre.place(x=2250, y=100, height=100, width=270)

enTextDiscuss = tk.Text(root)
enTextDiscuss.place(x=1825, y=80, height=50, width=300)
enTextDiscuss.insert(tk.INSERT, 'Score:')

btnDiscuss = tk.Button(root, text="Submit", command=writeDiscuss)
btnDiscuss.place(x=2100, y=20, height=50, width=100)

tk.mainloop()
