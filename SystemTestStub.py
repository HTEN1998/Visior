from time import sleep
from tkinter import *

def TestWindow(checkbox_vals , sum_check ,checkbox_calls_labels):
    multi_Tests = sum_check

    for i in range(len(checkbox_vals)):
        print(f"Itr {i}")
        if checkbox_vals[i].get() == 1:

            test_title = "Started "+checkbox_calls_labels.get(i)[1].split("\n")[1].replace(")","")+"Test"
            SysWindow = Tk()
            SysWindow.resizable(0, 0)
            SysWindow.config(bg="black")
            SysWindow.geometry("600x400")
            SysWindow.overrideredirect(1)

            SysWindow.geometry(f"+{abs(4)}+{abs(4)}")

            Label(SysWindow, font=("Courier bold", 12), text=test_title, width=len("VISIOR'S On Board Sensor Test"),
                  fg="#2ade2a",
                  bg="black").pack(side="top")
            
            text = Text(SysWindow,height=6, width=40,fg="#2ade2a",bg="black")
            vsb = Scrollbar(orient="vertical")
            text.configure(yscrollcommand=vsb.set)
            vsb.pack(side="right", fill="y")
            text.pack(side="left", fill="both", expand=True)
            
            for i in range(50):
                text.insert(END,"hello %d\n"%(i))
                # SysWindow.after(SysWindow,2000)

            if multi_Tests == True:

                SysWindow.after(5000,SysWindow.destroy)
            else:
                Button(SysWindow, font=("Courier bold", 9), text="Exit", command=SysWindow.destroy, width=4, bg="red",
                       fg="black",
                       borderwidth=0).place(relx=0.91, rely=0.0)


            SysWindow.mainloop()
            print(f"End ..{i}")


