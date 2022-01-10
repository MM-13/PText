#modules
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('MM13 - PText')
root.iconbitmap('C:/Users/MatthiasMaes/3D Objects/texteditor.ico')
root.state('zoomed')

global open_status_name
open_status_name = False

global selected
selected = False

#new file
def new_file():
    mtext.delete("1.0", END)
    root.title('New File - PText')
    statusbar.config(text= "New File    ")

    global open_status_name
    open_status_name = False

#open file
def open_file():
    mtext.delete("1.0", END)

    text_file = filedialog.askopenfilename(initialdir="", title= "Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("Alle Files", "*.*")))
    
    if text_file:
        global open_status_name
        open_status_name = text_file
    
    name = text_file
    statusbar.config(text=f'{name}        ')
    name = name.replace("", "")
    root.title(f'{name} - PText')

    text_file = open(text_file, 'r')
    txt = text_file.read()

    mtext.insert(END, txt)
    text_file.close()

#save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir="", title= "Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("Alle Files", "*.*")))
    if text_file:
        name = text_file
        statusbar.config(text=f'Saved: {name}        ')
        name = name.replace("", "")
        root.title(f'{name} - PText')

        text_file = open(text_file, 'w')
        text_file.write(mtext.get(1.0, END))
        text_file.close()

#save file
def save_file():
    global open_status_name
    if open_status_name:

        text_file = open(open_status_name, 'w')
        text_file.write(mtext.get(1.0, END))
        text_file.close()

        statusbar.config(text=f'Saved: {open_status_name}        ')

    else:
        save_as_file()

#cut text
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if mtext.selection_get():
            selected = mtext.selection_get()
            
            mtext.delete("sel.first", "sel.last")

            root.clipboard_clear()
            root.clipboard_append(selected)

#copy text
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    if mtext.selection_get():
        selected = mtext.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

#paste text
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = mtext.index(INSERT)
            mtext.insert(position, selected)



#frame
frame = Frame(root)
frame.pack(pady = 5)

#scrollbar
text_scroll = Scrollbar(frame)
text_scroll.pack(side = RIGHT, fill = Y)

#textbox
mtext = Text(frame, width = 110, height = 26, font = ("Helvetica", 16), selectbackground="blue", selectforeground="white", undo= True, yscrollcommand= text_scroll.set)
mtext.pack()

#configure scrollbar
text_scroll.config(command= mtext.yview)

#menubar
menu = Menu(root)
root.config(menu = menu)

#add file
file_menu = Menu(menu, tearoff= False)
menu.add_cascade(label= 'File', menu=file_menu)
file_menu.add_command(label= 'New', command= new_file)
file_menu.add_command(label= 'Open', command= open_file)
file_menu.add_command(label= 'Save', command= save_file)
file_menu.add_command(label= 'Save As', command= save_as_file)
file_menu.add_separator()
file_menu.add_command(label= 'Exit', command=root.quit)

#add edit
edit_menu = Menu(menu, tearoff= False)
menu.add_cascade(label= 'Edit', menu=edit_menu)
edit_menu.add_command(label= 'Cut           Crtl + x', command=lambda: cut_text(False))
edit_menu.add_command(label= 'Copy        Crtl + c', command=lambda: copy_text(False))
edit_menu.add_command(label= 'Paste        Crtl + v', command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label= 'Undo')
edit_menu.add_command(label= 'Redo')

#statusbar
statusbar = Label(root, text= 'Ready        ', anchor= E)
statusbar.pack(fill= X, side= BOTTOM, ipady= 5)

#keybindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

root.mainloop()