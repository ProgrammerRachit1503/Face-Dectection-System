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
import time


class Attendance:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        def load_and_resize_image(path, size):
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        def create_button(parent, image, text, command, x, y, width, height):
            btn_image = Button(parent, image=image, cursor="hand2", command=command)
            btn_image.place(x=x, y=y, width=width, height=height)
            btn_text = Button(
                parent,
                text=text,
                cursor="hand2",
                font=("times new roman", 15, "bold"),
                bg="darkblue",
                fg="white",
                command=command,
            )
            btn_text.place(x=x, y=y + 280, width=width, height=40)

        # First Image
        self.photoimg = load_and_resize_image(r"Images/face.jpeg", (640, 200))
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=640, height=200)

        # Second Image
        self.photoimg1 = load_and_resize_image(r"images/Gd Goenka Logo.jpg", (630, 200))
        Label(self.root, image=self.photoimg1).place(x=640, y=0, width=640, height=200)

        # Third Image
        self.photoimg2 = self.photoimg
        Label(self.root, image=self.photoimg2).place(x=1280, y=0, width=640, height=200)

        # BG Image
        self.bg_img = load_and_resize_image(
            r"Images/GD Goenka University.jpg", (1920, 880)
        )
        bg_img = Label(self.root, image=self.bg_img)
        bg_img.place(x=0, y=200, width=1920, height=880)

        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="blue",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1920, height=50)

        # Start Attendance Button
        self.photoimg4 = load_and_resize_image(
            r"Images/attendance System.jpeg", (300, 300)
        )
        create_button(
            bg_img,
            self.photoimg4,
            "Start Attendance",
            self.attendance,
            300,
            200,
            300,
            300,
        )

        # Check Attendance Button
        self.photoimg5 = load_and_resize_image(
            r"images/Check Attendance.jpg", (300, 300)
        )
        create_button(
            bg_img,
            self.photoimg5,
            "Check Attendance",
            self.open_attendance_dir,
            1250,
            200,
            300,
            300,
        )

    # ========================= Function Buttons =========================
    def open_attendance_dir(self):
        os.startfile("Attendance")

    def load_face_data(self):
        try:
            with open("known_faces.pkl", "rb") as f:
                known_face_encodings, known_face_names = pickle.load(f)
            return known_face_encodings, known_face_names
        except FileNotFoundError:
            return [], []

    def attendance(self):
        known_face_encodings, known_face_names = self.load_face_data()

        if not known_face_encodings or not known_face_names:
            messagebox.showerror("Error", "Please train data before taking attendance")
            return

        video_capture = cv2.VideoCapture(0)
        students = known_face_names.copy()
        face_locations = []
        face_encodings = []

        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")

        with open(f"Attendance/{current_date}.csv", "w+", newline="") as f:
            line_writer = csv.writer(f)

            frame_interval = 5
            frame_count = 0

            while True:
                _, frame = video_capture.read()

                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                if frame_count % frame_interval == 0:
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(
                        rgb_small_frame, face_locations
                    )

                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces(
                            known_face_encodings, face_encoding
                        )
                        face_distance = face_recognition.face_distance(
                            known_face_encodings, face_encoding
                        )
                        best_match_index = np.argmin(face_distance)

                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]

                            cv2.putText(
                                frame,
                                name,
                                (10, 100),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5,
                                (0, 0, 255),
                                1,
                                2,
                            )

                            if name in students:
                                students.remove(name)
                                current_time = now.strftime("%H:%M:%S")
                                line_writer.writerow(
                                    [
                                        name.split("_")[0],
                                        name.split("_")[1],
                                        current_time,
                                    ]
                                )
                    frame_count = 0

                frame_count += 1

                cv2.imshow("Attendance", frame)

                if cv2.waitKey(1) & 0xFF == 27:
                    break

        video_capture.release()
        cv2.destroyAllWindows()


def main() -> None:
    root = Tk()
    obj = Attendance(root)
    root.mainloop()


if __name__ == "__main__":
    main()
