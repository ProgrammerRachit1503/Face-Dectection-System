from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import face_recognition
import pickle
import mysql.connector
import numpy as np


class Face_Recognition:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Face Recognition System")


    title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black", fg="white")
    title_lbl.place(x=0, y=0, width=1920, height=50)

# 1st image
    img_1=Image.open(r"images\face.jpeg")
    img_1=img_1.resize((890, 1080), Image.LANCZOS)
    self.photo_img_1=ImageTk.PhotoImage(img_1)

    f_lbl=Label(self.root, image=self.photo_img_1)
    f_lbl.place(x=0, y=50, width=890, height=1080)

# 2nd inage
    img_2=Image.open(r"images\download01.jpeg")
    img_2=img_2.resize((1090, 1080), Image.LANCZOS)
    self.photo_img_2=ImageTk.PhotoImage(img_2)

    f_lbl=Label(self.root, image=self.photo_img_2)
    f_lbl.place(x=890, y=50, width=1090, height=1080)

# button
    btn_1 = Button(f_lbl, text="Face Recognition",command=self.recognize_face, cursor="hand2", font=("times new roman", 15, "bold"),bg="black", fg="white")
    btn_1.place(x=350, y=880, width=350, height=50)

  # ====================face_recognition==============================
  # def recognition(self):
  #   def draw_boundries(img, classifier, scale_factor, minNeighbors, color, text, clf):
  #     features=classifier.detectMultiScale(img, scale_factor, minNeighbors)

  #     coord=[]
  #     for(x,y,w,h) in features:
  #       cv2.rectangle(img(x,y), (x+w+50, y+h+50), (0,255,1), 3)
  #       id,predict=clf.predict(img[y:y+h+50, x:x+w+50])


  def recognize_face(img_path):
      # Load the trained model
      with open("known_faces.pkl", "rb") as f:
          known_face_encodings, known_face_names = pickle.load(f)

      # Load the image
      image = face_recognition.load_image_file(img_path)

      # Find faces in the image
      face_locations = face_recognition.face_locations(image)
      face_encodings = face_recognition.face_encodings(image, face_locations)

      for face_encoding in face_encodings:
          # See if the face is a match for the known faces
          matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
          name = "Unknown"

          # If a match was found in known_face_encodings, just use the first one.
          if True in matches:
              first_match_index = matches.index(True)
              name = known_face_names[first_match_index]

          # Or instead of just the first match, get all matches and find the one with largest distance
          # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
          # best_match_index = np.argmin(face_distances)
          # if matches[best_match_index]:
          #     name = known_face_names[best_match_index]

          # Do something with the face name, like print it or display it on the image
          print(f"I think this face is {name}")

          # Draw a box around the face
          top, right, bottom, left = face_locations[0]
          cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
          cv2.putText(image, name, (left + 6, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

      # Display the image
      cv2.imshow("Image", image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()



def main() -> None:
  root = Tk()
  obj = Face_Recognition(root)
  root.mainloop()

if __name__ == "__main__" :
  main()