from Tkinter import *
from PIL import Image       # pip install pillow
from PIL import ImageTk
import os
import sys
import dropbox              # pip install dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

delay = 3000
TOKEN = 'yIX6CZwhLDAAAAAAAAAAFnakjjVyy8DhVyWLHf0WIOjbpDH8t3l3yZBjpgVJ1rdK'
dbx = dropbox.Dropbox(TOKEN)
cloud_files = []
local_files = []
down_files = []
full_files = []

def file_update():
    for file in dbx.files_list_folder('').entries:
        if file.name.endswith('.jpg.') or file.name.endswith('.png'):
            cloud_files.append(file.name)
    files = os.listdir('.')
    for f in files:
        if f.endswith('.jpg') or f.endswith('.png'):
            local_files.append(f)
    print cloud_files
    print local_files

def im_update():
    global im_files
    if len(im_files) == 0:
        files = os.listdir('.')
        for f in files:
            if f.endswith('.jpg') or f.endswith('.png'):
                im_files.append(f)
    try:
        im = ImageTk.PhotoImage(Image.open(im_files.pop(0)).resize((w,h),Image.ANTIALIAS))
        la.configure(image=im)
        la.image = im
        root.after(delay, im_update)
    except:
        print('file open errer')
        im_update()

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
####root.attributes('-fullscreen', True)
#root.overrideredirect(True)
#root.focus_set()
#root.bind("<Escape>", lambda e: root.quit())
#root.attributes('-topmost', True)
#root.wm_state('zoomed')
#root.configure(background='black')

file_update()


im = ImageTk.PhotoImage(Image.open('start.png').resize((w,h),Image.ANTIALIAS))
la = Label(root, image=im, bg='black')
la.pack()



root.after(delay, im_update)
#root.mainloop()
