# -*- coding: utf8 -*-

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image
from PIL import ImageTk
from datetime import datetime
import os

sync = True
delay = 3000
status_bar_height = 50
font_name = 'Arial'
font_size = 36

root = Tk()
root.configure(background='black')
w, h = root.winfo_screenwidth(), root.winfo_screenheight() - status_bar_height

factor_screen = 1.0 * w / h
root.geometry("%dx%d+0+0" % (w, h))
root.overrideredirect(False) # True for macOS
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
#root.focus_set()
#root.bind("<Escape>", lambda e: root.quit())
#root.wm_state('zoomed')

def the_date():
    now = datetime.now()
    MM = str(now.month)
    DD = str(now.day)
    dd = ['월', '화', '수', '목', '금', '토', '일'][datetime.today().weekday()]
    return MM+'월 '+DD+'일('+dd+')'

def the_time():
    now = datetime.now()
    hh = str(now.hour)
    mm = str('%02d'%now.minute)
    return hh+':'+mm

files = os.listdir('.')
im_files = []
for f in files:
    if f.lower().endswith('.jpg') or f.lower().endswith('.png'):
        im_files.append(f)
pic_max = len(im_files)
pic_num = 1
f = im_files.pop(0)
pic = Image.open(f)
pic_w, pic_h = pic.size
factor_pic = 1.0 * pic_w / pic_h
if factor_pic > factor_screen:
    disp_w = w
    disp_h = pic_h * disp_w / pic_w
else:
    disp_h = h
    disp_w = pic_w * disp_h / pic_h
im = ImageTk.PhotoImage(pic.resize((disp_w,disp_h),Image.ANTIALIAS))
label_pic = Label(root, image=im, anchor="center", bg='black')
label_left = Label(root, text=the_date(), font=(font_name, font_size), anchor='w', bg='black', fg='grey')
label_center = Label(root, text=the_time(), font=(font_name, font_size), bg='black', fg='grey')
label_right = Label(root, text=str(pic_num)+'/'+str(pic_max), font=(font_name, font_size), anchor='e', bg='black', fg='grey')
label_pic.place(x=0, y=0, width=w, height=h)
label_left.place(x=0, y=h, width=w/4)
label_center.place(x=w/4, y=h, width=w/2)
label_right.place(x=w*3/4, y=h, width=w/4)

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
        #print(im_files)
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
            if factor_pic > factor_screen:
                disp_w = w
                disp_h = pic_h * disp_w / pic_w
            else:
                disp_h = h
                disp_w = pic_w * disp_h / pic_h
            im = ImageTk.PhotoImage(pic.resize((disp_w,disp_h),Image.ANTIALIAS))
            label_pic.configure(image=im)
            label_pic.image = im
            label_left.configure(text=the_date())
            label_center.configure(text=the_time())
            label_right.configure(text=str(pic_num)+'/'+str(pic_max))
            root.after(delay, im_update)
    except:
        print('file open errer')
        im_update()

root.after(delay, im_update)
root.mainloop()
