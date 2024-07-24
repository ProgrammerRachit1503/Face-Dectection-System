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
  # def __init__(self, root) -> None:
  #   self.root = root
  #   self.root.geometry("1920x1080+0+0")
  #   self.root.title("Student Details")


  #   title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="blue", fg="red")
  #   title_lbl.place(x=0, y=0, width=1920, height=50)

  #   # ========== Top Image ===============
  #   img_top = Image.open(r"Images/train2.jfif")  #change the image
  #   img_top = img_top.resize((1920, 300), Image.LANCZOS)
  #   self.photoimg_top = ImageTk.PhotoImage(img_top)

  #   f_lbl = Label(self.root, image = self.photoimg_top)
  #   f_lbl.place(x=0, y=50, width=1920, height=300)

    
  #   # ============= Train_Button =================
  #   b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier, font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
  #   b1_1.place(x=0, y=350, width=1920, height=50)

  #   # ===========Bottom Image ===================
  #   img_bottom = Image.open(r"Images/crowd1.jfif")  #change the image
  #   img_bottom = img_bottom.resize((1920, 730), Image.LANCZOS)
  #   self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

  #   f_lbl = Label(self.root, image = self.photoimg_bottom)
  #   f_lbl.place(x=0, y=400, width=1920, height=730)
  
  # def train_classifier(self):
  #   data_dir = "data"  # Assuming the data directory exists

  #   paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg") or file.endswith(".png")]

  #   faces = []
  #   ids = []

  #   for image_path in paths:
  #     try:
  #       img = Image.open(image_path).convert('L')
  #       imageNp = np.array(img, 'uint8')

  #       id_str = os.path.splitext(os.path.basename(image_path))[0].split("_")[1]
  #       id = int(id_str)

  #       faces.append(imageNp)
  #       ids.append(id)

  #       cv2.imshow("Training", imageNp)
  #       cv2.waitKey(1) 
      
  #     except FileNotFoundError as e:
  #       print(f"Error: File not found: {image_path}")

  #   # Ensure data has been loaded
  #   if not faces:
  #     print("Error: No images found in the data directory.")
  #     return

  #   # Convert lists to NumPy arrays for training
  #   faces_np = np.array(faces)
  #   ids_np = np.array(ids)

  #   # Train the classifier
  #   clf = cv2.face.LBPHFaceRecognizer_create()
  #   clf.train(faces_np, ids_np)

  #   # Save the classifier
  #   clf.write("classifier.xml")
  #   cv2.destroyAllWindows()
  #   messagebox.showinfo("Result", "Training dataset completed!")



  def train_classifier(self):
    data_dir = "data"  # Assuming the data directory exists

    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(data_dir):
      if filename.endswith(".jpg") or filename.endswith(".png"):
        # Improved filename parsing (assuming format: user_<id>_<Enrollment_No>_<img_id>)
        try:
          name, _, _, _ = filename.split("_")
          img_path = os.path.join(data_dir, filename)
          img = face_recognition.load_image_file(img_path)
          face_encoding = face_recognition.face_encodings(img)[0]  # Assume one face per image
          known_face_encodings.append(face_encoding)
          known_face_names.append(name)
          cv2.imshow("Training", face_encoding)  # Display for training visualization (optional)
          cv2.waitKey(1)  # Wait briefly (non-blocking)
        
        except ValueError:
          print(f"Error parsing filename: {filename}. Skipping.")

    if not known_face_encodings:
        print("Error: No valid image files found in the data directory.")
        return

    with open("known_encodings.pickle", "wb") as f:
        pickle.dump((known_face_encodings, known_face_names), f)

    messagebox.showinfo("Result", "Training data processed and saved!")
    cv2.destroyAllWindows()  # Close any open OpenCV windows



def main() -> None:
  root = Tk()
  # obj = Train(root)
  root.mainloop()

if __name__ == "__main__" :
  main()