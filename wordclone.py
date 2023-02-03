from tkinter import *
from tkinter import font
from tkinter import filedialog as fd

root = Tk()
root.title("WORD")
root.geometry("700x500")

my_menu = Menu(root)
root.config(menu = my_menu)

frame2 = LabelFrame(root)
# Buttons
bold_button = Button(text="BOLD" ).grid(row=0,column=0)
italic_button = Button(text="ITALIC").grid(row=0, column=1)
underline_button = Button(text="UNDERLINE").grid(row=0 , column=2)
frame2.grid(row=0,column=0)



my_frame = LabelFrame(root)
my_frame.grid(row=1 ,column=0 ,columnspan=4,padx=10 , pady=10)



# scroll bar
scroll  = Scrollbar(my_frame)
scroll.pack( side = RIGHT , fill=BOTH )


# creat text area
my_text = Text(my_frame  ,border=10 ,width= 180, height=40, selectbackground="Yellow" ,selectforeground="Black",undo= TRUE, yscrollcommand=scroll.set)
my_text.pack(padx=10 ,pady=10)


#global variables
global open_statu_name
open_statu_name = False

global selected_item
selected_item = False



# defines functions of menus
def new_file ():
    my_text.delete(1.0 , END)
    root.title('New file')
    statusbar.config(text = 'New file        ')
    
    global open_statu_name
    open_statu_name = False
    
    
def open_file () :
    # opening a filepath
    my_text.delete(1.0 , END)
    filepath = fd.askopenfile(initialdir="C://Users//rdmp//codemy python" , filetypes=[("All files"  ,"*.*") , ("Text files" , "*.txt") , ("PDF files"  , "*.pdf") , ("Document files"  , "*.dox") , ("python files"  ,"*.py")])
    path = filepath.name
    
    global open_statu_name
    open_statu_name = path
    # updating status bas
    root.title(path )
    statusbar.config(text = path)
    
    # opening a file
    text_file = open(path, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff )
    filepath.close()
    
    
def save_as_file() :
    # saving a file
    savefile = fd.asksaveasfile(defaultextension=".*", filetypes=[("text files" , "*.txt"), ("PDF files", "*.pdf"), ("python file" , "*.py") , ("All files", "*.*")])
    path = savefile.name 
    # updating status 
    root.title(path )
    statusbar.config(text = path)
    
    # opening the saved file
    text_file = open(path, 'w')
    stuff = text_file.write(my_text.get(1.0,END))
    savefile.close()
    
    
def save_file():
        global open_statu_name
        if open_statu_name:
            root.title(open_statu_name )
            statusbar.config(text =open_statu_name)
    
            # opening the saved file
            text_file = open(open_statu_name, 'w')
            stuff = text_file.write(my_text.get(1.0,END))
            text_file.close()
            statusbar.config(text = "Saved" + text_file)
            
        else :
            save_as_file()   
     


def cut_edit():
    global selected_item
    if my_text.selection_get():
        selected_text =my_text.selection_get()
        selected_item = selected_text
        my_text.delete("sel.first" , "sel.last") 
    


def copy_edit():
    global selected_item
    if my_text.selection_get():
        selected_text =my_text.selection_get()
        selected_item = selected_text
         

def paste_edit():
    global selected_item
    cursor = my_text.index(INSERT)
    my_text.insert(cursor ,selected_item)



    
# file menu
filemenu = Menu(my_menu , tearoff=FALSE)
my_menu.add_cascade(label = "FILE" , menu = filemenu)
filemenu.add_command(label = "NEW" , command= new_file)
filemenu.add_command(label = "OPEN" , command=open_file)
filemenu.add_command(label = "SAVE" )
filemenu.add_command(label = "SAVE AS",command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label = "EXIT" ,command = root.quit)


# edit menu
editmenu = Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label = "EDIT" , menu = editmenu)
editmenu.add_command(label = "CUT" , command = cut_edit)
editmenu.add_command(label = "COPY" ,command =copy_edit)
editmenu.add_command(label = "PASTE",command =paste_edit)
editmenu.add_command(label = "UNDO")
editmenu.add_command(label = "REDO")


statusbar =  Label(my_frame , text = "READY       " , anchor=E)
statusbar.pack(fill = X , side= RIGHT)


scroll.config(command = my_text.yview)

root.mainloop() 