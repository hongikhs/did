from tkinter import *
from PIL import Image
from PIL import ImageTk
import os

delay = 3000
root = Tk()
root.title('전자게시판')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(True)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
#root.bind("<Escape>", lambda e: root.quit())
#root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
#root.wm_state('zoomed')
#root.overrideredirect(True)
#root.geometry('1366x768+0+0')
root.configure(background='black')

files = os.listdir('.')
im_files = []
for f in files:
    if f.endswith('.jpg') or f.endswith('.png'):
        im_files.append(f)
#print(im_files)
im = ImageTk.PhotoImage(Image.open(im_files.pop(0)).resize((w,h),Image.ANTIALIAS))
la = Label(root, image=im, bg='black')
la.pack()       

def im_update():
    global im_files
    if len(im_files) == 0:
        files = os.listdir('.')
        for f in files:
            if f.endswith('.jpg') or f.endswith('.png'):
                im_files.append(f)
        print(im_files)
    try:
        im = ImageTk.PhotoImage(Image.open(im_files.pop(0)).resize((w,h),Image.ANTIALIAS))
        la.configure(image=im)
        la.image = im
        root.after(delay, im_update)
    except:
        print('file open errer')
        im_update()

root.after(delay, im_update)
root.mainloop()
