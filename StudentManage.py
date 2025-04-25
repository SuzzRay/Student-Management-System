from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x720+0+0")
        self.root.title("Student Management System")

        self.var_std_id = StringVar()
        self.var_rollno = StringVar()
        self.var_regno = StringVar()
        self.var_dob = StringVar()
        self.var_std_name = StringVar()
        self.var_semester = StringVar()
        self.var_session = StringVar()
        self.var_teacher = StringVar()
        self.var_phone = StringVar()
        self.var_dep = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_course = StringVar()

        # Frame
        bg_lbl = Label(self.root, bd=4, relief=RIDGE)
        bg_lbl.place(x=0, y=0, width=1350, height=720)

        lbl_title = Label(
            bg_lbl,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 40, "bold"),
            fg="blue",
            bg="white",
        )
        lbl_title.place(x=0, y=0, width=1500, height=50)

        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=0, y=50, width=1350, height=690)

        # Left Frame ------------------------------------->
        DataLeftFrame = LabelFrame(
            Manage_frame,
            bd=4,
            relief=RIDGE,
            padx=2,
            text="Student Information",
            font=("times new roman", 12, "bold"),
            fg="red",
            bg="white",
        )
        DataLeftFrame.place(x=0, y=0, width=800, height=700)

        img_5 = Image.open(
            r"C:\\Users\\Pc\\Desktop\\CMS\\college_images\\11th.jpg"
        )
        img_5 = img_5.resize((650, 120), Image.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)
        my_img = Label(DataLeftFrame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=650, height=150)

        # Information Form Frmae  --------------------------------->
        # Current Course info
        std_lbl_info_frame = LabelFrame(
            DataLeftFrame,
            bd=4,
            relief=RIDGE,
            padx=2,
            text="Current Course Information",
            font=("times new roman", 12, "bold"),
            fg="red",
            bg="white",
        )
        std_lbl_info_frame.place(x=0, y=150, width=650, height=140)

        # Department
        lbl_dep = Label(
            std_lbl_info_frame,
            text="Department",
            font=("arial", 12, "bold"),
            bg="white",
        )
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(
            std_lbl_info_frame,
            textvariable=self.var_dep,
            font=("arial", 12, "bold"),
            width=17,
            state="readonly",
        )
        combo_dep["value"] = (
            "Select Department",
            "Computer Science",
            "Mathematics",
            "Physics",
            "Chemistry",
            "Zoology",
            "Botany",
            "BCA",
        )
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_std = Label(
            std_lbl_info_frame, font=("arial", 12, "bold"), text="Course :", bg="White"
        )
        course_std.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        com_txtcourse_std = ttk.Entry(
            std_lbl_info_frame,
            textvariable=self.var_course,
            font=("arial", 11, "bold"),
            width=17,
        )
        com_txtcourse_std.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Session
        current_session = Label(
            std_lbl_info_frame, font=("arial", 12, "bold"), text="Session :", bg="white"
        )
        current_session.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        com_txt_current_session = ttk.Entry(
            std_lbl_info_frame,
            textvariable=self.var_session,
            font=("arial", 11, "bold"),
            width=17,
        )
        com_txt_current_session.grid(row=1, column=1, padx=2, sticky=W)

        # Semester
        label_semester = Label(
            std_lbl_info_frame,
            font=("arial", 12, "bold"),
            text="Semester :",
            bg="white",
        )
        label_semester.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        comsemester = ttk.Combobox(
            std_lbl_info_frame,
            textvariable=self.var_semester,
            state="readonly",
            font=("arial", 12, "bold"),
            width=17,
        )
        comsemester["value"] = (
            "Select Semester",
            "Sem - 1",
            "Sem - 2",
            "Sem - 3",
            "Sem - 4",
            "Sem - 5",
            "Sem - 6",
            "Sem - 7",
            "Sem - 8",
        )
        comsemester.current(0)
        comsemester.grid(row=1, column=3, padx=2, sticky=W)

        # Class Course info
        std_lbl_class_frame = LabelFrame(
            DataLeftFrame,
            bd=4,
            relief=RIDGE,
            padx=2,
            text="Current Course Information",
            font=("times new roman", 12, "bold"),
            fg="red",
            bg="white",
        )
        std_lbl_class_frame.place(x=0, y=300, width=650, height=250)

        # Id
        lbl_id = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Student ID :",
            bg="white",
        )
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        id_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_std_id,
            font=("arial", 11, "bold"),
            width=22,
        )
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Name
        lbl_name = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Student Name :",
            bg="white",
        )
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        name_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_std_name,
            font=("arial", 11, "bold"),
            width=22,
        )
        name_entry.grid(row=0, column=3, padx=2, pady=7)

        # Registration Number
        lbl_reg = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Registration No. :",
            bg="white",
        )
        lbl_reg.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        reg_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_regno,
            font=("arial", 11, "bold"),
            width=22,
        )
        reg_entry.grid(row=1, column=1, padx=2, pady=7)

        # Roll Number
        lbl_roll = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Roll No. :",
            bg="white",
        )
        lbl_roll.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        roll_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_rollno,
            font=("arial", 11, "bold"),
            width=22,
        )
        roll_entry.grid(row=1, column=3, padx=2, pady=7)

        # Gender
        label_gender = Label(
            std_lbl_class_frame, font=("arial", 12, "bold"), text="Gender :", bg="white"
        )
        label_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        gender = ttk.Combobox(
            std_lbl_class_frame,
            textvariable=self.var_gender,
            state="readonly",
            font=("arial", 12, "bold"),
            width=18,
        )
        gender["value"] = ("Select Gender", "Male", "Female", "Others")
        gender.current(0)
        gender.grid(row=2, column=1, padx=2, sticky=W)

        # Date of Birth
        lbl_dob = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Enter DOB :",
            bg="white",
        )
        lbl_dob.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        dob_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_dob,
            font=("arial", 11, "bold"),
            width=22,
        )
        dob_entry.grid(row=2, column=3, padx=2, pady=7)

        # Email
        lbl_email = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Enter Email :",
            bg="white",
        )
        lbl_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        email_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_email,
            font=("arial", 11, "bold"),
            width=22,
        )
        email_entry.grid(row=3, column=1, padx=2, pady=7)

        # Phone Number
        lbl_ph = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Phone No. :",
            bg="white",
        )
        lbl_ph.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        ph_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_phone,
            font=("arial", 11, "bold"),
            width=22,
        )
        ph_entry.grid(row=3, column=3, padx=2, pady=7)

        # Address
        lbl_add = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Address :",
            bg="white",
        )
        lbl_add.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        add_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_address,
            font=("arial", 11, "bold"),
            width=22,
        )
        add_entry.grid(row=4, column=1, padx=2, pady=7)

        # Teacher
        lbl_teacher = Label(
            std_lbl_class_frame,
            font=("arial", 11, "bold"),
            text="Teacher :",
            bg="white",
        )
        lbl_teacher.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        teacher_entry = ttk.Entry(
            std_lbl_class_frame,
            textvariable=self.var_teacher,
            font=("arial", 11, "bold"),
            width=22,
        )
        teacher_entry.grid(row=4, column=3, padx=2, pady=7)

        # Button
        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=550, width=650, height=38)

        btn_add = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            font=("arial", 11, "bold"),
            width=17,
            bg="blue",
            fg="white",
        )
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            font=("arial", 11, "bold"),
            width=17,
            bg="blue",
            fg="white",
        )
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            font=("arial", 11, "bold"),
            width=17,
            bg="blue",
            fg="white",
        )
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            font=("arial", 11, "bold"),
            width=17,
            bg="blue",
            fg="white",
        )
        btn_reset.grid(row=0, column=3, padx=1)

        # Right Frame
        DataRightFrame = LabelFrame(
            Manage_frame,
            bd=4,
            relief=RIDGE,
            padx=2,
            text="Student Information",
            font=("times new roman", 12, "bold"),
            fg="red",
            bg="white",
        )
        DataRightFrame.place(x=680, y=1, width=700, height=700)

        img_6 = Image.open(
            r"C:\\Users\\Pc\\Desktop\\CMS\\college_images\\s.jpg"
        )
        img_6 = img_6.resize((780, 200), Image.LANCZOS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        my_img = Label(DataRightFrame, image=self.photoimg_6, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=790, height=200)

        Search_Frame = LabelFrame(
            DataRightFrame,
            bd=4,
            relief=RIDGE,
            padx=2,
            text="Search Student Information",
            font=("times new roman", 12, "bold"),
            fg="red",
            bg="white",
        )
        Search_Frame.place(x=0, y=210, width=790, height=70)

        search_by = Label(
            Search_Frame,
            font=("arial", 11, "bold"),
            text="Search By :",
            fg="red",
            bg="black",
        )
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        self.var_com_search = StringVar()
        con_txt_search = ttk.Combobox(
            Search_Frame,
            textvariable=self.var_com_search,
            state="readonly",
            font=("arial", 12, "bold"),
            width=18,
        )
        con_txt_search["value"] = (
            "Select Option",
            "Roll_No",
            "Student_id",
            "Phone",
            "Reg_no",
        )
        con_txt_search.current(0)
        con_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(
            Search_Frame,
            textvariable=self.var_search,
            width=22,
            font=("arial", 11, "bold"),
        )
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(
            Search_Frame,
            text="Search",
            command=self.search_data,
            font=("arial", 11, "bold"),
            width=7,
            bg="blue",
            fg="white",
        )
        btn_search.grid(row=0, column=3, padx=5)

        btn_showall = Button(
            Search_Frame,
            text="Show All",
            command=self.fetch_data,
            font=("arial", 11, "bold"),
            width=7,
            bg="blue",
            fg="white",
        )
        btn_showall.grid(row=0, column=4, padx=5)

        # Scroll Bar
        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=260, width=650, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "id",
                "rollno",
                "regno",
                "dob",
                "name",
                "sem",
                "session",
                "teacher",
                "phno",
                "dep",
                "gender",
                "email",
                "add",
                "course",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("regno", text="Registration No")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("session", text="Session")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("phno", text="Phone No")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email Id")
        self.student_table.heading("add", text="Address")
        self.student_table.heading("course", text="Course")

        self.student_table["show"] = "headings"

        self.student_table.column("id", width=100)
        self.student_table.column("rollno", width=100)
        self.student_table.column("regno", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("session", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("phno", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("add", width=100)
        self.student_table.column("course", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (
            self.var_dep.get() == ""
            or self.var_email.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="qwerty@09876",
                    database="demo",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_std_id.get(),
                        self.var_rollno.get(),
                        self.var_regno.get(),
                        self.var_dob.get(),
                        self.var_std_name.get(),
                        self.var_semester.get(),
                        self.var_session.get(),
                        self.var_teacher.get(),
                        self.var_phone.get(),
                        self.var_dep.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_course.get(),
                    ),
                )

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student has been Added!", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="qwerty@09876", database="demo"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_std_id.set(data[0])
        self.var_rollno.set(data[1])
        self.var_regno.set(data[2])
        self.var_dob.set(data[3])
        self.var_std_name.set(data[4])
        self.var_semester.set(data[5])
        self.var_session.set(data[6])
        self.var_teacher.set(data[7])
        self.var_phone.set(data[8])
        self.var_dep.set(data[9])
        self.var_gender.set(data[10])
        self.var_email.set(data[11])
        self.var_address.set(data[12])
        self.var_course.set(data[13])

    def update_data(self):
        if (
            self.var_dep.get() == ""
            or self.var_email.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Are you sure this student data", parent=self.root
                )
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="qwerty@09876",
                        database="demo",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set roll_no=%s,reg_no=%s,dob=%s,name=%s,semester=%s,session=%s,teacher=%s,phone=%s,department=%s,gender=%s,email=%s,address=%s,course=%s where student_id=%s",
                        (
                            self.var_rollno.get(),
                            self.var_regno.get(),
                            self.var_dob.get(),
                            self.var_std_name.get(),
                            self.var_semester.get(),
                            self.var_session.get(),
                            self.var_teacher.get(),
                            self.var_phone.get(),
                            self.var_dep.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_address.get(),
                            self.var_course.get(),
                            self.var_std_id.get(),
                        ),
                    )
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student successfully updated", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete", "Are youy sure delete this student", parent=self.root
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="qwerty@09876",
                        database="demo",
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    value = (self.var_std_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete ", "Your Student data has been deleted", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_std_id.set("Enter Student Id ")
        self.var_rollno.set("Enter RollNo")
        self.var_regno.set("EnterRegNo")
        self.var_dob.set("Enter DoB")
        self.var_std_name.set("Enter Name")
        self.var_semester.set("Select Semester")
        self.var_session.set("Enter Session ")
        self.var_teacher.set("Enter Teacher Name")
        self.var_phone.set("Enter PhNo")
        self.var_dep.set("Select Department")
        self.var_gender.set("Select Gender")
        self.var_email.set("Enter Valid EmailId")
        self.var_address.set("Enter Address")
        self.var_course.set("Enter Course")

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select option")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="qwerty@09876",
                    database="demo",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select * from student where "
                    + str(self.var_com_search.get())
                    + " LIKE '%"
                    + str(self.var_search.get())
                    + "%'"
                )
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
