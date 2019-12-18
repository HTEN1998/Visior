import cv2
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from os import path
import os


class RcModeController:
    window = ""
    vid = ""
    width = 0
    height = 0
    canvas = ""
    delay = 15
    photo = ""
    snapshot = ""
    image_count = 0

    def __init__(self):
        try:
            self.window = Tk()
            self.window.geometry("620x580")
            self.window.resizable(0, 0)
            self.window.config(bg="black")
            w_height, w_width = 620, 620
            self.window.geometry(f"{w_height}x{w_width}")
            width = self.window.winfo_screenwidth()
            height = self.window.winfo_screenheight()
            print(f"width x height -> {width}x{height}")
            self.window.geometry(f"+{abs(w_width // 2 - width // 2)}+{abs(w_height // 2 - height // 2)}")
            self.window.overrideredirect(1)
            self.width = 620  # self.window.winfo_screenwidth()
            self.height = 620  # self.window.winfo_screenheight()
            print(f"width x height -> {360}x{360}")
            if not path.exists("./SnapShots"):
                os.mkdir("./SnapShots")
            else:
                self.ReadPresentImages()
        except Exception as e:
            print(f"Exception in <Function> __init__ - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def ReadPresentImages(self):
        imglist = os.listdir("./Snapshots/")
        first_split = img_names[::-1].split("_")
        second_split = first_split[1].split(".")
            self.image_count = int(second_split[0])
        print(f"image_counter -> {self.image_count}")

    def StreamScreen(self):
        try:
            self.vid = cv2.VideoCapture(0)
            print("Opencv init ..")
            Label(self.window, font=("Courier bold", 20), text="VISIOR'S On Board Camera Stream", width="1080",
                  fg="#2ade2a",
                  bg="black").pack(side="top")
            Button(self.window, font=("Courier bold", 15), text="Exit", command=self.window.destroy, width=5, bg="red",
                   fg="white",
                   borderwidth=0).place(relx=0.9, rely=0.0)
            Button(self.window, font=("Courier bold", 15), text="Snapshot", command=self.SaveFrame, width=45,
                   bg="#2ade2a",
                   fg="black",
                   borderwidth=1).place(relx=0.1, rely=0.6)
            self.canvas = Label(self.window, width=self.width, height=self.height // 2, bg="black")
            self.canvas.pack()
            self.update()
            self.window.mainloop()
        except Exception as e:
            print(f"Exception in <Function> StreamScreen - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def SaveFrame(self):
        try:
            self.image_count += 1
            SSpath = "./SnapShots/snapshot_" + str(self.image_count) + ".jpg"
            cv2.imwrite(SSpath, cv2.cvtColor(self.snapshot, cv2.COLOR_BGR2RGB))
            SavedLoc = Label(self.window, font=("Courier bold underline", 12), text=f"Snapshot Saved in -> {SSpath}",
                             width="1080",
                             fg="white", bg="black")
            SavedLoc.pack(side="bottom")
            self.window.after(1000, SavedLoc.forget)
        except Exception as e:
            print(f"Exception in <Function> SaveFrame - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def get_Frame(self):
        try:
            if self.vid.isOpened():
                ret, frame = self.vid.read()
                return ret, cv2.cvtColor(cv2.resize(frame, None, fx=0.9, fy=1.4), cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(f"Exception in <Function> get_Frame - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def update(self):
        try:
            ret, frame = self.get_Frame()
            self.snapshot = frame
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.configure(image=self.photo)
                self.canvas.image = self.photo
            self.window.after(2, self.update)
        except Exception as e:
            print(f"Exception in <Function> update - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

# if __name__ == "__main__":
#    TkinterCam()
