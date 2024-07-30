from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import face_recognition
import pickle
from datetime import datetime
import csv
import numpy as np


class Attendance:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Face Recognition System")

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
    bg_img = Image.open(r"Images/GD Goenka University.jpg")
    bg_img = bg_img.resize((1920, 880), Image.LANCZOS)
    self.bg_img = ImageTk.PhotoImage(bg_img)

    bg_img = Label(self.root, image = self.bg_img)
    bg_img.place(x=0, y=200, width=1920, height=880)

    title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="blue", fg="red")
    title_lbl.place(x=0, y=0, width=1920, height=50)

    # Start Attendance Button
    img4 = Image.open(r"Images/attendance System.jpeg")
    img4 = img4.resize((300, 300), Image.LANCZOS)
    self.photoimg4 = ImageTk.PhotoImage(img4)

    b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.attendance)
    b1.place(x=300, y=200, width=300, height=300)

    attendance_btn = Button(bg_img, text="Start Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=self.attendance)
    attendance_btn.place(x=300, y=480, width=300, height=40)

    # Check Attendance Button
    img5 = Image.open(r"images/Check Attendance.jpg")
    img5 = img5.resize((300, 300), Image.LANCZOS)
    self.photoimg5 = ImageTk.PhotoImage(img5)

    b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.open_attendance_dir)
    b1.place(x=1250, y=200, width=300, height=300)

    check_attendance_btn = Button(bg_img, text="Check Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=self.open_attendance_dir)
    check_attendance_btn.place(x=1250, y=480, width=300, height=40)

# ========================= Function Buttons =========================
  # ========================= Check Attendance Button =========================
  def open_attendance_dir(self):
    os.startfile("Attendance")

  # ========================= Start Attendance Button =========================
  def load_face_data(self):
    try:
      with open('known_faces.pkl', 'rb') as f:
        known_face_encodings, known_face_names = pickle.load(f)

      return known_face_encodings, known_face_names
    
    except FileNotFoundError:
      print("Face data file not found.")
      return [], []

  def attendance(self):
    known_face_encodings, known_face_names = self.load_face_data()

    if (not known_face_encodings) or (not known_face_names):
      messagebox.showerror("Error", "Please train data before taking attendance")
      return

    Video_Capture = cv2.VideoCapture(0)

    # List of Expected Students
    Students = known_face_names.copy()

    face_locations = []
    face_encodings = []

    # Get the current date and time
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")

    f = open(f"Attendance/{current_date}.csv", "w+", newline="")
    line_writer = csv.writer(f)

    while True:
      _, frame = Video_Capture.read()
      small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
      rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

      # Recognize Faces
      face_locations = face_recognition.face_locations(rgb_small_frame)
      face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

      for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if (matches[best_match_index]):
          name = known_face_names[best_match_index]

        # Add the text on frame if the person is present
        if name in known_face_names:
          font = cv2.FONT_HERSHEY_SIMPLEX
          bottomLeftCorner = (10, 100)
          fontScale = 0.5
          fontColor = (0, 0, 255)
          thickness = 1
          LineType = 2
          cv2.putText(frame, name, bottomLeftCorner, font, fontScale, fontColor, thickness, LineType)

          if name in Students:
            Students.remove(name)
            current_time = now.strftime("%H:%M:%S")
            line_writer.writerow([name, current_time])

        cv2.imshow("Attendance", frame)

      # Press esc key to exit
      if cv2.waitKey(1) & 0xFF == 27:
        break

    Video_Capture.release()
    cv2.destroyAllWindows()
    f.close()

def main() -> None:
  root = Tk()
  obj = Attendance(root)
  root.mainloop()

if __name__ == "__main__" :
  main()