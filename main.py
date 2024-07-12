from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student


class Face_Recognition_System:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Face Recognition System")

    # First Image
    img = Image.open(r"Images/face.jpeg")
    img = img.resize((640, 200), Image.LANCZOS)
    self.photon = ImageTk.PhotoImage(img)

    f_lbl = Label(self.root, image = self.photon)
    f_lbl.place(x=0, y=0, width=640, height=200)

    # Second Image
    img1 = Image.open(r"Images/attendance.jpeg")
    img1 = img1.resize((640, 200), Image.LANCZOS)
    self.photoimg1 = ImageTk.PhotoImage(img1)

    f_lbl = Label(self.root, image = self.photoimg1)
    f_lbl.place(x=640, y=0, width=640, height=200)

    #  Third Image
    img2 = Image.open(r"Images/face.jpeg")
    img2 = img2.resize((640, 200), Image.LANCZOS)
    self.photoimg2 = ImageTk.PhotoImage(img2)

    f_lbl = Label(self.root, image = self.photoimg2)
    f_lbl.place(x=1280, y=0, width=640, height=200)

    #  BG Image
    img3 = Image.open(r"Images/GD Goenka University.jpg")
    img3 = img3.resize((1920, 880), Image.LANCZOS)
    self.photoimg3 = ImageTk.PhotoImage(img3)

    bg_img = Label(self.root, image = self.photoimg3)
    bg_img.place(x=0, y=200, width=1920, height=880)

    title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="blue", fg="red")
    title_lbl.place(x=0, y=0, width=1920, height=50)

    # Student Button
    img4 = Image.open(r"Images/students.jpg")
    img4 = img4.resize((220, 220), Image.LANCZOS)
    self.photoimg4 = ImageTk.PhotoImage(img4)

    b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.student_details)
    b1.place(x=200, y=100, width=220, height=220)

    b1_1 = Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=self.student_details)
    b1_1.place(x=200, y=300, width=220, height=40)

    # Detect Face Button
    img5 = Image.open(r"Images/detection.jpeg")
    img5 = img5.resize((220, 220), Image.LANCZOS)
    self.photoimg5 = ImageTk.PhotoImage(img5)

    b2 = Button(bg_img, image=self.photoimg5, cursor="hand2")
    b2.place(x=620, y=100, width=220, height=220)

    b2_2 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    b2_2.place(x=620, y=300, width=220, height=40)

    # Attendance Button
    img6 = Image.open(r"Images/attendance System.jpeg")
    img6 = img6.resize((220, 220), Image.LANCZOS)
    self.photoimg6 = ImageTk.PhotoImage(img6)

    b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
    b3.place(x=1020, y=100, width=220, height=220)

    b3_3 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    b3_3.place(x=1020, y=300, width=220, height=40)

    # Help Button
    img7 = Image.open(r"Images/help.png")
    img7 = img7.resize((220, 220), Image.LANCZOS)
    self.photoimg7 = ImageTk.PhotoImage(img7)

    b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
    b4.place(x=1420, y=100, width=220, height=220)

    b4_4 = Button(bg_img, text="Help", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    b4_4.place(x=1420, y=300, width=220, height=40)

    # Train Face Button
    img8 = Image.open(r"Images/training.jpeg")
    img8 = img8.resize((220, 220), Image.LANCZOS)
    self.photoimg8 = ImageTk.PhotoImage(img8)

    b5 = Button(bg_img, image=self.photoimg8, cursor="hand2")
    b5.place(x=200, y=450, width=220, height=220)

    b5_5 = Button(bg_img, text="Train Face", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    b5_5.place(x=200, y=650, width=220, height=40)

    # Photos Button
    img9 = Image.open(r"images/multi face.jpg")
    img9 = img9.resize((220, 220), Image.LANCZOS)
    self.photoimg9 = ImageTk.PhotoImage(img9)

    b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
    b6.place(x=620, y=450, width=220, height=220)

    b6_6 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    b6_6.place(x=620, y=650, width=220, height=40)

    # Developer Button
    img10 = Image.open(r"Images/developer.webp")
    img10 = img10.resize((220, 220), Image.LANCZOS)
    self.photoimg10 = ImageTk.PhotoImage(img10)

    b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
    b7.place(x=1020, y=450, width=220, height=220)

    b7_6 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    b7_6.place(x=1020, y=650, width=220, height=40)

    # Exit Button
    img11 = Image.open(r"Images/exit.jpeg")
    img11 = img11.resize((220, 220), Image.LANCZOS)
    self.photoimg11 = ImageTk.PhotoImage(img11)

    b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
    b8.place(x=1420, y=450, width=220, height=220)

    b8_6 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
    b8_6.place(x=1420, y=650, width=220, height=40)

  # ================ Function Buttons ================
  def student_details(self):
    self.new_window = Toplevel(self.root)
    self.app = Student(self.new_window)


def main() -> None:
  root = Tk()
  obj = Face_Recognition_System(root)
  root.mainloop()

if __name__ == "__main__" :
  main()