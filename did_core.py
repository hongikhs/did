# 파이썬3.X에서 동작하는 코드입니다.

# 필요한 라이브러리 가져오기
from tkinter import *
from PIL import Image, ImageTk
import os

# 설정값
delay = 3000
sync_cmd = 'rclone sync hongikdid: ~/did'

# 창 띄우기
root = Tk()
root.attributes('-fullscreen', True)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# 첫 번째 사진 보여주기
os.system(sync_cmd)
files = os.listdir('.')
im_files = []
for f in files:
    if f.endswith('.jpg') or f.endswith('.png'):
        im_files.append(f)
im = ImageTk.PhotoImage(Image.open(im_files.pop(0)).resize((w,h),Image.ANTIALIAS))
la = Label(root, image=im, bg='black')
la.pack()

# 사진 업데이트 함수
def im_update():
    global im_files
    if len(im_files) == 0:
        os.system(sync_cmd)
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
