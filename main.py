from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train


class Face_Recognition_System:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Face Recognition System")

    # First Image
    img_1 = Image.open(r"Images/face.jpeg")
    img_1 = img_1.resize((640, 200), Image.LANCZOS)
    self.photo_img_1 = ImageTk.PhotoImage(img_1)

    f_lbl = Label(self.root, image = self.photo_img_1)
    f_lbl.place(x=0, y=0, width=640, height=200)

    # Second Image
    img_2 = Image.open(r"Images/attendance.jpeg")
    img_2 = img_2.resize((640, 200), Image.LANCZOS)
    self.photo_img_2 = ImageTk.PhotoImage(img_2)

    f_lbl = Label(self.root, image = self.photo_img_2)
    f_lbl.place(x=640, y=0, width=640, height=200)

    #  Third Image
    img_3 = Image.open(r"Images/face.jpeg")
    img_3 = img_3.resize((640, 200), Image.LANCZOS)
    self.photo_img_3 = ImageTk.PhotoImage(img_3)

    f_lbl = Label(self.root, image = self.photo_img_3)
    f_lbl.place(x=1280, y=0, width=640, height=200)

    #  BG Image
    img_4 = Image.open(r"Images/GD Goenka University.jpg")
    img_4 = img_4.resize((1920, 880), Image.LANCZOS)
    self.photo_img_4 = ImageTk.PhotoImage(img_4)

    bg_img = Label(self.root, image = self.photo_img_4)
    bg_img.place(x=0, y=200, width=1920, height=880)

    title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="blue", fg="red")
    title_lbl.place(x=0, y=0, width=1920, height=50)

    # Student Button
    img_5 = Image.open(r"Images/students.jpg")
    img_5 = img_5.resize((220, 220), Image.LANCZOS)
    self.photo_img_5 = ImageTk.PhotoImage(img_5)

    btn1 = Button(bg_img, image=self.photo_img_5, cursor="hand2", command=self.student_details)
    btn1.place(x=200, y=100, width=220, height=220)

    btn1_1 = Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=self.student_details)
    btn1_1.place(x=200, y=300, width=220, height=40)

    # Detect Face Button
    img_6 = Image.open(r"Images/detection.jpeg")
    img_6 = img_6.resize((220, 220), Image.LANCZOS)
    self.photo_img_6 = ImageTk.PhotoImage(img_6)

    btn2 = Button(bg_img, image=self.photo_img_6, cursor="hand2")
    btn2.place(x=620, y=100, width=220, height=220)

    btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    btn2_2.place(x=620, y=300, width=220, height=40)

    # Attendance Button
    img_7 = Image.open(r"Images/attendance System.jpeg")
    img_7 = img_7.resize((220, 220), Image.LANCZOS)
    self.photo_img_7 = ImageTk.PhotoImage(img_7)

    btn3 = Button(bg_img, image=self.photo_img_7, cursor="hand2")
    btn3.place(x=1020, y=100, width=220, height=220)

    btn3_3 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    btn3_3.place(x=1020, y=300, width=220, height=40)

    # Help Button
    img_8 = Image.open(r"Images/help.png")
    img_8 = img_8.resize((220, 220), Image.LANCZOS)
    self.photo_img_8 = ImageTk.PhotoImage(img_8)

    btn4 = Button(bg_img, image=self.photo_img_8, cursor="hand2")
    btn4.place(x=1420, y=100, width=220, height=220)

    btn4_4 = Button(bg_img, text="Help", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    btn4_4.place(x=1420, y=300, width=220, height=40)

    # Train Face Button
    img_9 = Image.open(r"Images/training.jpeg")
    img_9 = img_9.resize((220, 220), Image.LANCZOS)
    self.photo_img_9 = ImageTk.PhotoImage(img_9)

    btn5 = Button(bg_img, image=self.photo_img_9, cursor="hand2", command=Train.train_classifier)
    btn5.place(x=200, y=450, width=220, height=220)

    btn5_5 = Button(bg_img, text="Train Face", cursor="hand2", command=Train.train_classifier, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    btn5_5.place(x=200, y=650, width=220, height=40)

    # Photos Button
    img_10 = Image.open(r"images/multi face.jpg")
    img_10 = img_10.resize((220, 220), Image.LANCZOS)
    self.photo_img_10 = ImageTk.PhotoImage(img_10)

    btn6 = Button(bg_img, image=self.photo_img_10, cursor="hand2",command=self.open_img)
    btn6.place(x=620, y=450, width=220, height=220)

    btn6_6 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    btn6_6.place(x=620, y=650, width=220, height=40)

    # Developer Button
    img_11 = Image.open(r"Images/developer.webp")
    img_11 = img_11.resize((220, 220), Image.LANCZOS)
    self.photo_img_11 = ImageTk.PhotoImage(img_11)

    btn7 = Button(bg_img, image=self.photo_img_11, cursor="hand2")
    btn7.place(x=1020, y=450, width=220, height=220)

    btn7_7 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    btn7_7.place(x=1020, y=650, width=220, height=40)

    # Exit Button
    img_12 = Image.open(r"Images/exit.jpeg")
    img_12 = img_12.resize((220, 220), Image.LANCZOS)
    self.photo_img_12 = ImageTk.PhotoImage(img_12)

    btn8 = Button(bg_img, image=self.photo_img_12, cursor="hand2")
    btn8.place(x=1420, y=450, width=220, height=220)

    btn8_8 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    btn8_8.place(x=1420, y=650, width=220, height=40)


  def open_img(self):
    os.startfile("data")

  # ================ Function Buttons ================
  def student_details(self):
    self.new_window = Toplevel(self.root)
    self.app = Student(self.new_window)

  def train_data(self):
    self.new_window = Toplevel(self.root)
    self.app = Train(self.new_window)


def main() -> None:
  root = Tk()
  obj = Face_Recognition_System(root)
  root.mainloop()

if __name__ == "__main__" :
  main()