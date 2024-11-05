from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import face_recognition
import pickle
from student import Student
from attendance import Attendance
from developer import Developer


class Face_Recognition_System:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        fonts = ("times new roman", 15, "bold")

        def load_image(path, size):
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        def create_button(image, text, x, y, command):
            btn_image = Button(bg_img, image=image, cursor="hand2", command=command)
            btn_image.place(x=x, y=y, width=220, height=220)
            btn_text = Button(
                bg_img,
                text=text,
                cursor="hand2",
                font=fonts,
                bg="darkblue",
                fg="white",
                command=command,
            )
            btn_text.place(x=x, y=y + 200, width=220, height=40)

        # First Image
        self.photoimg = load_image(r"Images/face.jpeg", (640, 200))
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=640, height=200)

        # Second Image
        self.photoimg1 = load_image(r"images/Gd Goenka Logo.jpg", (630, 200))
        Label(self.root, image=self.photoimg1).place(x=640, y=0, width=640, height=200)

        # Third Image
        self.photoimg2 = load_image(r"Images/face.jpeg", (640, 200))
        Label(self.root, image=self.photoimg2).place(x=1280, y=0, width=640, height=200)

        # BG Image
        self.photoimg3 = load_image(r"Images/GD Goenka University.jpg", (1920, 880))
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1920, height=880)

        # Title Label
        Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="blue",
            fg="red",
        ).place(x=0, y=0, width=1920, height=50)

        # Buttons
        self.photoimg4 = load_image(r"Images/students.jpg", (220, 220))
        create_button(self.photoimg4, "Student Details", 200, 100, self.student_details)

        self.photoimg6 = load_image(r"Images/attendance System.jpeg", (220, 220))
        create_button(self.photoimg6, "Attendance", 820, 100, self.attendance_btn)

        self.photoimg8 = load_image(r"Images/training.jpeg", (220, 220))
        create_button(self.photoimg8, "Train Face", 200, 450, self.train_classifier)

        self.photoimg9 = load_image(r"images/multi face.jpg", (220, 220))
        create_button(self.photoimg9, "Photos", 820, 450, self.open_data_dir)

        self.photoimg10 = load_image(r"Images/developer.webp", (220, 220))
        create_button(self.photoimg10, "Developer", 1420, 100, self.dev_btn)

        self.photoimg11 = load_image(r"Images/exit.jpeg", (220, 220))
        create_button(self.photoimg11, "Exit", 1420, 450, root.destroy)

    # ========================= Function Buttons ===============================
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

    # ========================= Developer Button =========================
    def dev_btn(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

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
            if student_img.endswith((".jpg", ".png", ".jpeg")):
                img = read_img(f"{data_dir}/{student_img}")

                img_encoding = face_recognition.face_encodings(img)[0]

                known_face_encodings.append(img_encoding)
                # converts filename format student_<Enrollment Number>_<Student Name>_.jpg ==> <Enrollment Number>_<Student Name>
                known_face_names.append("_".join(student_img.split("_")[1:3]))

        if not known_face_encodings:
            print("Error: No valid image files found in the data directory.")
            messagebox.showerror(
                "Error", "No valid image files found in the data directory."
            )
            return

        file_path = "known_faces.pkl"
        if os.path.exists(file_path):
            os.remove(file_path)

        with open("known_faces.pkl", "wb") as f:
            pickle.dump((known_face_encodings, known_face_names), f)

        messagebox.showinfo("Success", "Training data completed.")


def main() -> None:
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


if __name__ == "__main__":
    main()
