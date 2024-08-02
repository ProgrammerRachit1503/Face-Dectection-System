from tkinter import *
from PIL import Image, ImageTk


class Developer:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Face Recognition System")
    
    my_font = ("times new roman", 15)
    
    # First Image
    img = Image.open(r"Images/face.jpeg")
    img = img.resize((640, 200), Image.LANCZOS)
    self.photon = ImageTk.PhotoImage(img)

    f_lbl = Label(self.root, image = self.photon)
    f_lbl.place(x=0, y=0, width=640, height=200)

    # Second Image
    img1 = Image.open(r"images/Gd Goenka Logo.jpg")
    img1 = img1.resize((630, 200), Image.LANCZOS)
    self.photoimg1 = ImageTk.PhotoImage(img1)

    f_lbl = Label(self.root, image = self.photoimg1)
    f_lbl.place(x=640, y=0, width=640, height=200)

    # Third Image
    img2 = Image.open(r"Images/face.jpeg")
    img2 = img2.resize((640, 200), Image.LANCZOS)
    self.photoimg2 = ImageTk.PhotoImage(img2)

    f_lbl = Label(self.root, image = self.photoimg2)
    f_lbl.place(x=1280, y=0, width=640, height=200)

    #  BG Image
    img3 = Image.open(r"Images/GD Goenka University.jpg")
    img3 = img3.resize((1920, 880), Image.LANCZOS)
    self.photoimg3 = ImageTk.PhotoImage(img3)

    bg_img = Label(self.root, image = self.photoimg3)
    bg_img.place(x=0, y=200, width=1920, height=880)

    title_lbl = Label(bg_img, text="DEVELOPERS", font=("times new roman", 35, "bold"), bg="blue", fg="red")
    title_lbl.place(x=0, y=0, width=1920, height=50)


    # Witch section
    witch_Frame=Frame(bg_img,bd=2, relief=RIDGE,bg="white")
    witch_Frame.place(x=100, y=100, width=700,height=215)

    # witch image
    witch_img=Image.open(r"Images/Prakriti Raj.jpg")
    witch_img=witch_img.resize((200,200), Image.LANCZOS)
    self.witch_photo=ImageTk.PhotoImage(witch_img)

    witch=Label(witch_Frame, image=self.witch_photo)
    witch.place(x=490 ,y=5 , width=200, height=200)

    # witch details
    witch_name = Label(witch_Frame, text = "Name: Prakriti Raj", font=my_font, bg="white")
    witch_name.grid(row = 0, column = 0, padx=4, pady=4, sticky=W)

    witch_enrollment_no = Label(witch_Frame, text = "Enrollment No: 220160212099", font=my_font, bg="white")
    witch_enrollment_no.grid(row = 1, column = 0, padx=4, pady=4, sticky=W)

    witch_course = Label(witch_Frame, text = "Course: BCA", font=my_font, bg="white")
    witch_course.grid(row = 2, column = 0, padx=4, pady=4, sticky=W)

    witch_role = Label(witch_Frame, text = "Role: Report Management", font=my_font, bg="white")
    witch_role.grid(row = 3, column = 0, padx=4, pady=4, sticky=W)
    
    witch_mail = Label(witch_Frame, text = "E-Mail: 220160212099.prakriti@gdgu.org", font=my_font, bg="white")
    witch_mail.grid(row = 4, column = 0, padx=4, pady=4, sticky=W)

    witch_skills = Label(witch_Frame, text = "Skills: ", font=my_font, bg="white")
    witch_skills.grid(row = 5, column = 0, padx=4, pady=4, sticky=W)

    # Wizard-1 section - Rachit Jain
    wizard_1_Frame=Frame(bg_img,bd=2, relief=RIDGE,bg="white")
    wizard_1_Frame.place(x=1100, y=100, width=700,height=215)

    # wizard-1 image
    wizard_1_img=Image.open(r"images/Rachit Jain.jpg")
    wizard_1_img=wizard_1_img.resize((200,200), Image.LANCZOS)
    self.wizard_1_photo=ImageTk.PhotoImage(wizard_1_img)

    wizard=Label(wizard_1_Frame, image=self.wizard_1_photo)
    wizard.place(x=490 ,y=5 , width=200, height=200)

    # wizard-1 details
    wizard_1_name = Label(wizard_1_Frame, text = "Name: Rachit Jain", font=my_font, bg="white")
    wizard_1_name.grid(row = 0, column = 0, padx=4, pady=4, sticky=W)

    wizard_1_enrollment_no = Label(wizard_1_Frame, text = "Enrollment No: 220160212042", font=my_font, bg="white")
    wizard_1_enrollment_no.grid(row = 1, column = 0, padx=4, pady=4, sticky=W)

    wizard_1_course = Label(wizard_1_Frame, text = "Course: BCA", font=my_font, bg="white")
    wizard_1_course.grid(row = 2, column = 0, padx=4, pady=4, sticky=W)

    wizard_1_role = Label(wizard_1_Frame, text = "Role: Coder", font=my_font, bg="white")
    wizard_1_role.grid(row = 3, column = 0, padx=4, pady=4, sticky=W)
    
    wizard_1_mail = Label(wizard_1_Frame, text = "E-Mail: 220160212042.rachit@gdgu.org", font=my_font, bg="white")
    wizard_1_mail.grid(row = 4, column = 0, padx=4, pady=4, sticky=W)

    wizard_1_skill = Label(wizard_1_Frame, text = "Skills: Python with DSA, Full Stack Web Dev", font=my_font, bg="white")
    wizard_1_skill.grid(row = 5, column = 0, padx=4, pady=4, sticky=W)


    # Wizard-2 section - Rhythm
    wizard_2_Frame=Frame(bg_img,bd=2, relief=RIDGE,bg="white")
    wizard_2_Frame.place(x=100, y=340, width=700,height=215)

    # wizard-2 image
    wizard_2_img=Image.open(r"Images\WhatsApp Image 2024-07-21 at 12.53.14 PM.jpeg")
    wizard_2_img=wizard_2_img.resize((200,200), Image.LANCZOS)
    self.wizard_2_photo=ImageTk.PhotoImage(wizard_2_img)

    wizard=Label(wizard_2_Frame, image=self.wizard_2_photo)
    wizard.place(x=490 ,y=5 , width=200, height=200)

    # wizard-2 details
    wizard_2_name = Label(wizard_2_Frame, text = "Name: Rhythm", font=my_font, bg="white")
    wizard_2_name.grid(row = 0, column = 0, padx=4, pady=4, sticky=W)

    wizard_2_enrollment_no = Label(wizard_2_Frame, text = "Enrollment No: 220160212076", font=my_font, bg="white")
    wizard_2_enrollment_no.grid(row = 1, column = 0, padx=4, pady=4, sticky=W)

    wizard_2_course = Label(wizard_2_Frame, text = "Course: BCA", font=my_font, bg="white")
    wizard_2_course.grid(row = 2, column = 0, padx=4, pady=4, sticky=W)

    wizard_2_role = Label(wizard_2_Frame, text = "Role: Leader, Coder", font=my_font, bg="white")
    wizard_2_role.grid(row = 3, column = 0, padx=4, pady=4, sticky=W)
    
    wizard_2_mail = Label(wizard_2_Frame, text = "E-Mail: 220160212076.rhythm@gdgu.org", font=my_font, bg="white")
    wizard_2_mail.grid(row = 4, column = 0, padx=4, pady=4, sticky=W)

    wizard_2_skill = Label(wizard_2_Frame, text = "Skills: Font-end Web Dev, Python, Management", font=my_font, bg="white")
    wizard_2_skill.grid(row = 5, column = 0, padx=4, pady=4, sticky=W)


    # Wizard-3 section - Rahul Sehraya
    wizard_3_Frame=Frame(bg_img,bd=2, relief=RIDGE,bg="white")
    wizard_3_Frame.place(x=1100, y=340, width=700,height=215)

    # wizard-3 image
    wizard_3_img=Image.open(r"images/Rahul Sehraya.jpg")
    wizard_3_img=wizard_3_img.resize((200,200), Image.LANCZOS)
    self.wizard_3_photo=ImageTk.PhotoImage(wizard_3_img)

    wizard=Label(wizard_3_Frame, image=self.wizard_3_photo)
    wizard.place(x=490 ,y=5 , width=200, height=200)

    # wizard-3 details
    wizard_3_name = Label(wizard_3_Frame, text = "Name: Rahul Sehraya", font=my_font, bg="white")
    wizard_3_name.grid(row = 0, column = 0, padx=4, pady=4, sticky=W)

    wizard_3_enrollment_no = Label(wizard_3_Frame, text = "Enrollment No: 220160212023", font=my_font, bg="white")
    wizard_3_enrollment_no.grid(row = 1, column = 0, padx=4, pady=4, sticky=W)

    wizard_3_course = Label(wizard_3_Frame, text = "Course: BCA", font=my_font, bg="white")
    wizard_3_course.grid(row = 2, column = 0, padx=4, pady=4, sticky=W)

    wizard_3_role = Label(wizard_3_Frame, text = "Role: Coder, Report Management", font=my_font, bg="white")
    wizard_3_role.grid(row = 3, column = 0, padx=4, pady=4, sticky=W)
    
    wizard_3_mail = Label(wizard_3_Frame, text = "E-Mail: 220160212023cl.rahul@gdgu.org", font=my_font, bg="white")
    wizard_3_mail.grid(row = 4, column = 0, padx=4, pady=4, sticky=W)

    wizard_3_skill = Label(wizard_3_Frame, text = "Skills: ", font=my_font, bg="white")
    wizard_3_skill.grid(row = 5, column = 0, padx=4, pady=4, sticky=W)


    # mentor section
    mentor_Frame=Frame(bg_img,bd=2, relief=RIDGE,bg="white")
    mentor_Frame.place(x=605, y=600, width=700,height=215)

    # mentor image
    mentor_img=Image.open(r"Images/Prakriti Raj.jpg")
    mentor_img=mentor_img.resize((200,200), Image.LANCZOS)
    self.mentor_photo=ImageTk.PhotoImage(mentor_img)

    wizard=Label(mentor_Frame, image=self.mentor_photo)
    wizard.place(x=490 ,y=5 , width=200, height=200)

    # Mentor details
    mentor_name = Label(mentor_Frame, text = "Name: Mrs. Manka Sharma", font=my_font, bg="white")
    mentor_name.grid(row = 0, column = 0, padx=4, pady=4, sticky=W)

    mentor_designation = Label(mentor_Frame, text = "Position: Assistant Professor GD Goenka University", font=my_font, bg="white")
    mentor_designation.grid(row = 1, column = 0, padx=4, pady=4, sticky=W)

    mentor_mail = Label(mentor_Frame, text = "E-Mail: manka.sharma@gdgu.org", font=my_font, bg="white")
    mentor_mail.grid(row = 2, column = 0, padx=4, pady=4, sticky=W)

    mentor_role = Label(mentor_Frame, text = "Role: Mentor", font=my_font, bg="white")
    mentor_role.grid(row = 3, column = 0, padx=4, pady=4, sticky=W)

    mentor_skill = Label(mentor_Frame, text = "Skills: Python Programming, AI/ML, Data Analytics", font=my_font, bg="white")
    mentor_skill.grid(row = 4, column = 0, padx=4, pady=4, sticky=W)


def main() -> None:
  root = Tk()
  obj = Developer(root)
  root.mainloop()

if __name__ == "__main__" :
  main()