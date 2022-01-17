#modules
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api

root = Tk()
root.title('MM13 - PText')
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

#bold text
def bold_it():
    bold_font = font.Font(mtext, mtext.cget("font"))
    bold_font.configure(weight="bold")

    mtext.tag_configure("bold", font=bold_font)

    current_tags = mtext.tag_names("sel.first")

    if "bold" in current_tags:
        mtext.tag_remove("bold", "sel.first", "sel.last")
    else:
        mtext.tag_add("bold", "sel.first", "sel.last")

#italic text
def italic_it():
    italics_font = font.Font(mtext, mtext.cget("font"))
    italics_font.configure(slant="italic")

    mtext.tag_configure("italic", font=italics_font)

    current_tags = mtext.tag_names("sel.first")

    if "italic" in current_tags:
        mtext.tag_remove("italic", "sel.first", "sel.last")
    else:
        mtext.tag_add("italic", "sel.first", "sel.last")

#fonts
def font1():
    fonts1 = font.Font(mtext, mtext.cget("font"))
    fonts1.configure(family="Helvetica")

    mtext.tag_configure("tags", font=fonts1)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font2():
    fonts2 = font.Font(mtext, mtext.cget("font"))
    fonts2.configure(family="Verdana")

    mtext.tag_configure("tags", font=fonts2)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font3():
    fonts3 = font.Font(mtext, mtext.cget("font"))
    fonts3.configure(family="Calibri")

    mtext.tag_configure("tags", font=fonts3)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font4():
    fonts4 = font.Font(mtext, mtext.cget("font"))
    fonts4.configure(family="Comic Sans MS")

    mtext.tag_configure("tags", font=fonts4)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font5():
    fonts5 = font.Font(mtext, mtext.cget("font"))
    fonts5.configure(family="Castellar")

    mtext.tag_configure("tags", font=fonts5)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font6():
    fonts6 = font.Font(mtext, mtext.cget("font"))
    fonts6.configure(family="Arial Black")

    mtext.tag_configure("tags", font=fonts6)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font7():
    fonts7 = font.Font(mtext, mtext.cget("font"))
    fonts7.configure(family="Algerian")

    mtext.tag_configure("tags", font=fonts7)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font8():
    fonts8 = font.Font(mtext, mtext.cget("font"))
    fonts8.configure(family="Broadway")

    mtext.tag_configure("tags", font=fonts8)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font9():
    fonts9 = font.Font(mtext, mtext.cget("font"))
    fonts9.configure(family="Magneto")

    mtext.tag_configure("tags", font=fonts9)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

def font0():
    fonts0 = font.Font(mtext, mtext.cget("font"))
    fonts0.configure(family="Cooper Black")

    mtext.tag_configure("tags", font=fonts0)

    current_tags = mtext.tag_names("sel.first")

    if "tags" in current_tags:
        mtext.tag_add("tags", "sel.first", "sel.last")
    else:
        mtext.tag_add("tags", "sel.first", "sel.last")

#color text
def text_color():
    mcolor = colorchooser.askcolor()[1]
    if mcolor:
        statusbar.config(text=mcolor)

        color_font = font.Font(mtext, mtext.cget("font"))

        mtext.tag_configure("colored", font=color_font, foreground=mcolor)

        current_tags = mtext.tag_names("sel.first")

        if "colored" in current_tags:
            mtext.tag_remove("colored", "sel.first", "sel.last")
        else:
            mtext.tag_add("colored", "sel.first", "sel.last")

#background color
def background_color():
    mcolor = colorchooser.askcolor()[1]
    if mcolor:
        mtext.config(bg=mcolor)

#change all text color
def all_text_color():
    mcolor = colorchooser.askcolor()[1]
    if mcolor:
        mtext.config(fg=mcolor)

#print file
def print_file():
    #printer_name = win32print.GetDefaultPrinter()
    #statusbar.config(text=printer_name)
    file_to_print = filedialog.askopenfilename(initialdir="", title= "Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("Alle Files", "*.*")))

    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

#select all text
def select_all(e):
    mtext.tag_add('sel', '1.0', 'end')

#clear all text
def clear_all():
    mtext.delete(1.0, END)

#night mode on
def night_mode_on():
    main_color = "#000000"
    second_color = "#373737"
    text_color = "#0000ff"
    mtext.config(fg="#0000ff")

    root.config(bg=main_color)
    statusbar.config(bg=main_color, fg=text_color)
    mtext.config(bg=second_color)
    toolbar_frame.config(bg=main_color)
    #toolbar buttons
    Bold_button.config(bg=second_color, fg=text_color)
    Italic_button.config(bg=second_color, fg=text_color)
    redo_button.config(bg=second_color, fg=text_color)
    undo_button.config(bg=second_color, fg=text_color)
    color_text_button.config(bg=second_color, fg=text_color)
    # file menu colors
    file_menu.config(bg=main_color, fg=text_color)
    edit_menu.config(bg=main_color, fg=text_color)
    color_menu.config(bg=main_color, fg=text_color)
    options_menu.config(bg=main_color, fg=text_color)

#hacker mode on
def hacker_mode_on():
    main_color = "#000000"
    second_color = "#373737"
    text_color = "#00ff00"
    mtext.config(fg="#00ff00")

    root.config(bg=main_color)
    statusbar.config(bg=main_color, fg=text_color)
    mtext.config(bg=second_color)
    toolbar_frame.config(bg=main_color)
    #toolbar buttons
    Bold_button.config(bg=second_color, fg=text_color)
    Italic_button.config(bg=second_color, fg=text_color)
    redo_button.config(bg=second_color, fg=text_color)
    undo_button.config(bg=second_color, fg=text_color)
    color_text_button.config(bg=second_color, fg=text_color)
    # file menu colors
    file_menu.config(bg=main_color, fg=text_color)
    edit_menu.config(bg=main_color, fg=text_color)
    color_menu.config(bg=main_color, fg=text_color)
    options_menu.config(bg=main_color, fg=text_color)

#night mode off
def night_mode_off():
    main_color = "SystemButtonFace"
    second_color = "SystemButtonFace"
    text_color = "black"

    root.config(bg=main_color)
    statusbar.config(bg=main_color, fg=text_color)
    mtext.config(bg="white")
    toolbar_frame.config(bg=main_color)
    #toolbar buttons
    Bold_button.config(bg=second_color, fg=text_color)
    Italic_button.config(bg=second_color, fg=text_color)
    redo_button.config(bg=second_color, fg=text_color)
    undo_button.config(bg=second_color, fg=text_color)
    color_text_button.config(bg=second_color, fg=text_color)
    # file menu colors
    file_menu.config(bg=main_color, fg=text_color)
    edit_menu.config(bg=main_color, fg=text_color)
    color_menu.config(bg=main_color, fg=text_color)
    options_menu.config(bg=main_color, fg=text_color)

#toolbar
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

#frame
frame = Frame(root)
frame.pack(pady = 5)

#vertical scrollbar
text_scroll = Scrollbar(frame)
text_scroll.pack(side = RIGHT, fill = Y)

#horizontal scrollbar
hor_scroll = Scrollbar(frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill= X)

#textbox
mtext = Text(frame, width=105, height=25, font=("Helvetica", 16), selectbackground="blue", selectforeground="white", undo= True, yscrollcommand= text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
mtext.pack()

#configure scrollbar
text_scroll.config(command= mtext.yview)
hor_scroll.config(command=mtext.xview)

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
file_menu.add_command(label= 'Print', command= print_file)
file_menu.add_separator()
file_menu.add_command(label= 'Exit', command=root.quit)

#add edit
edit_menu = Menu(menu, tearoff= False)
menu.add_cascade(label= 'Edit', menu=edit_menu)
edit_menu.add_command(label= 'Cut', command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label= 'Copy', command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label= 'Paste', command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label= 'Undo', command=mtext.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label= 'Redo', command=mtext.edit_redo, accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label= 'Select All', command=lambda: select_all(False), accelerator="(Ctrl+a)")
edit_menu.add_command(label= 'Clear', command=clear_all)

#style menu
style_menu = Menu(menu, tearoff=False)
menu.add_cascade(label= 'Styles', menu=style_menu)
style_menu.add_command(label= 'Algerian', command=font7)
style_menu.add_command(label= 'Arial Black', command=font6)
style_menu.add_command(label= 'Broadway', command=font8)
style_menu.add_command(label= 'Calibri', command=font3)
style_menu.add_command(label= 'Castellar', command=font5)
style_menu.add_command(label= 'Comic Sans MS', command=font4)
style_menu.add_command(label= 'Cooper Black', command=font0)
style_menu.add_command(label= 'Helvetica', command=font1)
style_menu.add_command(label= 'Magneto', command=font9)
style_menu.add_command(label= 'Verdana', command=font2)

#color menu
color_menu = Menu(menu, tearoff= False)
menu.add_cascade(label= 'Colors', menu=color_menu)
color_menu.add_command(label= 'Change selected', command= text_color)
color_menu.add_command(label= 'Change all', command= all_text_color)
color_menu.add_command(label= 'Background', command= background_color)

#options
options_menu = Menu(menu, tearoff= False)
menu.add_cascade(label= 'Options', menu=options_menu)
options_menu.add_command(label= 'Night Mode', command= night_mode_on)
options_menu.add_command(label= 'Hacker Mode', command= hacker_mode_on)
options_menu.add_command(label= 'Default Mode', command= night_mode_off)

#statusbar
statusbar = Label(root, text= 'Ready        ', anchor= E)
statusbar.pack(fill= X, side= BOTTOM, ipady= 15)

#keybindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
#select binding
root.bind('Control-A', select_all)
root.bind('Control-a', select_all)

#rest
fee = 'MM-13'
mlabel = Label(root, text=fee[:-1]).pack()

#Buttons
#Bold
Bold_button = Button(toolbar_frame, text='Bold', command=bold_it)
Bold_button.grid(row=0, column=2, sticky=W, padx=2)

#Italic
Italic_button = Button(toolbar_frame, text='Italic', command=italic_it)
Italic_button.grid(row=0, column=3, padx=2)

#undo/redo buttons
undo_button = Button(toolbar_frame, text='Undo', command=mtext.edit_undo)
undo_button.grid(row=0, column=0, padx=2)
redo_button = Button(toolbar_frame, text='Redo', command=mtext.edit_redo)
redo_button.grid(row=0, column=1, padx=2)

#color button
color_text_button = Button(toolbar_frame, text='Color', command= text_color)
color_text_button.grid(row=0, column=4, padx=2)

root.mainloop()