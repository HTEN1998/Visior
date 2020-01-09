import time
from tkinter import*
       
def addPrint():
        for i in range(50):
                text.insert(END,"count %d"%(i)+"\n")        
                text.yview_moveto(1)
                time.sleep(0.06)
                vsb.update()  
        btn=Button(root,font = ("Courier bold", 11),text = "Install Updates",width = 10,fg="black",bg="#2ade2a",borderwidth=0,highlightthickness=0,activebackground="black",activeforeground="white")
        btn.place(relx=0.8,rely=0.93)

root = Tk()
root.overrideredirect(True)  
root.resizable(0, 0)
root.config(bg = "black")
root.geometry('640x480')
root.geometry(f"+{abs(4)}+{abs(4)}")

Label(root,font = ("Courier bold", 20), text = "VISIOR Updation", width = "1080",fg = "#2ade2a",
                  bg = "black").pack(side = "top")
Button(root,font = ("Courier bold", 10), text = "\u274c",command = root.destroy,width=4,bg="black",fg="red",borderwidth=0, highlightthickness = 0, activebackground = "black",  activeforeground = "white").place(relx = 0.91,rely=0.0)

text = Text(root,height=26,width=40,fg="#2ade2a",bg="black",borderwidth = 0,highlightthickness = 0)
vsb = Scrollbar(orient="vertical")
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right",fill='y')
text.pack(side="left")

addPrint()


root.mainloop() 
