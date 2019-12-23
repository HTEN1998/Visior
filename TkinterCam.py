import cv2
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from os import path
import os
from time import sleep
import keyboard as raw_key
from pynput import keyboard as py_key
#from CameraMotion import CameraMotion

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
    CamUp = ""
    CamDown = ""
    CamLeft = ""
    CamRight = ""
    MoveForward=""
    MoveBackward=""
    TurnLeft=""
    TurnRight=""
    CamMotion = ""


    def __init__(self):
        try:
            self.window = Tk()
            self.window.geometry("620x580")
            self.window.resizable(0, 0)
            self.window.config(bg="black")
            w_height, w_width = 640, 490
            self.window.geometry(f"{w_height}x{w_width}")
            width = self.window.winfo_screenwidth()
            height = self.window.winfo_screenheight()
            print(f"width x height -> {width}x{height}")
            self.window.geometry(f"+{abs(0)}+{abs(0)}")
            self.window.overrideredirect(1)
            self.width = 620  # self.window.winfo_screenwidth()
            self.height = 620  # self.window.winfo_screenheight()
            print(f"width x height -> {360}x{360}")
            self.window.focus()
            #self.CamMotion = CameraMotion()
            #self.CamMotion.ResetCameraPosition()
            
            
            if not path.exists("./SnapShots"):
                os.mkdir("./SnapShots")
            #else:
                #self.ReadPresentImages()
        except Exception as e:
            print(f"Exception in <Function> __init__ - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def ReadPresentImages(self):
        imglist = os.listdir("./Snapshots/")[-1]
        first_split = imglist.split("_")
        second_split = first_split[1].split(".")
        self.image_count = int(second_split[0])
        print(f"image_counter -> {self.image_count}")

    def on_press(self, key):
        b_g = "yellow"
        f_g = "blue"
        border_w=3
        if str(format(key)) == "'w'":
            self.CamUp.config(bg=b_g, fg=f_g,width = 4 , borderwidth=border_w)
        if str(format(key)) == "'s'":
            self.CamDown.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "'a'":
            self.CamLeft.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "'d'":
            self.CamRight.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "Key.up":
            self.MoveForward.config(bg=b_g, fg=f_g,width = 4 , borderwidth=border_w)
        if str(format(key)) == "Key.down":
            self.MoveBackward.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "Key.left":
            self.TurnLeft.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "Key.right":
            self.TurnRight.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)

        print(f"pressed -> {str(format(key))}")

    def on_release(self, key):
        b_g = "#2ade2a"
        f_g = "black"
        border_w=1
        if str(format(key)) == "'w'":
            self.CamUp.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "'s'":
            self.CamDown.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "'a'":
            self.CamLeft.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "'d'":
            self.CamRight.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "Key.up":
            self.MoveForward.config(bg=b_g, fg=f_g,width = 4 , borderwidth=border_w)
        if str(format(key)) == "Key.down":
            self.MoveBackward.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "Key.left":
            self.TurnLeft.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)
        if str(format(key)) == "Key.right":
            self.TurnRight.config(bg=b_g, fg=f_g,width = 4, borderwidth=border_w)

    def StreamScreen(self):
        try:

            self.vid = ""#cv2.VideoCapture(0)
            print("Opencv init ..")
            listerner = py_key.Listener(
                on_press=self.on_press,
                on_release=self.on_release
            )
            listerner.start()
            print("Key Listener started .. ")

            Label(self.window, font=("Courier bold", 20), text="VISIOR'S On Board Camera Stream", width="1080",
                  fg="#2ade2a",
                  bg="black").pack(side="top")
            Button(self.window, font=("Courier bold", 10), text="Exit", command=self.window.destroy, width=4, bg="red",
                   fg="white",
                   borderwidth=0).place(relx=0.91, rely=0.0)
            Button(self.window, font=("Courier bold", 7), text="Snapshot", command=self.SaveFrame, width=108,
                   bg="#2ade2a",
                   fg="black",
                   borderwidth=0).place(relx=0.0, rely=0.6)

            self.CreateCameraButtons()
            self.CreateMovementButton()

            self.canvas = Label(self.window, width = 88, height=15, bg="red")
            self.canvas.pack()
            #self.update()

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



    def CreateCameraButtons(self):
        self.CamUp = Button(self.window, font=("Courier bold", 11), text="Up(W)", width=4,
                            bg="#2ade2a",
                            fg="black",
                            borderwidth=2,highlightthickness=0)
        self.CamUp.place(relx=0.21, rely=0.72)
        self.CamRight = Button(self.window, font=("Courier bold", 11), text="Right(D)", width=4,
                               bg="#2ade2a",
                               fg="black",
                               borderwidth=2,highlightthickness=0)
        self.CamRight.place(relx=0.32, rely=0.8)
        self.CamDown = Button(self.window, font=("Courier bold", 11), text="Down(S)", width=4,
                              bg="#2ade2a",
                              fg="black",
                              borderwidth=2,highlightthickness=0)
        self.CamDown.place(relx=0.21, rely=0.8)
        self.CamLeft = Button(self.window, font=("Courier bold", 11), text="Left(A)", width=4,
                              bg="#2ade2a",
                              fg="black",
                              borderwidth=2,highlightthickness=0)
        self.CamLeft.place(relx=0.1, rely=0.8)

        Label(self.window, font=("Courier bold", 12), text="Camera Control", width=len(" Camera Control "),
              fg="white",
              bg="black").place(relx=0.139, rely=0.89)

    def CreateMovementButton(self):
        self.MoveForward = Button(self.window, font=("Courier bold", 11), text="Front(^)", width=4,
                            bg="#2ade2a",
                            fg="black",
                            borderwidth=2,highlightthickness=0)
        self.MoveForward.place(relx=0.7, rely=0.72)
        self.MoveBackward = Button(self.window, font=("Courier bold", 11), text="Back(!)", width=4,
                                  bg="#2ade2a",
                                  fg="black",
                                  borderwidth=2,highlightthickness=0)
        self.MoveBackward.place(relx=0.7, rely=0.8)
        self.TurnLeft = Button(self.window, font=("Courier bold", 11), text="Left(<)", width=4,
                                   bg="#2ade2a",
                                   fg="black",
                                   borderwidth=2,highlightthickness=0)
        self.TurnLeft.place(relx=0.59, rely=0.8)
        self.TurnRight = Button(self.window, font=("Courier bold", 11), text="Right(>)", width=4,
                                   bg="#2ade2a",
                                   fg="black",
                                   borderwidth=2,highlightthickness=0)
        self.TurnRight.place(relx=0.81, rely=0.8)
        Label(self.window, font=("Courier bold", 12), text="Motion Control", width=len(" Camera Control "),
              fg="white",
              bg="black").place(relx=0.63, rely=0.89)
