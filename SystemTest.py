from tkinter import *
from tkinter import messagebox
from time import sleep
from SystemTestStub import TestWindow

class SystemTest():
    SysWindow = ""
    win_width = ""
    win_height = ""
    max_boxes = 5
    recCount = 0
    checkbox_vals = [0,0,0,0,0]
    checkbox_calls_labels = {0:["fsonic","(This Will Run Tests on \nFront Ultrasonic Sensor)"],
                             1:["bsonic","(This Will Run Tests on \nBottom Ultrasonic Sensor)"],
                             2:["video","(This Will Run Tests on \nThe Video Camera)"],
                             3:["motors","(This Will Run Tests on \nThe Driving Motors)"],
                             4:["camerapan","(This Will Run Tests on \nThe Camera Moment \nModule)"]}

    def __init__(self):
        self.SysWindow = Tk()
        self.SysWindow.resizable(0, 0)
        self.SysWindow.config(bg="black")
        self.SysWindow.geometry("600x400")
        self.win_width = 600
        self.win_height = 400
        self.SysWindow.geometry(f"+{abs(0)}+{abs(0)}")
        self.SysWindow.overrideredirect(1)
        Button(self.SysWindow, font=("Courier bold", 10), text="Exit", command=self.SysWindow.destroy, width=4, bg="red",
               fg="white",
               borderwidth=0).place(relx=0.91, rely=0.0)
        for IntVars_ in range(0,self.max_boxes):
            self.checkbox_vals[IntVars_] = IntVar()
        print(f"Check Box init -> {self.checkbox_vals}")
        self.MainMenu()




    def MainMenu(self):
        try:
            Label(self.SysWindow, font=("Courier bold", 15), text="VISIOR'S On Board Sensor Test", width=len("VISIOR'S On Board Sensor Test"),
                  fg="#2ade2a",
                  bg="black").pack(side="top")
            Label(self.SysWindow, font=("Courier bold", 9), text="Click on the checkboxe's to select and then \nClick 'Start Test' button at the bottom of screen to start tests \n ''you can also run multpile tests''", width=self.win_width,
                  fg="#2ade2a",
                  bg="black").pack(side="top")

            Button(self.SysWindow, font=("Courier bold", 13), text="Start Tests >", width=len("Start Tests >"),highlightthickness=0, bg="#2ade2a",
                   fg="black", borderwidth=0,command = self.getCheckBoxState).pack(side="bottom",pady = 5)



            self.CreateCheckBar()
            self.SysWindow.focus()
            self.SysWindow.mainloop()
        except Exception as e:
            print(f"Exception in <Function> MainMenu - <Class> SystemTest - <File> SystemTest.py --> {e}")
            pass


    def CreateCheckBar(self):
        y_pos_start = 0.25

        for checkboxes in range(0,self.max_boxes):
            if checkboxes<=2:
                x_pos_start = 0.15
            else:
                x_pos_start = 0.6
            if checkboxes == 3:
                y_pos_start = 0.25

            check_box_text = self.checkbox_calls_labels.get(checkboxes)[1].split("\n")[1].replace(")","")
            Checkbutton(self.SysWindow , text = check_box_text , variable =self.checkbox_vals[checkboxes],fg="red",font=("Courier bold", 10),
                        bg="black").place(relx = x_pos_start ,rely = y_pos_start)
            Label(self.SysWindow, font=("Courier bold", 9), justify = "left",text=self.checkbox_calls_labels.get(checkboxes)[1], width=len("This Will Run Test son   "),
                  fg="#2ade2a",
                  bg="black").place(relx = x_pos_start ,rely = y_pos_start+0.06)
            y_pos_start+=0.23


    def getCheckBoxState(self):
        print(len(self.checkbox_vals))

        sum_check = 0
        for i in range(len(self.checkbox_vals)):
            sum_check+=self.checkbox_vals[i].get()


        if sum_check==0:
            messagebox.showerror("Cannot Run Tests","No Option Selected For Test \n'Select Atleast one option'")
        else:
            self.SysWindow.destroy()
            TestWindow(self.checkbox_vals , not sum_check == 1,self.checkbox_calls_labels)
            #messagebox.showinfo("Completed","Tests Completed")
            SystemTest().MainMenu()

            self.SysWindow.after(3000, self.SysWindow.destroy)







    def __del__(self):
        try:
            self.SysWindow.destroy()
        except Exception as e:
            print(f"Exception in <Function> __del__ - <Class> SystemTest - <File> SystemTest.py --> {e}")
            pass







if __name__ == "__main__":
    St = SystemTest()
    St.MainMenu()