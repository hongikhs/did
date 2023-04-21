# -*- coding: utf8 -*-

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image
from PIL import ImageTk
from datetime import datetime
import sys, os
import time

root = Tk()

### 설정값 ###

root.configure(background='black')

sync = True             # rclone 싱크 여부
delay_default = 2000    # 그림 바꾸는 간격(ms)
stretch = False         # 화면에 맞게 그림 늘이기
font_name = 'Arial'

### 함수부 ###

def the_date():
    now = datetime.now()
    YYYY = str(now.year)
    MM = str(now.month)
    DD = str(now.day)
    dd = ['월', '화', '수', '목', '금', '토', '일'][datetime.today().weekday()]
    return MM+'.'+DD+'.('+dd+')'

def the_time():
    now = datetime.now()
    hh = str(now.hour)
    mm = str('%02d'%now.minute)
    return hh+':'+mm

def im_update():
    global im_files
    global pic_max, pic_num
    
    if sync:
        os.system('rclone sync hongikdid: ~/did')
    if len(im_files) == 0:
        files = os.listdir('.')
        for f in files:
            if f.lower().endswith('.jpg') or f.lower().endswith('.png') or f.lower().endswith('.mp4') or f.lower().endswith('.mkv') or f.lower().endswith('.avi'):
                im_files.append(f)
        im_files.sort()
        print(im_files)
        pic_max = len(im_files)
        pic_num = 0
    try:
        f = im_files.pop(0)
        pic_num += 1
        print(f, len(im_files))
        if f.lower().endswith('.mp4'):
            os.system('omxplayer -b ' + f)
            root.after(0, im_update)
        else:
            pic = Image.open(f)
            pic_w, pic_h = pic.size
            factor_pic = 1.0 * pic_w / pic_h
            #print(f, pic.size, factor_pic)
            if stretch :
                im = ImageTk.PhotoImage(pic.resize((w,h),Image.ANTIALIAS))
            else :
                if factor_pic > factor_screen:
                    disp_w = w
                    disp_h = int(pic_h * disp_w / pic_w)
                else:
                    disp_h = oh
                    disp_w = int(pic_w * disp_h / pic_h)
                im = ImageTk.PhotoImage(pic.resize((disp_w,disp_h),Image.ANTIALIAS))
            label_pic.configure(image=im)
            label_pic.image = im
            label_left.configure(text=the_date()+' '+the_time())
            label_right.configure(text=str(pic_num)+'/'+str(pic_max))
            if f[0] == '[' and f[2] == ']' :
                delay = int(f[1]) * 1000
            else :
                delay = delay_default
            root.after(delay, im_update)         
    except:
        print('file open errer')
        im_update()

### 여기부터 시작 ###

status_bar_height = int(root.winfo_screenheight() / 30)
font_size = int(status_bar_height * 2 / 3)
font_color = 'white'

ow, oh = root.winfo_screenwidth(), root.winfo_screenheight()
w, h = ow, oh - status_bar_height

factor_screen = 1.0 * w / h
root.geometry("%dx%d+0+0" % (w, h))
root.overrideredirect(False) # True for macOS
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)

delay = delay_default
im_files = []

pic_max=0
pic_num=0

label_pic = Label(root, anchor="center", bg='black')
label_left = Label(root, text=the_date()+' '+the_time(), font=(font_name, font_size), anchor='w', bg='black', fg=font_color)
label_right = Label(root, text=str(pic_num)+'/'+str(pic_max), font=(font_name, font_size), anchor='e', bg='black', fg=font_color)

label_pic.place(x=0, y=0, width=w, height=oh)
label_left.place(x=0, y=h, width=w*1/8)
label_right.place(x=w*15/16, y=h, width=w/16)

root.after(delay, im_update)
root.mainloop()