from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import re


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
        self.var_stu_division = StringVar()
        self.var_gender = StringVar()
        self.var_stu_email = StringVar()
        self.var_stu_phone = StringVar()
        self.var_address = StringVar()

        self.mysql_host = "localhost"
        self.mysql_username = "root"
        self.mysql_pass = "7575"
        self.mysql_DB = "face_recognizer"
        self.mysql_port = 3306

        # Load and place images
        self.load_and_place_image("Images/face.jpeg", 0, 0, 640, 200)
        self.load_and_place_image("Images/attendance.jpeg", 640, 0, 640, 200)
        self.load_and_place_image("Images/face.jpeg", 1280, 0, 640, 200)
        self.load_and_place_image(
            "Images/GD Goenka University.jpg", 0, 200, 1920, 880, bg=True
        )

        title_lbl = Label(
            self.root,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="blue",
            fg="red",
        )
        title_lbl.place(x=0, y=200, width=1920, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="pink")
        main_frame.place(x=10, y=260, width=1900, height=780)

        # Left Frame
        left_Frame = LabelFrame(
            main_frame,
            bd=2,
            bg="White",
            relief="ridge",
            text="Student Details",
            font=("times new roman", 16, "bold"),
        )
        left_Frame.place(x=10, y=10, width=940, height=760)

        self.load_and_place_image(
            "Images/face.jpeg", 10, 0, 920, 150, parent=left_Frame
        )

        # Current course
        current_course_Frame = LabelFrame(
            left_Frame,
            bd=2,
            bg="White",
            relief="ridge",
            text="Current Course Information",
            font=("times new roman", 16, "bold"),
        )
        current_course_Frame.place(x=10, y=160, width=920, height=150)

        self.create_label_combobox(
            current_course_Frame,
            "Department",
            self.var_department,
            0,
            0,
            [
                "Select the Department",
                "IT",
                "Computers",
                "Medical",
                "Civil",
                "Electrical",
            ],
        )
        self.create_label_combobox(
            current_course_Frame,
            "Course",
            self.var_course,
            0,
            2,
            [
                "Select the Course",
                "B.Tech CSE",
                "BCA (AI/ML)",
                "B.Tech Civil",
                "B.Pharma",
                "B.Tech EE",
            ],
        )
        self.create_label_combobox(
            current_course_Frame,
            "Year",
            self.var_year,
            1,
            0,
            ["Select the Year", "2020", "2021", "2022", "2023", "2024"],
        )
        self.create_label_combobox(
            current_course_Frame,
            "Semester",
            self.var_semester,
            1,
            2,
            ["Select the Semester", "1st", "2nd", "3rd", "4th"],
        )

        # Class Student Information
        class_Student_Frame = LabelFrame(
            left_Frame,
            bd=2,
            bg="White",
            relief="ridge",
            text="Class Student Information",
            font=("times new roman", 16, "bold"),
        )
        class_Student_Frame.place(x=10, y=320, width=920, height=400)

        self.create_label_entry(
            class_Student_Frame, "Student Name:", self.var_student_name, 0, 0
        )

        vcmd_enroll = (self.root.register(self.validate_input), "%d", "%P", 12)

        self.create_label_entry(
            class_Student_Frame,
            "Enrollment No:",
            self.var_enrollment_no,
            0,
            2,
            "key",
            vcmd_enroll,
        )

        self.create_label_combobox(
            class_Student_Frame,
            "Student Division:",
            self.var_stu_division,
            1,
            0,
            ["Select the Division", "A", "B", "C"],
        )

        self.create_label_combobox(
            class_Student_Frame,
            "Gender:",
            self.var_gender,
            1,
            2,
            ["Male", "Female", "Others"],
        )

        self.create_label_entry(
            class_Student_Frame, "Student E-Mail:", self.var_stu_email, 2, 0
        )

        self.create_label_entry(class_Student_Frame, "Address:", self.var_address, 3, 0)

        vcmd_phone = (self.root.register(self.validate_input), "%d", "%P", 10)

        self.create_label_entry(
            class_Student_Frame,
            "Student Phone Number:",
            self.var_stu_phone,
            2,
            2,
            "key",
            vcmd_phone,
        )

        # Radio Buttons
        self.var_radio = StringVar()
        radio_btn_1 = ttk.Radiobutton(
            class_Student_Frame,
            variable=self.var_radio,
            text="Take Photo Sample",
            value="Yes",
        )

        radio_btn_1.grid(row=4, column=0)

        radio_btn_2 = ttk.Radiobutton(
            class_Student_Frame,
            variable=self.var_radio,
            text="No Photo Sample",
            value="No",
        )
        radio_btn_2.grid(row=4, column=1)

        # Button Frame 1
        btn_Frame = Frame(class_Student_Frame, bd=2, relief=RIDGE, bg="white")
        btn_Frame.place(x=7, y=265, width=900, height=40)

        self.create_button(btn_Frame, "Save", self.add_data, 0, 0)
        self.create_button(btn_Frame, "Update", self.update_data, 0, 1)
        self.create_button(btn_Frame, "Reset", self.reset_data, 0, 2)
        self.create_button(btn_Frame, "Delete", self.delete_data, 0, 3)

        # Button Frame 2
        btn_Frame_2 = Frame(class_Student_Frame, bd=2, relief=RIDGE, bg="white")
        btn_Frame_2.place(x=7, y=310, width=900, height=40)

        take_sample_btn = Button(
            btn_Frame_2,
            command=self.generate_dataset,
            text="Take Sample",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            width=74,
        )
        take_sample_btn.grid(row=1, column=0)

        # Right Frame
        right_Frame = LabelFrame(
            main_frame,
            bd=2,
            bg="White",
            relief="ridge",
            text="Student Details",
            font=("times new roman", 16, "bold"),
        )
        right_Frame.place(x=960, y=10, width=940, height=760)

        self.load_and_place_image(
            "images/students.jpg", 10, 0, 920, 225, parent=right_Frame
        )

        # Table Frame
        Table_Frame = Frame(right_Frame, bd=2, bg="White", relief="ridge")
        Table_Frame.place(x=10, y=240, width=920, height=400)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            Table_Frame,
            column=(
                "Department",
                "Course",
                "Year",
                "Semester",
                "Student Name",
                "Enrollment No.",
                "Student Division",
                "Gender",
                "Student E-Mail",
                "Student Phone No.",
                "Address",
                "Photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student Name", text="Student Name")
        self.student_table.heading("Enrollment No.", text="Enrollment No.")
        self.student_table.heading("Student Division", text="Student Division")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Student E-Mail", text="Student E-Mail")
        self.student_table.heading("Student Phone No.", text="Student Phone No.")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Student Name", width=100)
        self.student_table.column("Enrollment No.", width=100)
        self.student_table.column("Student Division", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Student E-Mail", width=100)
        self.student_table.column("Student Phone No.", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ====================== UI maker Methods =========================
    def load_and_place_image(self, path, x, y, width, height, bg=False, parent=None):
        img = Image.open(path)
        img = img.resize((width, height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label = Label(parent if parent else self.root, image=photo)
        label.image = photo
        label.place(x=x, y=y, width=width, height=height)
        if bg:
            self.bg_img = label

    def create_label_combobox(self, parent, text, variable, row, col, values):
        label = Label(
            parent, text=text, font=("times new roman", 15, "bold"), bg="white"
        )
        label.grid(row=row, column=col, padx=10, pady=15, sticky=W)
        combo = ttk.Combobox(
            parent,
            textvariable=variable,
            font=("times new roman", 15, "bold"),
            state="readonly",
        )
        combo["values"] = values
        combo.current(0)
        combo.grid(row=row, column=col + 1, padx=5, pady=15, sticky=W)

    def create_label_entry(
        self, parent, text, variable, row, col, validate=None, validatecommand=None
    ):
        label = Label(
            parent, text=text, font=("times new roman", 15, "bold"), bg="white"
        )
        label.grid(row=row, column=col, padx=10, pady=15, sticky=W)
        entry = ttk.Entry(
            parent, textvariable=variable, font=("times new roman", 15, "bold")
        )

        if validate and validatecommand:
            entry.config(validate=validate, validatecommand=validatecommand)

        entry.grid(row=row, column=col + 1, padx=10, pady=15, sticky=W)

    def create_button(self, parent, text, command, row, col):
        button = Button(
            parent,
            text=text,
            command=command,
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            width=18,
        )
        button.grid(row=row, column=col)

    def connect_db(self):
        return mysql.connector.connect(
            host=self.mysql_host,
            username=self.mysql_username,
            password=self.mysql_pass,
            database=self.mysql_DB,
            port=self.mysql_port,
        )

    # ================ Function Declaration ================

    # ================  Adding Data ================
    def add_data(self):
        if (
            self.var_department.get() == "Select the Department"
            or self.var_course.get() == "Select the Course"
            or self.var_year.get() == "Select the Year"
            or self.var_semester.get() == "Select the Semester"
            or self.var_student_name.get() == ""
            or self.var_enrollment_no.get() == ""
            or self.var_stu_division.get() == "Select the Division"
            or self.var_stu_email.get() == ""
            or self.var_stu_phone.get() == ""
            or self.var_address.get() == ""
            or self.var_radio.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        elif len(self.var_stu_phone.get()) != 10:
            messagebox.showerror("Error", "Invalidate Phone Number", parent=self.root)

        elif len(self.var_enrollment_no.get()) != 12:
            messagebox.showerror(
                "Error", "Invalidate Enrollment Number", parent=self.root
            )

        elif not (
            re.match(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                self.var_stu_email.get(),
            )
        ):
            messagebox.showerror("Error", "Invalidate Email Address", parent=self.root)

        else:
            try:
                conn = self.connect_db()
                my_cursor = conn.cursor()
                my_tuple = (
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_student_name.get(),
                    self.var_enrollment_no.get(),
                    self.var_stu_division.get(),
                    self.var_gender.get(),
                    self.var_stu_email.get(),
                    self.var_stu_phone.get(),
                    self.var_address.get(),
                    self.var_radio.get(),
                )
                my_cursor.execute(
                    "insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    my_tuple,
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details has been added Successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ================  Fetch Data ================
    def fetch_data(self):
        conn = self.connect_db()
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
            self.student_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    # ================ Get Cursor ================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_department.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_name.set(data[4])
        self.var_enrollment_no.set(data[5])
        self.var_stu_division.set(data[6])
        self.var_gender.set(data[7])
        self.var_stu_email.set(data[8])
        self.var_stu_phone.set(data[9])
        self.var_address.set(data[10])
        self.var_radio.set(data[11])

    # ================ Update data ================
    def update_data(self):
        if (
            self.var_department.get() == "Select the Department"
            or self.var_course.get() == "Select the Course"
            or self.var_year.get() == "Select the Year"
            or self.var_semester.get() == "Select the Semester"
            or self.var_student_name.get() == ""
            or self.var_enrollment_no.get() == ""
            or self.var_stu_division.get() == "Select the Division"
            or self.var_stu_email.get() == ""
            or self.var_stu_phone.get() == ""
            or self.var_address.get() == ""
            or self.var_radio.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        elif len(self.var_stu_phone.get()) != 10:
            messagebox.showerror("Error", "Invalidate Phone Number", parent=self.root)

        elif len(self.var_enrollment_no.get()) != 12:
            messagebox.showerror(
                "Error", "Invalidate Enrollment Number", parent=self.root
            )

        elif not (
            re.match(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                self.var_stu_email.get(),
            )
        ):
            messagebox.showerror("Error", "Invalidate Email Address", parent=self.root)

        else:
            try:
                update = messagebox.askyesno(
                    "Update",
                    "Are you sure you want to update student details?",
                    parent=self.root,
                )
                if update > 0:
                    conn = self.connect_db()
                    my_tuple = (
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_student_name.get(),
                        self.var_stu_division.get(),
                        self.var_gender.get(),
                        self.var_stu_email.get(),
                        self.var_stu_phone.get(),
                        self.var_address.get(),
                        self.var_radio.get(),
                        self.var_enrollment_no.get(),
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Department=%s, Course=%s, Year=%s, Semester=%s, StudentName=%s, StudentDivision=%s, Gender=%s, StudentEMail=%s, StudentPhone=%s, Address=%s, PhotoSample=%s where EnrollmentNumber=%s",
                        my_tuple,
                    )
                elif not update:
                    return
                messagebox.showinfo(
                    "Update", "Student Details Updated successfully", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ================= Delete Data =================
    def delete_data(self):
        if self.var_enrollment_no.get() == "":
            messagebox.showerror(
                "Error", "Enrollment number is required", parent=self.root
            )
            return

        try:
            delete = messagebox.askyesno(
                "Delete Student Data",
                "Are you sure you want to delete student details?",
                parent=self.root,
            )

            if delete:
                with self.connect_db() as conn:
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "DELETE FROM student WHERE EnrollmentNumber=%s",
                        (self.var_enrollment_no.get()),
                    )
                    conn.commit()

                messagebox.showinfo(
                    "Delete", "Student Details Deleted Successfully", parent=self.root
                )
                self.fetch_data()
                self.reset_data()

        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # ================= Reset Data =================
    def reset_data(self):
        self.var_department.set("Select the Department")
        self.var_course.set("Select the Course")
        self.var_year.set("Select the Year")
        self.var_semester.set("Select the Semester")
        self.var_student_name.set("")
        self.var_enrollment_no.set("")
        self.var_stu_division.set("Select the Division")
        self.var_gender.set("Male")
        self.var_stu_email.set("")
        self.var_stu_phone.set("")
        self.var_address.set("")
        self.var_radio.set("")

    # ============ Generate data set or take a photo sample =============
    def generate_dataset(self):
        if self.var_student_name.get() == "" or self.var_enrollment_no.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            with self.connect_db() as conn:
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                self.fetch_data()

            # ============ Load Predifined data on face frontal from openCV ==========
            cam = cv2.VideoCapture(0)

            instructions = (
                'Press "Esc" Key to close camera, Press "Spacebar" Key to capture image'
            )

            while True:
                ret, my_frame = cam.read()

                if not ret:
                    messagebox.showerror(
                        "Error", "Failed to detect Camera.", parent=self.root
                    )
                    return
                cv2.imshow(instructions, my_frame)

                if cv2.waitKey(1) & 0xFF == 27:  # Press Esc to exit window
                    break

                if cv2.waitKey(1) & 0xFF == 32:  # Press Spacebar to capture image
                    Face_value = cv2.resize(my_frame, (0, 0), fx=0.5, fy=0.5)

                    if Face_value is not None:
                        self.__extracted_from_generate_dataset_23__(Face_value)
                    else:
                        messagebox.showerror(
                            "Error", "No face detected", parent=self.root
                        )

            cam.release()
            cv2.destroyAllWindows()

        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    def __extracted_from_generate_dataset_23__(self, Face_value):
        face = Face_value
        file_name_path = f"data/student_{self.var_enrollment_no.get()}_{self.var_student_name.get()}_.jpg"

        cv2.imwrite(file_name_path, face)

    # ============ Validation Functions ================
    # ============ Validation Phone Number =============

    def validate_input(self, action, value_if_allowed, max_length):
        if action == "1":
            if value_if_allowed.isdigit():
                if len(value_if_allowed) <= int(max_length):
                    return True
                else:
                    return False
            else:
                return False

        elif action == "0":
            return True

        else:
            return False


def main() -> None:
    root = Tk()
    obj = Student(root)
    root.mainloop()


if __name__ == "__main__":
    main()
