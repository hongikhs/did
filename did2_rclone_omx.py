from Tkinter import *
from PIL import Image
from PIL import ImageTk
import os

delay = 3000
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(True)
root.geometry("%dx%d+0+0" % (w, h))
#root.focus_set()
#root.bind("<Escape>", lambda e: root.quit())
root.attributes('-fullscreen', True)
#root.attributes('-topmost', True)
#root.wm_state('zoomed')
#root.configure(background='black')

os.system('rclone sync hongikdid: ~/did')
files = os.listdir('.')
im_files = []
for f in files:
    if f.lower.endswith('.jpg') or f.lower.endswith('.png'):
        im_files.append(f)
#print(im_files)
im = ImageTk.PhotoImage(Image.open(im_files.pop(0)).resize((w,h-50),Image.ANTIALIAS))
la = Label(root, image=im, bg='black')
lb = label(root, text = '홍대부고 SW교육봉사 동아리')
la.pack()       
lb.pack()

def im_update():
    global im_files
    os.system('rclone sync hongikdid: ~/did')
    if len(im_files) == 0:
        files = os.listdir('.')
        for f in files:
            if f.lower.endswith('.jpg') or f.lower.endswith('.png') or f.lower.endswith('.mp4') or f.lower.endswith('.mkv') or f.lower.endswith('.avi'):
                im_files.append(f)
        print(im_files)
    try:
        f = im_files.pop(0)
        if f.endswith('.mp4'):
            os.system('omxplayer -b ' + f)
            root.after(0, im_update)
        else:
            im = ImageTk.PhotoImage(Image.open(f).resize((w,h),Image.ANTIALIAS))
            la.configure(image=im)
            la.image = im
            root.after(delay, im_update)
    except:
        print('file open errer')
        im_update()

root.after(delay, im_update)
root.mainloop()
