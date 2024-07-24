from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
import face_recognition
import pickle


class Train:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Student Details")


    title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="blue", fg="red")
    title_lbl.place(x=0, y=0, width=1920, height=50)

    # ========== Top Image ===============
    img_top = Image.open(r"Images/train2.jfif")  #change the image
    img_top = img_top.resize((1920, 300), Image.LANCZOS)
    self.photoimg_top = ImageTk.PhotoImage(img_top)

    f_lbl = Label(self.root, image = self.photoimg_top)
    f_lbl.place(x=0, y=50, width=1920, height=300)

    
    # ============= Train_Button =================
    b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier, font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
    b1_1.place(x=0, y=350, width=1920, height=50)

    # ===========Bottom Image ===================
    img_bottom = Image.open(r"Images/crowd1.jfif")  #change the image
    img_bottom = img_bottom.resize((1920, 730), Image.LANCZOS)
    self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

    f_lbl = Label(self.root, image = self.photoimg_bottom)
    f_lbl.place(x=0, y=400, width=1920, height=730)

  def train_classifier(self):
    data_dir = "data"

    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(data_dir):
      if filename.endswith(".jpg"):
        pass

    if not known_face_encodings:
      print("Error: No valid image files found in the data directory.")
      return

    with open("known_encodings.pickle", "wb") as f:
      pickle.dump((known_face_encodings, known_face_names), f)

    messagebox.showinfo("Result", "Training data processed and saved!")
    cv2.destroyAllWindows()  # Close any open OpenCV windows




def main() -> None:
  root = Tk()
  obj = Train(root)
  root.mainloop()

if __name__ == "__main__" :
  main()