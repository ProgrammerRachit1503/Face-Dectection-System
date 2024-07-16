from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class Student:
  def __init__(self, root) -> None:
    self.root = root
    self.root.geometry("1920x1080+0+0")
    self.root.title("Student Details")

    # ================ Variables ================
    self.var_department = StringVar()
    self.var_course = StringVar()
    self.var_year = StringVar()
    self.var_semester = StringVar()
    self.var_student_name = StringVar()
    self.var_enrollment_no = StringVar()
    self.var_stu_course = StringVar()
    self.var_gender = StringVar()
    self.var_stu_email = StringVar()
    self.var_stu_phone = StringVar()
    self.var_address = StringVar()
    self.var_teacher = StringVar()

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

    dep_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_department, font=("times new roman", 15, "bold"), state="readonly")
    dep_combo["values"]=("Select the Department","IT","Computers","Medical","Civil","Electrical")
    dep_combo.current(0)
    dep_combo.grid(row = 0, column = 1, padx=5, pady=15, sticky=W)

    #Course
    course_lbl = Label(current_course_Frame, text = "Course", font=("times new roman", 15, "bold"), bg="white")
    course_lbl.grid(row = 0, column = 2, padx=10, pady=15, sticky=W)

    course_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_course, font=("times new roman", 15, "bold"), state="readonly")
    course_combo["values"]=("Select the Course","B.Tech CSE","BCA (AI/ML)","B.Tech Civil","B.Pharma","B.Tech EE")
    course_combo.current(0)
    course_combo.grid(row = 0, column = 3, padx=5, pady=15, sticky=W)


    # Year
    year_lbl = Label(current_course_Frame, text = "Year", font=("times new roman", 15, "bold"), bg="white")
    year_lbl.grid(row = 1, column = 0, padx=10, pady=15, sticky=W)

    year_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_year, font=("times new roman", 15, "bold"), state="readonly")
    year_combo["values"]=("Select the Year","2020","2021","2022","2023","2024")
    year_combo.current(0)
    year_combo.grid(row = 1, column = 1, padx=5, pady=15, sticky=W)


    # semester
    sem_lbl = Label(current_course_Frame, text = "Semester", font=("times new roman", 15, "bold"), bg="white")
    sem_lbl.grid(row = 1, column = 2, padx=10, pady=15, sticky=W)

    sem_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_semester, font=("times new roman", 15, "bold"), state="readonly")
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

    student_name_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_student_name, font=("times new roman", 15, "bold"))
    student_name_entry.grid(row = 0, column=1, padx=10, pady=15, sticky=W)

    # enrollment no
    Student_Enrollment_no_lbl = Label(class_Student_Frame, text = "Enrollment No:", font=("times new roman", 15, "bold"), bg="white")
    Student_Enrollment_no_lbl.grid(row = 0, column = 2, padx=10, pady=15, sticky=W)

    student_Enrollment_no_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_enrollment_no, font=("times new roman", 15, "bold"))
    student_Enrollment_no_entry.grid(row = 0, column=3, padx=10, pady=15, sticky=W)

    # Student course
    Student_course_lbl = Label(class_Student_Frame, text = "Student course:", font=("times new roman", 15, "bold"), bg="white")
    Student_course_lbl.grid(row = 1, column = 0, padx=10, pady=15, sticky=W)

    student_course_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_stu_course, font=("times new roman", 15, "bold"))
    student_course_entry.grid(row = 1, column=1, padx=10, pady=15, sticky=W)

    # gender
    Student_gender_lbl = Label(class_Student_Frame, text = "Gender:", font=("times new roman", 15, "bold"), bg="white")
    Student_gender_lbl.grid(row = 1, column = 2, padx=10, pady=15, sticky=W)
    
    Student_gender_entry = ttk.Combobox(class_Student_Frame, textvariable=self.var_gender, font=("times new roman", 15, "bold"), state="readonly")
    Student_gender_entry["values"]=("Select your Gender","Male","Female","Others")
    Student_gender_entry.current(0)
    Student_gender_entry.grid(row = 1, column = 3, padx=10, pady=15, sticky=W)

    # Email
    Student_email_lbl = Label(class_Student_Frame, text = "Student E-Mail:", font=("times new roman", 15, "bold"), bg="white")
    Student_email_lbl.grid(row = 2, column = 0, padx=10, pady=15, sticky=W)

    student_email_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_stu_email, font=("times new roman", 15, "bold"))
    student_email_entry.grid(row = 2, column=1, padx=10, pady=15, sticky=W)

    # phone number
    Student_Number_lbl = Label(class_Student_Frame, text = "Student Phone Number:", font=("times new roman", 15, "bold"), bg="white")
    Student_Number_lbl.grid(row = 2, column = 2, padx=10, pady=15, sticky=W)

    student_Number_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_stu_phone, font=("times new roman", 15, "bold"))
    student_Number_entry.grid(row = 2, column=3, padx=10, pady=15, sticky=W)

    # address
    Student_Address_lbl = Label(class_Student_Frame, text = "Address:", font=("times new roman", 15, "bold"), bg="white")
    Student_Address_lbl.grid(row = 3, column = 0, padx=10, pady=15, sticky=W)

    student_Address_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_address, font=("times new roman", 15, "bold"))
    student_Address_entry.grid(row = 3, column=1, padx=10, pady=15, sticky=W)

    # Teacher name
    Student_Teacher_name_lbl = Label(class_Student_Frame, text = "Teacher Name:", font=("times new roman", 15, "bold"), bg="white")
    Student_Teacher_name_lbl.grid(row = 3, column = 2, padx=10, pady=15, sticky=W)

    student_Teacher_name_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_teacher, font=("times new roman", 15, "bold"))
    student_Teacher_name_entry.grid(row = 3, column=3, padx=10, pady=15, sticky=W)

    # Radio Buttons
    self.var_radio1 = StringVar()
    radio_btn_1 = ttk.Radiobutton(class_Student_Frame, textvariable=self.var_radio1, text="Take Photo Sample", value="Yes")
    radio_btn_1.grid(row=4, column=0)

    self.var_radio2 = StringVar()
    radio_btn_2 = ttk.Radiobutton(class_Student_Frame, textvariable=self.var_radio2, text="No Photo Sample", value="No")
    radio_btn_2.grid(row=4, column=1)

    # button Frame 1
    btn_Frame=Frame(class_Student_Frame,bd=2, relief=RIDGE,bg="white")
    btn_Frame.place(x=7, y=265, width=900,height=40)

    save_btn=Button(btn_Frame, text="Save", command=self.add_data, font=("times new roman", 15, "bold"), bg="blue", fg="white", width=18)
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

    img_right = Image.open(r"images/students.jpg")  #change the image
    img_right = img_right.resize((920, 230), Image.LANCZOS)
    self.photoimg_right = ImageTk.PhotoImage(img_right)

    f_lbl = Label(right_Frame, image = self.photoimg_right)
    f_lbl.place(x=10, y=0, width=920, height=150)

    # ================ Search System ================
    Search_Frame = LabelFrame(right_Frame, bd=2, bg = "White", relief="ridge", text="Search System", font=("times new roman", 15, "bold"))
    Search_Frame.place(x=10, y=160, width=920, height=70)

    search_lbl = Label(Search_Frame, text = "Search By :-", font=("times new roman", 12), bg="pink", fg="blue")
    search_lbl.grid(row = 0, column = 0, padx=10, pady=5, sticky=W)

    search_combo = ttk.Combobox(Search_Frame, font=("times new roman", 12), state="readonly", width=12)
    search_combo["values"]=("Select","Enrollment No","Phone No")
    search_combo.current(0)
    search_combo.grid(row = 0, column = 1, padx=2, pady=5, sticky=W)

    search_entry = ttk.Entry(Search_Frame, font=("times new roman", 12), width=50)
    search_entry.grid(row = 0, column=2, padx=10, pady=5, sticky=W)

    search_btn=Button(Search_Frame, text="Search", font=("times new roman", 10, "bold"), bg="pink", fg="blue", width=12)
    search_btn.grid(row=0,column=3, padx=5)
    
    show_all_btn=Button(Search_Frame, text="Show All", font=("times new roman", 10, "bold"), bg="pink", fg="blue", width=12)
    show_all_btn.grid(row=0,column=4, padx=5)

    # Table Frame
    Table_Frame = Frame(right_Frame, bd=2, bg = "White", relief="ridge")
    Table_Frame.place(x=10, y=240, width=920, height=400)

    scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

    self.student_table = ttk.Treeview(Table_Frame, column=("Department", "Course", "Year", "Semester", "Student Name", "Enrollment No.", "Student Course", "Gender", "Student E-Mail", "Student Phone No.", "Address", "Teacher Name", "Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_x.config(command=self.student_table.xview)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=self.student_table.yview)

    self.student_table.heading("Department", text="Department")
    self.student_table.heading("Course", text="Course")
    self.student_table.heading("Year", text="Year")
    self.student_table.heading("Semester", text="Semester")
    self.student_table.heading("Student Name", text="Student Name")
    self.student_table.heading("Enrollment No.", text="Enrollment No.")
    self.student_table.heading("Student Course", text="Student Course")
    self.student_table.heading("Gender", text="Gender")
    self.student_table.heading("Student E-Mail", text="Student E-Mail")
    self.student_table.heading("Student Phone No.", text="Student Phone No.")
    self.student_table.heading("Address", text="Address")
    self.student_table.heading("Teacher Name", text="Teacher Name")
    self.student_table.heading("Photo", text="PhotoSampleStatus")
    self.student_table["show"] = "headings"

    self.student_table.column("Department", width=100)
    self.student_table.column("Course", width=100)
    self.student_table.column("Year", width=100)
    self.student_table.column("Semester", width=100)
    self.student_table.column("Student Name", width=100)
    self.student_table.column("Enrollment No.", width=100)
    self.student_table.column("Student Course", width=100)
    self.student_table.column("Gender", width=100)
    self.student_table.column("Student E-Mail", width=100)
    self.student_table.column("Student Phone No.", width=100)
    self.student_table.column("Address", width=100)
    self.student_table.column("Teacher Name", width=100)
    self.student_table.column("Photo", width=150)

    self.student_table.pack(fill=BOTH, expand=1)

  # ================ Function Declaration ================
  def add_data(self):
    if self.var_department.get() == "Select the Department" or self.var_student_name.get() == "" or self.var_enrollment_no == "":
      messagebox.showerror("Error",'All fields are required', parent = self.root)
    else:
      try:
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "7575", database ="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                            self.var_department.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_student_name.get(),
                                                                                                            self.var_enrollment_no.get(),
                                                                                                            self.var_stu_course.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_stu_email.get(),
                                                                                                            self.var_stu_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                          )
                          )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student details has been added Successfully", parent = self.root)
      
      except Exception as es:
        messagebox.showerror("Error",f"Due to :{str(es)}", parent = self.root)



def main() -> None:
  root = Tk()
  obj = Student(root)
  root.mainloop()

if __name__ == "__main__" :
  main()