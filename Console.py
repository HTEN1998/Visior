from tkinter import *
from TkinterCam import *
from tkinter import messagebox
from SystemTest import *


class Console:
    window = ""
    radio_var = 0
    radio_buttons_labels_vals = {1: ["Remote Controlled mode",
                                     "This Mode allows yo to control Visior manually with keyboard\nfollowing is provided\n- Camera Movment\n- The Movment of the Bot \n- Monitoring sensor data",
                                     1],
                                 2: ["Autonomous working mode",
                                     "This this mode Visior will work in self controlled mode\ni.e. without any manual interaction \nThe info needed to be provided is\n- the source and destination go to and come from",
                                     2],
                                 3: ["Run Tests",
                                     "This will allow you run 'TroubleShooting' \nThe Sensors and modules onboard Visior",
                                     3]}
    radio_buttton_vars = [0, 0, 0]

    radio_button_clicked = -1

    def __init__(self):
        # name_str = "V  i  s  i  o  r"
        # self.window.wait_visibility()
        # self.window.config(bg="dodger blue")
        # self.window.wm_attributes("-transparent","dodger blue")
        '''self.window = Tk()
        self.window.config(bg="black")
        self.window.overrideredirect(1)
        w_height, w_width = 360, 360
        self.window.geometry(f"{w_height}x{w_width}")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        print(f"width x height -> {width}x{height}")
        self.window.geometry(f"+{abs(w_width // 2 - width // 2)}+{abs(w_height // 2 - height // 2)}")'''
        self.window = Tk()
        self.window.geometry("640x480")
        self.window.resizable(0, 0)
        self.window.config(bg="black")

        self.window.geometry(f"+{abs(0)}+{abs(0)}")
        #self.window.overrideredirect(1)
        for i in range(10):
            self.radio_buttton_vars.append(0)

        self.window.focus()
        Label(self.window, text="V  I  S  I  O  R\n console", bg="black", fg="#2ade2a", font=("Courier ", 20)).pack(
            side="top",
            pady="10",
            expand=False)

        Button(self.window, font=("Courier bold", 10), text="Exit", command=self.window.destroy, width=4, bg="red",
               fg="white",
               borderwidth=0).place(relx=0.91, rely=0.0)

        self.radio_buttton_vars.clear()

    def MainMenu(self):
        try:
            self.radio_button_clicked = -1
            i = 0
            y_pos = 0.2
            self.radio_var = IntVar()

            for indexes, values in self.radio_buttons_labels_vals.items():
                Radiobutton(self.window, text=values[0], variable=self.radio_var, value=values[-1], bg="black",
                            fg="red", font=("Courier underline", 11),
                            command=lambda: self.SetRadioClicked(self.radio_var.get())).place(relx=0.2, rely=y_pos)
                Label(self.window, text=values[1], bg="black", fg="#2ade2a", font=("Courier ", 10),
                      justify="left").place(relx=0.2, rely=y_pos + 0.05)
                i += 1
                y_pos += 0.27

            Button(self.window, font=("Courier bold", 11), text="Next", width=10, fg="black", bg="#2ade2a",
                   borderwidth=0, command=self.callDecider).place(relx=0.83, rely=y_pos - 0.08)
            Label(self.window, text="Select any option and click 'Next' to proceed", bg="black", fg="red",
                  font=("Courier ", 10), justify="left").place(relx=0.05, rely=y_pos - 0.08)
            self.window.mainloop()
        except Exception as e:
            print(f"Exception in <Function> MainMenu - <Class> Console - <File> Console.py --> {e}")
            pass

    def SetRadioClicked(self, radio_val):
        self.radio_button_clicked = radio_val

    def callDecider(self):
        if self.radio_button_clicked == 1:
            self.RcMode()
        elif self.radio_button_clicked == 2:
            pass
        elif self.radio_button_clicked == 3:
            self.sysTest()
        elif self.radio_button_clicked == -1:
            messagebox.showerror("Error", "No Option Selected")

    def RcMode(self):
        try:
            if self.window:
                self.window.destroy()
                print("Jumped to TkinterCam  from Console .. ")
                RcModeController().StreamScreen()
        except Exception as e:
            print(f"Exception in <Function> RcMode - <Class> Console - <File> Console.py --> {e}")
            pass

    def sysTest(self):
        try:
            if self.window:
                self.window.destroy()
                print("Jumped to System Test  from Console .. ")
                SystemTest()
        except Exception as e:
            print(f"Exception in <Function> sysTest - <Class> Console - <File> Console.py --> {e}")
            pass

    def __del__(self):
        try:
            self.window.destroy()
        except:
            pass


if __name__ == "__main__":
    Console().MainMenu()
