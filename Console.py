from tkinter import *


class Console:
    window = ""

    def __init__(self):
        # name_str = "V  i  s  i  o  r"
        # self.window.wait_visibility()
        # self.window.config(bg="dodger blue")
        # self.window.wm_attributes("-transparent","dodger blue")
        self.window = Tk()

    def MainMenu(self):
        try:
            # self.window.wait_visibility()
            self.window.config(bg="black")
            # self.window.wm_attributes("-transparent","dodger blue")
            self.window.overrideredirect(1)
            w_height, w_width = 360, 360
            self.window.geometry(f"{w_height}x{w_width}")
            width = self.window.winfo_screenwidth()
            height = self.window.winfo_screenheight()
            print(f"width x height -> {width}x{height}")
            self.window.geometry(f"+{abs(w_width // 2 - width // 2)}+{abs(w_height // 2 - height // 2)}")
            Label(self.window, text="V  i  s  i  o  r\n console", bg="black", fg="#2ade2a", font=("Courier ", 20)).pack(
                side="top",
                pady="10",
                expand=False)

            Button(self.window, text="Exit ", command=self.window.destroy, width=5, bg="red", fg="white",
                   borderwidth=0).place(relx=0.9, rely=0.0)
            Button(self.window, text="\nRun Tests\n", command=self.window.destroy, width=20, bg="#2ade2a",
                   fg="black", borderwidth=1).place(relx=0.3, rely=0.7)
            Button(self.window, text="Remote\n Controller\n Mode", command=self.window.destroy, width=15, bg="#2ade2a",
                   fg="black",
                   borderwidth=2).place(relx=0.1, rely=0.4)
            Button(self.window, text="Autonomous\n Controlled\n Mode", command=self.window.destroy, width=15,
                   bg="#2ade2a",
                   fg="black",
                   borderwidth=2).place(relx=0.6, rely=0.4)
            self.window.mainloop()
        except Exception as e:
            print(f"Exception in <Function> MainMenu - <Class> Console - <File> Console.py --> {e}")
            pass

    def __del__(self):
        try:
            self.window.destroy()
        except:
            pass


if __name__ == "__main__":
    Console().MainMenu()
