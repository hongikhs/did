# -*- coding: utf8 -*-

from Tkinter import *
from PIL import Image
from PIL import ImageTk
import os

sync = False
delay = 3000

root = Tk()
root.configure(background='black')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()-25
factor_screen = 1.0 * w / h
root.overrideredirect(True)
root.geometry("%dx%d+0+0" % (w, h))
root.attributes('-fullscreen', True)
#root.attributes('-topmost', True)
#root.focus_set()
#root.bind("<Escape>", lambda e: root.quit())
#root.wm_state('zoomed')

#os.system('rclone sync hongikdid: ~/did')
files = os.listdir('.')
im_files = []
for f in files:
    if f.lower().endswith('.jpg') or f.lower().endswith('.png'):
        im_files.append(f)
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
la = Label(root, image=im, anchor="center", bg='black')
lb = Label(root, text='홍대부고 SW교육봉사 동아리', anchor="s")
la.pack()
lb.pack()

def im_update():
    global im_files
    if sync:
        os.system('rclone sync hongikdid: ~/did')
    if len(im_files) == 0:
        files = os.listdir('.')
        for f in files:
            if f.lower().endswith('.jpg') or f.lower().endswith('.png') or f.lower().endswith('.mp4') or f.lower().endswith('.mkv') or f.lower().endswith('.avi'):
                im_files.append(f)
        print(im_files)
    try:
        f = im_files.pop(0)
        print(f, len(im_files))
        if f.lower().endswith('.mp4'):
            os.system('omxplayer -b ' + f)
            root.after(0, im_update)
        else:
            pic = Image.open(f)
            pic_w, pic_h = pic.size
            factor_pic = 1.0 * pic_w / pic_h
            print(f, pic.size, factor_pic)
            if factor_pic > factor_screen:
                disp_w = w
                disp_h = pic_h * disp_w / pic_w
                margin_h = (h - disp_h) / 2.0
            else:
                disp_h = h
                disp_w = pic_w * disp_h / pic_h
                margin_h = 0
            im = ImageTk.PhotoImage(pic.resize((disp_w,disp_h),Image.ANTIALIAS))
            la.configure(image=im)
            la.image = im
            root.after(delay, im_update)
    except:
        print('file open errer')
        im_update()

root.after(delay, im_update)
root.mainloop()
