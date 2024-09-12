from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        my_font = ("times new roman", 15)

        def load_image(path, size):
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        def place_image(parent, image, x, y, width, height):
            lbl = Label(parent, image=image)
            lbl.place(x=x, y=y, width=width, height=height)
            return lbl

        def create_label(parent, text, row, column, font, bg, padx=4, pady=4, sticky=W):
            lbl = Label(parent, text=text, font=font, bg=bg)
            lbl.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
            return lbl

        # First Image
        self.photon = load_image(r"Images/face.jpeg", (640, 200))
        place_image(self.root, self.photon, 0, 0, 640, 200)

        # Second Image
        self.photoimg1 = load_image(r"images/Gd Goenka Logo.jpg", (630, 200))
        place_image(self.root, self.photoimg1, 640, 0, 640, 200)

        # Third Image
        self.photoimg2 = load_image(r"Images/face.jpeg", (640, 200))
        place_image(self.root, self.photoimg2, 1280, 0, 640, 200)

        # BG Image
        self.photoimg3 = load_image(r"Images/GD Goenka University.jpg", (1920, 880))
        bg_img = place_image(self.root, self.photoimg3, 0, 200, 1920, 880)

        title_lbl = Label(
            bg_img,
            text="DEVELOPERS",
            font=("times new roman", 35, "bold"),
            bg="blue",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1920, height=50)

        def create_section(parent, x, y, width, height, img_path, details):
            frame = Frame(parent, bd=2, relief=RIDGE, bg="white")
            frame.place(x=x, y=y, width=width, height=height)

            photo = load_image(img_path, (200, 200))
            place_image(frame, photo, 490, 5, 200, 200)

            for i, detail in enumerate(details):
                create_label(frame, detail, i, 0, my_font, "white")

        # Witch section
        create_section(
            bg_img, 100, 100, 700, 215, r"Images/Prakriti Raj.jpg",
            [
                "Name: Prakriti Raj",
                "Enrollment No: 220160212099",
                "Course: BCA",
                "Role: Report Management",
                "E-Mail: 220160212099.prakriti@gdgu.org",
                "Skills: "
            ]
        )

        # Wizard-1 section - Rachit Jain
        create_section(
            bg_img, 1100, 100, 700, 215, r"images/Rachit Jain.jpg",
            [
                "Name: Rachit Jain",
                "Enrollment No: 220160212042",
                "Course: BCA",
                "Role: Coder",
                "E-Mail: 220160212042.rachit@gdgu.org",
                "Skills: Python with DSA, Full Stack Web Dev"
            ]
        )

        # Wizard-2 section - Rhythm
        create_section(
            bg_img, 100, 340, 700, 215, r"Images/Rhythm Gupta.jpeg",
            [
                "Name: Rhythm",
                "Enrollment No: 220160212076",
                "Course: BCA",
                "Role: Leader, Coder",
                "E-Mail: 220160212076.rhythm@gdgu.org",
                "Skills: Font-end Web Dev, Python, Management"
            ]
        )

        # Wizard-3 section - Rahul Sehraya
        create_section(
            bg_img, 1100, 340, 700, 215, r"images/Rahul Sehraya.jpg",
            [
                "Name: Rahul Sehraya",
                "Enrollment No: 220160212023",
                "Course: BCA",
                "Role: Coder, Report Management",
                "E-Mail: 220160212023.rahul@gdgu.org",
                "Skills: "
            ]
        )

        # Mentor section
        create_section(
            bg_img, 605, 600, 700, 215, r"Images/Prakriti Raj.jpg",
            [
                "Name: Mrs. Manka Sharma",
                "Position: Assistant Professor GD Goenka University",
                "E-Mail: manka.sharma@gdgu.org",
                "Role: Mentor",
                "Skills: Python Programming, AI/ML, Data Analytics"
            ]
        )

def main() -> None:
    root = Tk()
    obj = Developer(root)
    root.mainloop()

if __name__ == "__main__":
    main()