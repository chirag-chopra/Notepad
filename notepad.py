from tkinter import *
import pyautogui
from tkinter import filedialog

def newfile():
    global filee
    root.title('Untitled - Notepad')
    textarea.delete(1.0, END)
def openfile():
    global filee
    filee = filedialog.askopenfilename(filetype=(('File','*.txt'),('All Files')))
    if filee is '':
        filee = None
    else:
        root.title(f'Notepad  {filee}')
        textarea.delete(1.0, END)
        f = open(filee, 'r')
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global filee
    filee = filedialog.asksaveasfile(mode = 'w',defaultextension='*.txt',filetype=(('File','*.txt'),('All Files')))
    if filee is None:
        return
    else:
        text2save = textarea.get(1.0, END)
        filee.write(str(text2save))
        filee.close()

def cut():
    pyautogui.hotkey('ctrl', 'x')

def copy():
    pyautogui.hotkey('ctrl', 'c')

def paste():
     pyautogui.hotkey('ctrl', 'v')

def undo():
    pyautogui.hotkey('ctrl', 'z')

def redo():
    pyautogui.hotkey('ctrl', 'y')

def notepad():
    top = Toplevel()
    top.focus()
    top.geometry('450x270+120+120')
    top.minsize(450, 270)
    top.maxsize(450, 270)
    top.title('About - Notepad')
    top.iconbitmap(r'images/np.ico')

    main = Frame(top)
    main.pack()
    head = Label(main, text='Notepad V1.0', font=('Arial', 20, 'bold'), pady=35)
    head.pack()

    Label(main,text = 'Notepad is a simple text editor which enables user\nto create documents. It is only capable of\ncreating and editing plain text files',pady=20, font=('Arial',12,'bold')).pack()

def developer():
    top = Toplevel()
    top.focus()
    top.geometry('450x270+120+120')
    top.minsize(450, 270)
    top.maxsize(450, 270)
    top.title('About - Developer')
    top.iconbitmap(r'images/np.ico')

    main = Frame(top)
    main.pack()

    Label(main,text='About Developer', font = ('Comic Sans',30,'bold'),pady=20).pack()
    Label(main,text='Chirag Chopra is a young BCA student from Delhi,India.\nApart from programming '
                    'he has deep interest in Ethical Hacking\nand Penetration Testing.', font=('Comic Sans',10,'bold'),pady=10).pack()
    Label(main, text='Meet me on :',font=('Comic Sans',10,'bold')).pack(anchor='w')
    Label(main,text='https://www.facebook.com/chirag.chopra.5494',font=('Comic Sans',9,'bold')).pack(anchor='w')
    Label(main,text='https://www.instagram.com/127.01.0.1/',font=('Comic Sans',9,'bold')).pack(anchor='w')
    Label(main, text='https://twitter.com/Mighty_Chirag',font=('Comic Sans',9,'bold')).pack(anchor='w')

def theme(*args):
    if themes[0] == var.get():
        textarea.configure(background='#ffffff', fg='black', insertbackground='black')
    elif themes[1] == var.get():
        textarea.configure(background='#e6e6e6', fg='black', insertbackground='black')
    elif themes[2] == var.get():
        textarea.configure(background='#000000', fg='yellow', insertbackground='white')
    elif themes[3] == var.get():
        textarea.configure(background='#000000', fg='green', insertbackground='white')

root = Tk()
root.title('Untitled - Notepad')
root.geometry('837x593')
root.minsize(837,593)
root.iconbitmap(r'images/np.ico')

line = Menu(root)
root.config(menu=line)

file = Menu(line, tearoff=0)
line.add_cascade(label="File", menu=file)
new_icon = PhotoImage(file = 'images/paste.png')
file.add_command(label='New', command=newfile)
file.add_command(label='Open', command=openfile)
file.add_command(label='Save', command=savefile)
file.add_separator()
file.add_command(label='Exit                   Alt + F4', command=root.destroy)

edit = Menu(line, tearoff=0)
line.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Undo                 Cntl + Z', command=undo)
edit.add_command(label='Redo                  Cntl + Y', command=redo)
edit.add_separator()
edit.add_command(label='Cut                    Cntl + X', command=cut)
edit.add_command(label='Copy                 Cntl + C', command=copy)
edit.add_command(label='Paste                 Cntl + V', command=paste)

about = Menu(line, tearoff=0)
line.add_cascade(label='About', menu=about)
about.add_command(label='Notepad', command=notepad)
about.add_separator()
about.add_command(label='Developer', command=developer)

frame_btn = Frame(root,pady=3, padx=10)

new_btn = Button(frame_btn, padx=10, borderwidth=0, command=newfile)
new_img = PhotoImage(file='images/new.png')
new_btn.config(image=new_img, width=32, height=32)

open_btn = Button(frame_btn, padx=10, borderwidth=0, command=openfile)
open_img = PhotoImage(file='images/open.png')
open_btn.config(image=open_img, width=32, height=32)

save_btn = Button(frame_btn, padx=10, borderwidth=0, command=savefile)
save_img = PhotoImage(file='images/save.png')
save_btn.config(image=save_img, width=32, height=32)

cut_btn = Button(frame_btn, padx=10, borderwidth=0, command=cut)
cut_img = PhotoImage(file='images/cut.png')
cut_btn.config(image=cut_img, width=32, height=32)

copy_btn = Button(frame_btn, padx=10, borderwidth=0, command=copy)
copy_img = PhotoImage(file='images/copy.png')
copy_btn.config(image=copy_img, width=32, height=32)

paste_btn = Button(frame_btn, padx=10, borderwidth=0, command=paste)
paste_img = PhotoImage(file='images/paste.png')
paste_btn.config(image=paste_img, width=28, height=32)

var = StringVar()
var.set('Select Theme')
themes = ['No Theme','Light Theme','Dark Theme','Hacker Theme']
t = OptionMenu(frame_btn,var,*themes)
t.pack(side='right')
var.trace('w',theme)

frame_btn.pack(anchor='w')
new_btn.pack(side='left')
open_btn.pack(side='left')
save_btn.pack(side='left')
cut_btn.pack(side='left')
copy_btn.pack(side='left')
paste_btn.pack(side='left')

textarea = Text(root, font=('Arial', 12),undo=True)
textarea.pack(expand=TRUE,fill=BOTH)
textarea.focus()

scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)

root.mainloop()