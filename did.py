from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
#import time

root = Tk()

files = os.listdir('.')
im_files = []
for f in files:
    if f.endswith('.jpg') or f.endswith('.png'):
        #print(f)
        im_files.append(f)
print(im_files)
im = ImageTk.PhotoImage(Image.open(im_files.pop()))
la = Label(root, image = im)
la.pack()       

def update():
    global im_files
    if len(im_files) == 0:
        files = os.listdir('.')
        for f in files:
            if f.endswith('.jpg') or f.endswith('.png'):
                #print(f)
                im_files.append(f)
        print(im_files)
    im = ImageTk.PhotoImage(Image.open(im_files.pop()))
    #la = Label(root, image = im)
    #la.pack()
    la.configure()
    print(im_files)
    #time.sleep(1)
    root.after(1000,update)


#root.title('전자게시판')
#root.geometry('1920x1080+0+0')
#popup = Toplevel(root)

#update()
root.after(1000, update)
root.mainloop()
