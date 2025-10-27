import tkinter as tk
from tkinter import Frame, Label, RIDGE, W
from PIL import Image, ImageTk
from PIL.Image import Resampling  # Modern import for resampling filter
import os # Used for robust path handling (optional but good)

class Developer:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        
        # This list is CRUCIAL to hold references to all PhotoImage objects.
        # If you don't store them, Python's garbage collector will discard
        # them, and your images will disappear from the GUI.
        self._image_references = []
        
        # Store common font as an instance variable
        self.card_font = ("times new roman", 15)

        self._setup_window()
        self._create_header()
        self._create_main_body()

    def _setup_window(self):
        """Sets up the main window geometry and title."""
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

    def _load_image(self, path: str, size: tuple[int, int]):
        """
        A helper method to load, resize, and store an image.
        Handles FileNotFoundError by creating a placeholder.
        """
        try:
            # Note: Normalized all paths to use 'images/' (lowercase)
            img = Image.open(path)
            img = img.resize(size, Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            
            # Add to our list to prevent garbage collection
            self._image_references.append(photo_img)
            return photo_img
        
        except FileNotFoundError:
            print(f"Warning: Image file not found at {path}. Creating placeholder.")
            # Create a grey placeholder image
            img = Image.new('RGB', size, color='grey')
            label = f"{size[0]}x{size[1]}\n{os.path.basename(path)}"
            # (We could draw the text on the image, but for simplicity
            # we just return a blank grey box)
            photo_img = ImageTk.PhotoImage(img)
            self._image_references.append(photo_img)
            return photo_img
        
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None

    def _create_header(self):
        """Creates the top header with three images."""
        
        # Left header image
        img_left = self._load_image(r"images/face.jpeg", (640, 200))
        if img_left:
            lbl_left = Label(self.root, image=img_left)
            lbl_left.place(x=0, y=0, width=640, height=200)

        # Center header image
        img_center = self._load_image(r"images/Gd Goenka Logo.jpg", (630, 200))
        if img_center:
            # Note: Original code resized to 630 but placed in a 640-wide widget
            lbl_center = Label(self.root, image=img_center)
            lbl_center.place(x=640, y=0, width=640, height=200)

        # Right header image
        img_right = self._load_image(r"images/face.jpeg", (640, 200))
        if img_right:
            lbl_right = Label(self.root, image=img_right)
            lbl_right.place(x=1280, y=0, width=640, height=200)

    def _create_main_body(self):
        """Creates the background image, title, and all developer/mentor cards."""
        
        # Background Image
        img_bg = self._load_image(r"images/GD Goenka University.jpg", (1920, 880))
        
        # Place background label. It will act as the parent for other widgets.
        bg_label = Label(self.root, image=img_bg)
        bg_label.place(x=0, y=200, width=1920, height=880)

        # Title Label
        title_lbl = Label(
            bg_label,
            text="DEVELOPERS",
            font=("times new roman", 35, "bold"),
            bg="blue",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1920, height=50)

        # --- Developer & Mentor Data ---
        # Separating data from logic makes it easy to add/remove/update people.
        developer_data = [
            {
                "name": "Prakriti Raj",
                "enrollment": "220160212099",
                "course": "BCA",
                "role": "Report Management",
                "email": "220160212099.prakriti@gdgu.org",
                "skills": "", # Original was "Skills: "
                "image_path": r"images/Prakriti Raj.jpg",
                "pos_x": 100,
                "pos_y": 100
            },
            {
                "name": "Rachit Jain",
                "enrollment": "220160212042",
                "course": "BCA",
                "role": "Coder",
                "email": "220160212042.rachit@gdgu.org",
                "skills": "Python with DSA, Full Stack Web Dev",
                "image_path": r"images/Rachit Jain.jpg",
                "pos_x": 1100,
                "pos_y": 100
            },
            {
                "name": "Rhythm",
                "enrollment": "220160212076",
                "course": "BCA",
                "role": "Leader, Coder",
                "email": "220160212076.rhythm@gdgu.org",
                "skills": "Font-end Web Dev, Python, Management",
                "image_path": r"images/Rhythm Gupta.jpeg",
                "pos_x": 100,
                "pos_y": 340
            },
            {
                "name": "Rahul Sehraya",
                "enrollment": "220160212023",
                "course": "BCA",
                "role": "Coder, Report Management",
                "email": "220160212023.rahul@gdgu.org",
                "skills": "", # Original was "Skills: "
                "image_path": r"images/Rahul Sehraya.jpg",
                "pos_x": 1100,
                "pos_y": 340
            }
        ]

        # Loop through the data and create a card for each developer
        for dev in developer_data:
            self._create_developer_card(bg_label, dev)

        # --- Mentor Card ---
        # The mentor card is slightly different, so we handle it separately.
        # We could also make the _create_developer_card function more flexible.
        mentor_data = {
            "name": "Mrs. Manka Sharma",
            "designation": "Position: Assistant Professor GD Goenka University",
            "email": "manka.sharma@gdgu.org",
            "role": "Role: Mentor",
            "skills": "Skills: Python Programming, AI/ML, Data Analytics",
            "image_path": r"images/Gd Goenka Logo.jpg", # Reusing logo
            "pos_x": 605,
            "pos_y": 600
        }
        self._create_mentor_card(bg_label, mentor_data)


    def _create_developer_card(self, parent: tk.Widget, details: dict):
        """
        A reusable method to create a single developer card.
        """
        frame = Frame(parent, bd=2, relief=RIDGE, bg="white")
        frame.place(x=details['pos_x'], y=details['pos_y'], width=700, height=215)

        img = self._load_image(details['image_path'], (200, 200))
        if img:
            img_label = Label(frame, image=img)
            img_label.place(x=490, y=5, width=200, height=200)

        # Create labels from the details dictionary
        labels_info = [
            f"Name: {details['name']}",
            f"Enrollment No: {details['enrollment']}",
            f"Course: {details['course']}",
            f"Role: {details['role']}",
            f"E-Mail: {details['email']}",
            f"Skills: {details['skills']}"
        ]
        
        for i, text in enumerate(labels_info):
            lbl = Label(frame, text=text, font=self.card_font, bg="white")
            lbl.grid(row=i, column=0, padx=4, pady=4, sticky=W)

    def _create_mentor_card(self, parent: tk.Widget, details: dict):
        """
        A specific method for the mentor card, which has different fields.
        """
        frame = Frame(parent, bd=2, relief=RIDGE, bg="white")
        frame.place(x=details['pos_x'], y=details['pos_y'], width=700, height=215)

        img = self._load_image(details['image_path'], (200, 200))
        if img:
            img_label = Label(frame, image=img)
            img_label.place(x=490, y=5, width=200, height=200)

        # Mentor-specific details
        # Note: Some original text already included the prefix (e.g., "Role: ...")
        labels_info = [
            f"Name: {details['name']}",
            details['designation'],
            f"E-Mail: {details['email']}",
            details['role'],
            details['skills']
        ]

        for i, text in enumerate(labels_info):
            lbl = Label(frame, text=text, font=self.card_font, bg="white")
            lbl.grid(row=i, column=0, padx=4, pady=4, sticky=W)

def main() -> None:
    """Main function to initialize and run the application."""
    root = tk.Tk()
    app = Developer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
