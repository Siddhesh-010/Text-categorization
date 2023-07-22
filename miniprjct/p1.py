from tkinter import *
from tkinter.scrolledtext import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\textfiles",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    #print(file.read())
    data = file.read()
    mw_st_data .insert(END,data)
    file.close()

mw = Tk()
mw.title("Text Categorization with news documents")
mw.geometry("2000x2500+0+0")
mw['bg']='#B5D3E7'
f=("Arial", 30, "bold")
f_text=("Times New Roman",30)
y=20
x=10

mw_st_data = ScrolledText(mw, width=65, height=10, font=f_text)
mw_st_data.pack()             
mw_lab_topic=Label(mw, text="Text Categorization", font=f)
mw_btn_select = Button(mw, text="Select", font=f, width=8,command=openFile)
mw_btn_select.pack()
mw_btn_stop = Button(mw, text="Stop", font=f, width=8)
mw_btn_filteration = Button(mw, text="Filteration", font=f, width=8)
mw_btn_validation = Button(mw, text="Validation", font=f, width=8)
mw_btn_algo = Button(mw, text="Algo", font=f, width=8)

mw_st_data.place(x=45,y=70)
mw_lab_topic.place(x=550, y=15)
mw_btn_select.place(x=15, y=600)
mw_btn_stop.place(x=250, y=600)
mw_btn_filteration.place(x=500, y=600)
mw_btn_validation.place(x=750, y=600)
mw_btn_algo.place(x=1000, y=600)


mw.mainloop()