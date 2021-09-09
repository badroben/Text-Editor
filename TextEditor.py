import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# change the color of the text
def change_color():
    color = colorchooser.askcolor(title='pick a color for your text')
    text_area.config(fg=color[1])

# change the font type and the font size
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

# new file
def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

# save file
def save_file():
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")
                                                   ])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
        except Exception:
            print("Unable to save file :(")
        finally:
            file.close()

# open file
def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"), ("Text Documents", "*.text")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except Exception:
        print("Unable to read file :(")
    finally:
        file.close()

# copy selected text
def copy():
    text_area.event_generate("<<Copy>>")

# paste already copied text
def paste():
    text_area.event_generate("<<Paste>>")

# cut selected text
def cut():
    text_area.event_generate("<<Cut>>")

# show info about the program
def about():
    showinfo("About this program", "This is a program written by Badro Benouatas :D")

# quit the program
def quit():
    window.destroy()


window = Tk()
window.title("Text Editor Program")
file = None
window.iconbitmap('peepo.ico')

window_width = 700
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Find the coordinates for the window to be in the centre of the screen
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# default font name
font_name = StringVar(window)
font_name.set("Comic Sans")

# default font size
font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
# weight = 1 so that the column and row extend if there is extra space to fill
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# Specify where the text area should stick to and since we want it to
# fill the window we stick it to all 4 directions.
text_area.grid(sticky=N + E + S + W)
frame = Frame(window)
frame.grid()
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# color button to change the color of the text
color_button = Button(frame, text="Change Text Color", command=change_color)
color_button.grid(row=0, column=0)

# font box to change the font
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

# size box to change the size of the text
size_box = Spinbox(frame, from_=1, to=72, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save File", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
