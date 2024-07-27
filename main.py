from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
from attendance import Attendance
import cv2
import os
import face_recognition
import pickle


class Face_Recognition_System:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Face Recognition System")
    
    fonts = ("times new roman", 15, "bold")

    # First Image
    img = Image.open(r"Images/face.jpeg")
    img = img.resize((640, 200), Image.LANCZOS)
    self.photoimg = ImageTk.PhotoImage(img)

    f_lbl = Label(self.root, image = self.photoimg)
    f_lbl.place(x=0, y=0, width=640, height=200)

    # Second Image
    img1 = Image.open(r"images/Gd Goenka Logo.jpg")
    img1 = img1.resize((630, 200), Image.LANCZOS)
    self.photoimg1 = ImageTk.PhotoImage(img1)

    f_lbl = Label(self.root, image = self.photoimg1)
    f_lbl.place(x=640, y=0, width=640, height=200)

    #  Third Image
    self.photoimg2 = ImageTk.PhotoImage(img)

    f_lbl = Label(self.root, image = self.photoimg2)
    f_lbl.place(x=1280, y=0, width=640, height=200)

    #  BG Image
    img3 = Image.open(r"Images/GD Goenka University.jpg")
    img3 = img3.resize((1920, 880), Image.LANCZOS)
    self.photoimg3 = ImageTk.PhotoImage(img3)

    bg_img = Label(self.root, image = self.photoimg3)
    bg_img.place(x=0, y=200, width=1920, height=880)

    # Title Label
    title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="blue", fg="red")
    title_lbl.place(x=0, y=0, width=1920, height=50)

    # Student Button
    img4 = Image.open(r"Images/students.jpg")
    img4 = img4.resize((220, 220), Image.LANCZOS)
    self.photoimg4 = ImageTk.PhotoImage(img4)

    b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.student_details)
    b1.place(x=200, y=100, width=220, height=220)

    b1_1 = Button(bg_img, text="Student Details", cursor="hand2", font=fonts, bg="darkblue", fg="white", command=self.student_details)
    b1_1.place(x=200, y=300, width=220, height=40)

    # Attendance Button
    img6 = Image.open(r"Images/attendance System.jpeg")
    img6 = img6.resize((220, 220), Image.LANCZOS)
    self.photoimg6 = ImageTk.PhotoImage(img6)

    b3 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_btn)
    b3.place(x=820, y=100, width=220, height=220)

    b3_3 = Button(bg_img, text="Attendance", cursor="hand2", font=fonts, bg="darkblue", fg="white", command=self.attendance_btn)
    b3_3.place(x=820, y=300, width=220, height=40)

    # Train Face Button
    img8 = Image.open(r"Images/training.jpeg")
    img8 = img8.resize((220, 220), Image.LANCZOS)
    self.photoimg8 = ImageTk.PhotoImage(img8)

    b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_classifier)
    b5.place(x=200, y=450, width=220, height=220)

    b5_5 = Button(bg_img, text="Train Face", cursor="hand2", command=self.train_classifier, font=fonts, bg="darkblue", fg="white")
    b5_5.place(x=200, y=650, width=220, height=40)

    # Photos Button
    img9 = Image.open(r"images/multi face.jpg")
    img9 = img9.resize((220, 220), Image.LANCZOS)
    self.photoimg9 = ImageTk.PhotoImage(img9)

    b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_data_dir)
    b6.place(x=820, y=450, width=220, height=220)

    b6_6 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_data_dir, font=fonts, bg="darkblue", fg="white")
    b6_6.place(x=820, y=650, width=220, height=40)

    # Developer Button
    img10 = Image.open(r"Images/developer.webp")
    img10 = img10.resize((220, 220), Image.LANCZOS)
    self.photoimg10 = ImageTk.PhotoImage(img10)

    b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
    b7.place(x=1420, y=100, width=220, height=220)

    b7_6 = Button(bg_img, text="Developer", cursor="hand2", font=fonts, bg="darkblue", fg="white")
    b7_6.place(x=1420, y=300, width=220, height=40)

    # Exit Button
    img11 = Image.open(r"Images/exit.jpeg")
    img11 = img11.resize((220, 220), Image.LANCZOS)
    self.photoimg11 = ImageTk.PhotoImage(img11)

    b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
    b8.place(x=1420, y=450, width=220, height=220)

    b8_6 = Button(bg_img, text="Exit", cursor="hand2", font=fonts, bg="darkblue", fg="white")
    b8_6.place(x=1420, y=650, width=220, height=40)

# ========================= Function Buttons =========================
  # ========================= Student Details Button =========================
  def student_details(self):
    self.new_window = Toplevel(self.root)
    self.app = Student(self.new_window)

  # ========================= Photos Button =========================
  def open_data_dir(self):
    os.startfile("data")

  # ========================= Attendance Button =========================
  def attendance_btn(self):
    self.new_window = Toplevel(self.root)
    self.app = Attendance(self.new_window)

  # ========================= Train Data Button =========================
  def train_classifier(self):
    def read_img(path):
      img = cv2.imread(path)
      (h, w) = img.shape[:2]
      width = 500
      ratio = width / float(w)
      height = int(h * ratio)
      return cv2.resize(img, (width, height))

    data_dir = "data"

    known_face_encodings = []
    known_face_names = []

    for student_img in os.listdir(data_dir):
      img = read_img(f"{data_dir}/{student_img}")
      
      img_encoding = face_recognition.face_encodings(img)[0]
      
      known_face_encodings.append(img_encoding)
      # converts filename format student_<Enrollment Number>_<Student Name>_.jpg ==> <Enrollment Number>_<Student Name> 
      known_face_names.append("_".join(student_img.split("_")[1:3]))

    if not known_face_encodings:
      print("Error: No valid image files found in the data directory.")
      messagebox.showerror("Error","No valid image files found in the data directory.")
      return

    with open("known_faces.pkl", "wb") as f:
      pickle.dump((known_face_encodings, known_face_names), f)
    
    messagebox.showinfo("Success","Training data completed.")


def main() -> None:
  root = Tk()
  obj = Face_Recognition_System(root)
  root.mainloop()

if __name__ == "__main__" :
  main()