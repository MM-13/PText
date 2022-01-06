#modules
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('MM13 - PText')
root.iconbitmap('C:/Users/MatthiasMaes/3D Objects/texteditor.ico')
root.state('zoomed')

#new file
def new_file():
    mtext.delete("1.0", END)
    root.title('New File - PText')
    statusbar.config(text= "New File    ")

#open file
def open_file():
    mtext.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="", title= "Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("Alle Files", "*.*")))
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
file_menu.add_command(label= 'Save')
file_menu.add_command(label= 'Save As', command= save_as_file)
file_menu.add_separator()
file_menu.add_command(label= 'Exit', command=root.quit)

#add edit
edit_menu = Menu(menu, tearoff= False)
menu.add_cascade(label= 'Edit', menu=edit_menu)
edit_menu.add_command(label= 'Cut')
edit_menu.add_command(label= 'Copy')
edit_menu.add_command(label= 'Paste')
edit_menu.add_command(label= 'Undo')
edit_menu.add_command(label= 'Redo')

#statusbar
statusbar = Label(root, text= 'Ready        ', anchor= E)
statusbar.pack(fill= X, side= BOTTOM, ipady= 5)

root.mainloop()
