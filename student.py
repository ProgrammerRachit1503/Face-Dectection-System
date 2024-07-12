from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Face Recognition System")

    # First Image
    img = Image.open(r"Images/face.jpeg")
    img = img.resize((640, 200), Image.LANCZOS)
    self.photon = ImageTk.PhotoImage(img)

    f_lbl = Label(self.root, image = self.photon)
    f_lbl.place(x=0, y=0, width=640, height=200)

    # Second Image
    img1 = Image.open(r"Images/attendance.jpeg")
    img1 = img1.resize((640, 200), Image.LANCZOS)
    self.photoimg1 = ImageTk.PhotoImage(img1)

    f_lbl = Label(self.root, image = self.photoimg1)
    f_lbl.place(x=640, y=0, width=640, height=200)

    #  Third Image
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

    title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="blue", fg="red")
    title_lbl.place(x=0, y=0, width=1920, height=50)

    # Main Frame
    main_frame = Frame(bg_img, bd=2, bg="pink")
    main_frame.place(x=10, y=60, width=1900, height=780)

    # Left Frame
    left_Frame = LabelFrame(main_frame, bd=2, bg = "White", relief="ridge", text="Student Details", font=("times new roman", 16, "bold") )
    left_Frame.place(x=10, y=10, width=940, height=760)

    img_left = Image.open(r"Images/face.jpeg")  #change the image
    img_left = img_left.resize((920, 230), Image.LANCZOS)
    self.photoimg_left = ImageTk.PhotoImage(img_left)

    f_lbl = Label(left_Frame, image = self.photoimg_left)
    f_lbl.place(x=10, y=0, width=920, height=150)

    # current course
    current_course_Frame = LabelFrame(left_Frame, bd=2, bg = "White", relief="ridge", text="Current Course Information", font=("times new roman", 16, "bold") )
    current_course_Frame.place(x=10, y=160, width=920, height=150)

    # Department
    dep_lbl = Label(current_course_Frame, text = "Department", font=("times new roman", 15, "bold"), bg="white")
    dep_lbl.grid(row = 0, column = 0, padx=10, pady=15, sticky=W)

    dep_combo = ttk.Combobox(current_course_Frame, font=("times new roman", 15, "bold"), state="readonly")
    dep_combo["values"]=("Select the Department","IT","Computers","Medical","Civil","Electrical")
    dep_combo.current(0)
    dep_combo.grid(row = 0, column = 1, padx=5, pady=15, sticky=W)

    #Course
    course_lbl = Label(current_course_Frame, text = "Course", font=("times new roman", 15, "bold"), bg="white")
    course_lbl.grid(row = 0, column = 2, padx=10, pady=15, sticky=W)

    course_combo = ttk.Combobox(current_course_Frame, font=("times new roman", 15, "bold"), state="readonly")
    course_combo["values"]=("Select the Course","B.Tech CSE","BCA (AI/ML)","B.Tech Civil","B.Pharma","B.Tech EE")
    course_combo.current(0)
    course_combo.grid(row = 0, column = 3, padx=5, pady=15, sticky=W)


    # Year
    year_lbl = Label(current_course_Frame, text = "Year", font=("times new roman", 15, "bold"), bg="white")
    year_lbl.grid(row = 1, column = 0, padx=10, pady=15, sticky=W)

    year_combo = ttk.Combobox(current_course_Frame, font=("times new roman", 15, "bold"), state="readonly")
    year_combo["values"]=("Select the Year","2020","2021","2022","2023","2024")
    year_combo.current(0)
    year_combo.grid(row = 1, column = 1, padx=5, pady=15, sticky=W)


    # semester
    sem_lbl = Label(current_course_Frame, text = "Semester", font=("times new roman", 15, "bold"), bg="white")
    sem_lbl.grid(row = 1, column = 2, padx=10, pady=15, sticky=W)

    sem_combo = ttk.Combobox(current_course_Frame, font=("times new roman", 15, "bold"), state="readonly")
    sem_combo["values"]=("Select the Semester","1st","2nd","3rd","4th")
    sem_combo.current(0)
    sem_combo.grid(row = 1, column = 3, padx=5, pady=15, sticky=W)


    # Class Student Information
    class_Student_Frame = LabelFrame(left_Frame, bd=2, bg = "White", relief="ridge", text="Class Student Information", font=("times new roman", 16, "bold") )
    class_Student_Frame.place(x=10, y=320, width=920, height=400)

    #Student ID Label
    # Student_ID_lbl = Label(class_Student_Frame, text = "Student ID:", font=("times new roman", 15, "bold"), bg="white")
    # Student_ID_lbl.grid(row = 0, column = 0, padx=10, pady=15, sticky=W)

    # student_ID_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    # student_ID_entry.grid(row = 0, column=1, padx=10, pady=15, sticky=W)

    # student name
    Student_name_lbl = Label(class_Student_Frame, text = "Student Name:", font=("times new roman", 15, "bold"), bg="white")
    Student_name_lbl.grid(row = 0, column = 0, padx=10, pady=15, sticky=W)

    student_name_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    student_name_entry.grid(row = 0, column=1, padx=10, pady=15, sticky=W)

    # enrollment no
    Student_Enrollment_no_lbl = Label(class_Student_Frame, text = "Enrollment No:", font=("times new roman", 15, "bold"), bg="white")
    Student_Enrollment_no_lbl.grid(row = 0, column = 2, padx=10, pady=15, sticky=W)

    student_Enrollment_no_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    student_Enrollment_no_entry.grid(row = 0, column=3, padx=10, pady=15, sticky=W)

    # course
    Student_course_lbl = Label(class_Student_Frame, text = "Student course:", font=("times new roman", 15, "bold"), bg="white")
    Student_course_lbl.grid(row = 1, column = 0, padx=10, pady=15, sticky=W)

    student_course_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    student_course_entry.grid(row = 1, column=1, padx=10, pady=15, sticky=W)

    # gender
    Student_gender_lbl = Label(class_Student_Frame, text = "Gender:", font=("times new roman", 15, "bold"), bg="white")
    Student_gender_lbl.grid(row = 1, column = 2, padx=10, pady=15, sticky=W)
    
    Student_gender_entry = ttk.Combobox(class_Student_Frame, font=("times new roman", 15, "bold"), state="readonly")
    Student_gender_entry["values"]=("Select your Gender","Male","Female")
    Student_gender_entry.current(0)
    Student_gender_entry.grid(row = 1, column = 3, padx=5, pady=15, sticky=W)

    # Email
    Student_email_lbl = Label(class_Student_Frame, text = "Student E-Mail:", font=("times new roman", 15, "bold"), bg="white")
    Student_email_lbl.grid(row = 2, column = 0, padx=10, pady=15, sticky=W)

    student_email_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    student_email_entry.grid(row = 2, column=1, padx=10, pady=15, sticky=W)

    # phone number
    Student_Number_lbl = Label(class_Student_Frame, text = "Phone Number:", font=("times new roman", 15, "bold"), bg="white")
    Student_Number_lbl.grid(row = 2, column = 2, padx=10, pady=15, sticky=W)

    student_Number_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    student_Number_entry.grid(row = 2, column=3, padx=10, pady=15, sticky=W)

    # address
    Student_Address_lbl = Label(class_Student_Frame, text = "Address:", font=("times new roman", 15, "bold"), bg="white")
    Student_Address_lbl.grid(row = 3, column = 0, padx=10, pady=15, sticky=W)

    student_Address_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    student_Address_entry.grid(row = 3, column=1, padx=10, pady=15, sticky=W)

    # Teacher name
    Student_Teacher_name_lbl = Label(class_Student_Frame, text = "Teacher Name:", font=("times new roman", 15, "bold"), bg="white")
    Student_Teacher_name_lbl.grid(row = 3, column = 2, padx=10, pady=15, sticky=W)

    student_Teacher_name_entry = ttk.Entry(class_Student_Frame, font=("times new roman", 15, "bold"))
    student_Teacher_name_entry.grid(row = 3, column=3, padx=10, pady=15, sticky=W)

    # Radio Buttons
    radio_btn_1 = ttk.Radiobutton(class_Student_Frame, text="Take Photo Sample", value="Yes")
    radio_btn_1.grid(row=4, column=0)


    radio_btn_2 = ttk.Radiobutton(class_Student_Frame, text="No Photo Sample", value="Yes")
    radio_btn_2.grid(row=4, column=1)

    # button Frame 1
    btn_Frame=Frame(class_Student_Frame,bd=2, relief=RIDGE,bg="white")
    btn_Frame.place(x=7, y=265, width=900,height=40)

    save_btn=Button(btn_Frame, text="Save", font=("times new roman", 15, "bold"), bg="blue", fg="white", width=18)
    save_btn.grid(row=0,column=0)

    
    update_btn=Button(btn_Frame, text="Update", font=("times new roman", 15, "bold"), bg="blue", fg="white", width=18)
    update_btn.grid(row=0,column=1)
    
    reset_btn=Button(btn_Frame, text="Reset", font=("times new roman", 15, "bold"), bg="blue", fg="white", width=18)
    reset_btn.grid(row=0,column=2)
    
    delete_btn=Button(btn_Frame, text="Delete", font=("times new roman", 15, "bold"), bg="blue", fg="white", width=18)
    delete_btn.grid(row=0,column=3)

    # button frame 2
    btn_Frame_2=Frame(class_Student_Frame,bd=2, relief=RIDGE,bg="white")
    btn_Frame_2.place(x=7, y=310, width=900,height=40)

    take_sample_btn=Button(btn_Frame_2, text="Take Sample", font=("times new roman", 15, "bold"), bg="blue", fg="white", width=37)
    take_sample_btn.grid(row=1,column=0)

    update_sample_btn=Button(btn_Frame_2, text="Update Sample", font=("times new roman", 15, "bold"), bg="blue", fg="white", width=37)
    update_sample_btn.grid(row=1,column=3)
    
             
    # Right Frame
    right_Frame = LabelFrame(main_frame, bd=2, bg = "White", relief="ridge", text="Student Details", font=("times new roman", 16, "bold") )
    right_Frame.place(x=960, y=10, width=940, height=760)


def main() -> None:
  root = Tk()
  obj = Student(root)
  root.mainloop()

if __name__ == "__main__" :
  main()