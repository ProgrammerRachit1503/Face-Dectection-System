from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


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

        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_clasifier, font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=350, width=1980, height=50)

        # ===========Bottom Image ===================
        img_bottom = Image.open(r"Images/crowd1.jfif")  #change the image
        img_bottom = img_bottom.resize((1920, 730), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image = self.photoimg_bottom)
        f_lbl.place(x=0, y=400, width=1920, height=730)

  def train_clasifier(self):
     data_dir=("data")
     path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

     faces=[]
     ids=[]

     for image in path:
        img=Image.open(image).convert('L')  # Gray scale image
        imageNp=np.array(img, 'uint8')
        id=int(os.path.split(image)[1].split('.')[1])


        faces.append(imageNp)
        ids.append(id)
        cv2.imshow("Training", imageNp)
        cv2.wait(1)==13
     ids-np.array(ids)

     #================= Train the classifier and save ===================
     clf=cv2.face.LBPHFaceRecognizer_create()
     clf.train(faces, ids)
     clf.write("classifier.xml")
     cv2.destroyAllWindows()
     messagebox.showinfo("Result", "Training dataset completed !!!")





def main() -> None:
  root = Tk()
  obj = Train(root)
  root.mainloop()

if __name__ == "__main__" :
  main()