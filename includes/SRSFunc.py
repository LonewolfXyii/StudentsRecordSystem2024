import tkinter as TK
from tkinter import messagebox, ttk, filedialog
import customtkinter as CTR
import json
import shutil
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
import Main as MN
from login import runlogin_window
from PIL import Image



maxlogin = 3
has_run_updates = False
currentTheme = "dark-blue"
WhoLoggedIn = [None]
choices_themes = ("breeze", "carrot", "cherry",
                 "coffee", "marsh", "metal", "midnight", "orange", 
                 "pink", "rose", "sky", "violet")
lighting = "dark"

graphactivities = ["Assignments", "Quizzes", "Exams"]
graphgrades = [35, 69, 24]
colors = ["#87CEEB", "#FFD700", "#FF6347"]


CTR.set_default_color_theme(currentTheme)
CTR.set_appearance_mode("dark")


# FOR LOADING JSON FILES AND SAVING #
def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

# loadables #
students = load_json("students.json")
courses = load_json("courses.json")
grades = load_json("grades.json")
LOGINS = load_json("LOGINS.json")

# TO GUARD ACCESS TO BUTTONS #

class AdminOnlyAccess(CTR.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_readonly = False

    def make_readonly(self):
        self.configure(state="disabled")
        self.is_readonly = True

    def guard_configure(self, *args, **kwargs):
        if self.is_readonly:
            print("Button is read-only")
        else:
            super().configure(*args, **kwargs)

def check_and_disable(WhoLoggedIn, LOGINS, ViewingWarning, items_inplace, buttn_upload_studs, *items):
    if WhoLoggedIn:
        logged_in_user = WhoLoggedIn[0]
        for user in LOGINS:
            if user["username"] == logged_in_user:
                if not user.get("is_Admin", False):
                    disable_items(ViewingWarning, items_inplace, buttn_upload_studs, *items)
                break

def disable_items(ViewingWarning, items_inplace, buttn_upload_studs,*items):
    ViewingWarning.place(relx=0.455, rely=0.91, anchor=TK.CENTER, relwidth=0.50)
    buttn_upload_studs.grid_forget()
    for theseitems in items_inplace:
        theseitems.place_forget()
    
    for button in items:
        button.make_readonly()

# FOR TURNING OFF LIGHT #
def turnOnturnOff():
        global lighting
        if lighting == "dark":
            CTR.set_appearance_mode("light")
            lighting = "light"
    
        else:
            CTR.set_appearance_mode("dark")
            lighting = "dark"
# CHANGING THEMES #
def changetheme(cb_theme):
    global currentTheme
    currentTheme = cb_theme
    CTR.set_default_color_theme(f"includes/themes/{currentTheme}.json")
    print (currentTheme)
# THE TREE VIEW #
def create_tree1(container, headings=None):

    treeframe = TK.Frame(container) 
    treeframe.place(relx=0.5, rely=0.382, anchor=TK.CENTER, relwidth=0.994)
    tree1 = ttk.Treeview(treeframe, show="headings")
    tree1["columns"] = ("Student_ID", "First_Name", "Last_Name", "Gender", "Class", "Credits Earned", "Tuition", "Image_Path")
    tree1.column("Student_ID", anchor=TK.W, width=90)
    tree1.column("First_Name", anchor=TK.W, width=90)
    tree1.column("Last_Name", anchor=TK.W, width=90)
    tree1.column("Gender", anchor=TK.CENTER, width=60)
    tree1.column("Class", anchor=TK.CENTER, width=90)
    tree1.column("Credits Earned", anchor=TK.CENTER, width=90)
    tree1.column("Tuition", anchor=TK.CENTER, width=90)
    tree1.column("Image_Path", anchor=TK.CENTER, width=90)
    tree1.pack(side="left", fill="both", expand=True)
    tree_scroll = TK.Scrollbar(treeframe,command=tree1.yview)
    tree_scroll.pack(side="right", fill="y")

    tree1.configure(yscrollcommand=tree_scroll.set)

    headings = headings or {
        "Student_ID": "Student ID",
        "First_Name": "First Name",
        "Last_Name": "Last Name",
        "Gender": "Gender",
        "Class": "Class",
        "Credits Earned": "Credits Earned",
        "Tuition": "Tuition",
        "Image_Path": "Image Path"
    }

    for key, value in headings.items():
        tree1.heading(key, text=value, anchor=TK.CENTER if key in ["Gender", "Class", "Credits Earned", "Tuition", "Image_Path"] 
    else TK.W, command=lambda _key=key: sort_treeview_column(tree1, _key, False))

    return treeframe, tree1

def create_tree2(container, headings=None):

    treeframe = TK.Frame(container) 
    treeframe.place(relx=0.5, rely=0.382, anchor=TK.CENTER, relwidth=0.994)
    treeV2 = ttk.Treeview(treeframe, show="headings")
    treeV2["columns"] = ("Student ID",
                         "Course ID", 
                         "Course Description", 
                         "Credits Earned", 
                         "Assignment", 
                         "Quiz", 
                         "Exam", 
                         "Final Grade", 
                         "Percent Equivalent", 
                         "Letter Grade")
    
    treeV2.column("Student ID", anchor=TK.W, width=60)
    treeV2.column("Course ID", anchor=TK.W, width=40)
    treeV2.column("Course Description", anchor=TK.W, width=100)
    treeV2.column("Credits Earned", anchor=TK.CENTER, width=37)
    treeV2.column("Assignment", anchor=TK.CENTER, width=40)
    treeV2.column("Quiz", anchor=TK.CENTER, width=28)
    treeV2.column("Exam", anchor=TK.CENTER, width=28)
    treeV2.column("Final Grade", anchor=TK.CENTER, width=40)
    treeV2.column("Percent Equivalent", anchor=TK.CENTER, width=40)
    treeV2.column("Letter Grade", anchor=TK.CENTER, width=40)
    treeV2.pack(side="left", fill="both", expand=True)
    tree_scroll = TK.Scrollbar(treeframe,command=treeV2.yview)
    tree_scroll.pack(side="right", fill="y")

    treeV2.configure(yscrollcommand=tree_scroll.set)

    headings = headings or {
        "Student ID": "Student ID",
        "Course ID": "Course ID",
        "Course Description": "Course Description",
        "Credits Earned": "Credits Earned",
        "Assignment": "Assignment",
        "Quiz": "Quiz",
        "Exam": "Exam",
        "Final Grade": "Final Grade",
        "Percent Equivalent": "Percent Equivalent",
        "Letter Grade": "Letter Grade"
    }

    for key, value in headings.items():
        treeV2.heading(key, text=value, anchor=TK.W, command=lambda _key=key: sort_treeview_column(treeV2, _key, False))

    return treeframe, treeV2

def start_treeview1(tree, students):
    for item in tree.get_children():
        tree.delete(item)

    for student in students:
        tree.insert("", "end", values=(
            student["Student_ID"],
            student["First_Name"],
            student["Last_Name"],
            student["Gender"],
            student["Class"],
            student["Credits Earned"],
            student["Tuition"],
            student["Image_Path"]
        ))

def start_treeview2(tree, students, courses):
    for item in tree.get_children():
        tree.delete(item)

    for student in students:
        for course_id, activity_grades in student["grades"].items():
            course_desc = next(course["course_desc"] for course in courses if course["course_id"] == course_id)
            final_grade_info = activity_grades["final_grade"]
            tree.insert("", "end", values=(
                student["Student_ID"],
                course_id,
                course_desc,
                student["Credits Earned"],
                activity_grades.get("assignment", ""),
                activity_grades.get("quiz", ""),
                activity_grades.get("exam", ""),
                final_grade_info["grade"],
                final_grade_info["percent_equivalent"],
                final_grade_info["letter_equivalent"]
            ))
            

# FOR SORTING OUT TREE VIEW GIVING IT A TAG #

def sort_treeview_column(treeview, col, reverse):
    data_list = [(treeview.set(x, col), x) for x in treeview.get_children("")]
    data_list.sort(reverse=reverse)
    
    for index, (val, x) in enumerate(data_list):
        treeview.move(x, "", index)
    
    for each, item in enumerate(treeview.get_children("")):
        if each % 2 == 0: 
            treeview.item(item, tags=("evenrow",))
        else:
            treeview.item(item, tags=("oddrow",))
    
    treeview.heading(col, command=lambda _col=col: sort_treeview_column(treeview, _col, not reverse))

# APPLYING COLORS #
def apply_row_colors(treeview):
    treeview.tag_configure("oddrow", background="white")
    treeview.tag_configure("evenrow", background="lightblue")

    for each, item in enumerate(treeview.get_children("")):
        if each % 2 == 0:
            treeview.item(item, tags=("evenrow",))
        else:
            treeview.item(item, tags=("oddrow",))
            
# REFRESHING TREEVIEW #
def clear_treeview(treeview):
    try:
        if treeview.get_children():
            for item in treeview.get_children():
                treeview.delete(item)
    except Exception as e:
        print(f"An error occurred while clearing the treeview: {e}")

# LOGIN #
def login(username_entry, password_entry, loginroot):
    global maxlogin
    global WhoLoggedIn
    global LOGINS
    username_input = username_entry.get()
    password_input = password_entry.get()

    print(f"maxlogin: {maxlogin}")
    
    if username_input == "" or password_input == "":
        messagebox.showerror("Error", "Please Type the Username and Password")
        return 

    for user in LOGINS:
        if user["username"] == username_input and user["password"] == password_input:
            messagebox.showinfo("Success", "Login Successful")
            WhoLoggedIn[0] = (username_input)
            loginroot.destroy()
            MN.MainWindow()
            return 
    
    if maxlogin > 0:
        messagebox.showerror("Error", f"Wrong Credentials! Remaining tries: {maxlogin}")
        maxlogin -= 1
        print(f"login remaining: {maxlogin}")
    
    if maxlogin == 0:
        messagebox.showerror("Error", "Reached Maximum of LOGINS, Exiting Program")
        loginroot.destroy()

## STUDENT IMAGE  ##

def display_student_image(student_id, studpic, students):
    try:
        student = next(s for s in students if s["Student_ID"] == student_id)
        image_path = student["Image_Path"]

        if image_path is None:
            print("Error: The image path is None.")
            return
        
        image = Image.open(image_path)
        photo = CTR.CTkImage(light_image=image, size=(160, 160))

        studpic.configure(image=photo)
        studpic.image = photo

    except AttributeError:
        print(f"Student Image Missing")

    except Exception as e: 
        print(f"An unexpected error occurred: {e}")

## SEARCHES ##
def search_gender(treeview, selected_gender):
    searched_students = []

    for student in students:
        if selected_gender == "Select Gender" or student["Gender"] == selected_gender:
            searched_students.append(student)
    updatetreelist(treeview, searched_students)

def search_class(treeview, selected_gender):
    searched_students = []

    for student in students:
        if selected_gender == "All" or student["Class"] == selected_gender:
            searched_students.append(student)
    updatetreelist(treeview, searched_students)

def search_first_name(treeview, event, search_fn, students):
    writteninboxis = search_fn.get().strip().lower()
    searched_students = []

    for student in students:
        if writteninboxis in student["First_Name"].lower():
            searched_students.append(student)
    updatetreelist(treeview, searched_students)

## UPLOADING IMAGE  ##     

def upload_image(treeview, students):
    image_file_types = [("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
    file_path = filedialog.askopenfilename(filetypes=image_file_types)
    
    if file_path:
        selected_items = treeview.selection()
        
        if not selected_items:
            print("No student selected")
            return
        
        selected_item = selected_items[0]
        student_id = int(treeview.item(selected_item)["values"][0])
        with open("students.json", "r") as file:
            students = json.load(file)

        file_extension = file_path.split(".")[-1]
        
        new_file_path = f"Images/{student_id}.{file_extension}"
        
        shutil.copyfile(file_path, new_file_path)         

        for student in students:
           if student["Student_ID"] == student_id:
              student["Image_Path"] = new_file_path
         
        with open("students.json", "w") as file:
            json.dump(students, file, indent=2)
            
            updatetreelist(treeview, students)

## EVENT TIED FUNCTIONS  ##

def on_tree_select(event, treeview, studpic, students):
    try:
        selected_item = treeview.selection()[0]
        student_id = int(treeview.item(selected_item)["values"][0])
        display_student_image(student_id, studpic, students)
    except IndexError:
        print("NOTHING SELECTED")

def register(username, password, is_Admin, su_pwd, frame):
    SUPER_ADMIN_PASSWORD = "123!!!321"
    LOGINS = load_json("LOGINS.json")
    if is_Admin and su_pwd != SUPER_ADMIN_PASSWORD:
        messagebox.showerror("Error", "Invalid super admin password. You do not have permission to register as ADMIN.")
        return
    
# LIMITING TO 12 CHARS ONLY #
    if len(username) > 12 or len(password) > 12:
        messagebox.showerror("Error", "Username and password must be up to 12 characters long.")
        return
    if " " in username or " " in password:
        messagebox.showerror("Error", "Username and password should not contain spaces.")
        return
    
# MAKING SURE ITS NOT EMPTYY #
    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return
    
# NO DOUBLE USERS #
    if any(user["username"] == username for user in LOGINS):
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        return
    
# THIS IS TO ADD A NEW USER ID AND AUTO SORTING IT #
    if LOGINS:
        max_user_id = max(user["user_id"] for user in LOGINS)
        new_user_id = max_user_id + 1
    else:
        new_user_id = 1

# FORMAT FOR NEW USER #
    new_user = {
        "user_id": new_user_id,
        "username": username,
        "password": password,
        "is_Admin": is_Admin
    }
    LOGINS.append(new_user)
    save_json("LOGINS.json", LOGINS)
    messagebox.showinfo("Success", "Registration successful!")
    
    frame.destroy()
    
# REG TOP LEVEL WINDOW #
def registration_page(loginroot):
    def registering():
        username = entry_username.get()
        password = entry_password.get()
        role = V.get()
        is_Admin = role == "Teacher"
        su_pwd = entry_su_pwd.get() if is_Admin else ""
        register(username, password, is_Admin, su_pwd, frame)
    
    def whatRole(*args):
        role = V.get()
        if role == "Teacher":
            label_su_pwd.pack(pady=4, before=buttn_register)
            entry_su_pwd.pack(pady=4, before=buttn_register)
        else:
            label_su_pwd.pack_forget()
            entry_su_pwd.pack_forget()

# main registration frame #   
    frame = CTR.CTkToplevel(loginroot)
    frame.geometry("250x320+720+330")
    frame.title("Registration")
      

    CTR.CTkLabel(frame, text="Username").pack(pady=4)
    entry_username = CTR.CTkEntry(frame)
    entry_username.pack()

    CTR.CTkLabel(frame, text="Password").pack(pady=4)
    entry_password = CTR.CTkEntry(frame, show="*")
    entry_password.pack()

    CTR.CTkLabel(frame, text="Role").pack(pady=4)
    V = CTR.StringVar(value="Student")
    cb_role = CTR.CTkComboBox(frame, variable=V, values=["Teacher", "Student"])
    cb_role.pack()
    V.trace("w", whatRole)

    label_su_pwd = CTR.CTkLabel(frame, text="Control Password")
    entry_su_pwd = CTR.CTkEntry(frame, show="*")
    
    buttn_register = CTR.CTkButton(frame, text="Register", command=registering)
    buttn_register.pack(pady=4)

# ADDING STUDENT #

def add_studData(treeview, students):
    add_window = CTR.CTkToplevel()
    add_window.title("Add Data")
    add_window.geometry("300x300")
    add_window.resizable(False, False) 
    
    label_frame = CTR.CTkFrame(add_window)
    label_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    entry_frame = CTR.CTkFrame(add_window)
    entry_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    lbl_student_id = CTR.CTkLabel(label_frame, text="Student ID")
    lbl_student_id.pack(anchor="w")
    entry_student_id = CTR.CTkEntry(entry_frame)
    entry_student_id.pack(anchor="e")
    entry_student_id.configure(validate="key", validatecommand=(add_window.register(lambda text: text.isdigit()), "%S"))

    lbl_first_name = CTR.CTkLabel(label_frame, text="First Name")
    lbl_first_name.pack(anchor="w")
    entry_first_name = CTR.CTkEntry(entry_frame)
    entry_first_name.pack(anchor="e")

    lbl_last_name = CTR.CTkLabel(label_frame, text="Last Name")
    lbl_last_name.pack(anchor="w")
    entry_last_name = CTR.CTkEntry(entry_frame)
    entry_last_name.pack(anchor="e")

    lbl_gender = CTR.CTkLabel(label_frame, text="Gender")
    lbl_gender.pack(anchor="w")
    gender_options = ["Male", "Female", "LGBTQIA+"]
    combo_gender = CTR.CTkComboBox(entry_frame, values=gender_options)
    combo_gender.pack(anchor="e")

    lbl_class = CTR.CTkLabel(label_frame, text="Class")
    lbl_class.pack(anchor="w")
    class_options = ["BSIS", "BFA", "BMA"]
    combo_class = CTR.CTkComboBox(entry_frame, values=class_options)
    combo_class.pack(anchor="e")

    lbl_tuition = CTR.CTkLabel(label_frame, text="Tuition")
    lbl_tuition.pack(anchor="w")
    tuition_options = ["Paid", "Missing"]
    combo_tuition = CTR.CTkComboBox(entry_frame, values=tuition_options)
    combo_tuition.pack(anchor="e")

    def save_data():
        data = {
            "Student_ID": int(entry_student_id.get()),
            "First_Name": entry_first_name.get(),
            "Last_Name": entry_last_name.get(),
            "Gender": combo_gender.get(),
            "Class": combo_class.get(),
            "Credits Earned": 0,
            "Tuition": combo_tuition.get(),
            "Image_Path": None, 
            "enrolled_courses": []  
        }
        try:
            with open("students.json", "r") as file:
                students = json.load(file)
            for index, student in enumerate(students): 
                 if student["Student_ID"] == data["Student_ID"]:
                     students[index] = data
                     break 
            else:       
                 students.append(data)       

            with open("students.json", "w") as file:
                json.dump(students, file, indent=2)
            
            print("Data Saved!!!")
            updatetreelist(treeview, students)
            add_window.destroy()

        except Exception as e:
            print(f"An error occurred: {e}")

    save_button = CTR.CTkButton(entry_frame, text="Save", command=save_data)
    save_button.pack(anchor="e", pady=10)

# REMOVING STUDENT  #
def remove_selected(treeview, students):
    try:
        selected_item = treeview.selection()[0]
        student_id = treeview.item(selected_item, "values")[0]
        
        if messagebox.askyesno("Confirmation", "Lets remove this selected STUDENT CONFIRM?"):
            with open("students.json", "r") as file:
                students = json.load(file)

            to_rem_students = []
            for student in students:
                if student["Student_ID"] != int(student_id):
                    to_rem_students.append(student)
            students = to_rem_students


            with open("students.json", "w") as file:
                json.dump(students, file, indent=2)

            treeview.delete(selected_item)
            updatetreelist(treeview, students)

    except IndexError:
        messagebox.showinfo("Info", "No student selected dummy")

## CALL TO UPDATE TREE VIEW ##
def updatetreelist(treeview, students):

    for item in treeview.get_children():
        treeview.delete(item)
    
    for student in students:
        treeview.insert("", "end", values=(student["Student_ID"],
                                        student["First_Name"],
                                        student["Last_Name"],
                                        student["Gender"],
                                        student["Class"],
                                        student["Credits Earned"],
                                        student["Tuition"],
                                        student["Image_Path"]))
    apply_row_colors(treeview)

## UPDATING THE STUDENT LIST WITH FILE ##

def upload_studlist(treeview, students):
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        if file_path.endswith("students.json"):
            destination_path = "./students.json"
            shutil.copy(file_path, destination_path)
            print("File successfully copied to the program's folder.")

            with open(destination_path, "r") as file:
                students = json.load(file)
                updatetreelist(treeview, students)
                apply_row_colors(treeview)
        else:
            messagebox.showerror("Error", "The selected file is not students.json. Please upload the correct file.")

## GRADES CALCULATIONS ##

def assign_grades_to_students(students, grades):
    for student in students:
        student["grades"] = {}
        for grade_record in grades:
            if grade_record["student_id"] == student["Student_ID"]:
                course_id = grade_record["course_id"]
                student["grades"][course_id] = grade_record["grades"]

def get_grade_info(grade):
    if 95 <= grade <= 100:
        letter = "A"
        percent = 100
    elif 91 <= grade < 95:
        letter = "A-"
        percent = 94
    elif 87 <= grade < 91:
        letter = "B+"
        percent = 90
    elif 83 <= grade < 87:
        letter = "B"
        percent = 86
    elif 79 <= grade < 83:
        letter = "B-"
        percent = 82
    elif 75 <= grade < 79:
        letter = "C"
        percent = 78
    elif 70 <= grade < 75:
        letter = "D"
        percent = 74
    else:
        letter = "F"
        percent = 69
    return {"letter_equivalent": letter, "percent_equivalent": percent}

def calculate_final_grade(activity_grades):
    total = sum(activity_grades.values())
    final_grade = total / len(activity_grades)
    final_grade = round(final_grade * 2) / 2 
    final_grade = round(final_grade, 1)
    return final_grade
    
def update_final_grades(students):
    global has_run_updates 
    if not has_run_updates:
        for student in students:
            total_credits = 0
            for course_id, activities in student["grades"].items():
                final_grade = calculate_final_grade(activities)
                grade_info = get_grade_info(final_grade)
                activities["final_grade"] = {
                    "grade": final_grade,
                    "letter_equivalent": grade_info["letter_equivalent"],
                    "percent_equivalent": grade_info["percent_equivalent"]
                }
                # Check if the final grade is passing
                if final_grade >= 70:
                    course_credits = next(course["credits"] for course in courses if course["course_id"] == course_id)
                    total_credits += course_credits
            student["Credits Earned"] = total_credits
    has_run_updates = True

## GRAPHING THE GRADES ##
        
def forGraph(graphframe):
    global graphgrades

    figure = create_bar_graph(graphgrades)
    canvas = tkagg.FigureCanvasTkAgg(figure, master=graphframe)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget() 
    canvas_widget.grid()
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=TK.CENTER, relwidth=0.99)
    canvas_widget.configure(bg="#2f2f2f")

def create_bar_graph(graphgrades):
    global graphactivities
    fig, ax = plt.subplots(figsize=(2, 1.5))
    fig.patch.set_facecolor("grey")
    ax.barh(graphactivities, graphgrades, color=colors)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Grades", fontsize=4, color="red")  
    ax.set_title("Grades in Assignments, Quizzes, and Exams", fontsize=6, color="red")
    ax.tick_params(axis="both", which="major", labelsize=4, colors="red")
    ax.grid(axis="x", linestyle="--", alpha=0.7)
    ax.set_facecolor("grey")
    return fig

## FOR FUN ##

def show_mercy(graphframe, text, root, picframe, happy_smile, imgsmile):
    update_graph(graphframe, text, root)
    show_smile(picframe, happy_smile, imgsmile)

def update_graph(graphframe, text, root):

    for widget in graphframe.winfo_children():
        widget.destroy()
    
    def draw_new_graph():
        global graphgrades, canvas

        graphgrades = [71, 71, 71]

        figure = create_bar_graph(graphgrades)

        canvas = tkagg.FigureCanvasTkAgg(figure, master=graphframe)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=TK.CENTER, relwidth=1)

        text.configure(text="STUDENT PASSED!! (^_^)", fg_color="green")
    root.after(1000, draw_new_graph)
    
def show_smile(picframe, happy_smile, imgsmile):
    happy_smile.place(relx=0.5, rely=0.5, anchor=TK.CENTER, relwidth=1)

    fade_smile(picframe, happy_smile,imgsmile, 340)

def fade_smile(picframe, happy_smile, imgsmile, alpha):
    if alpha > 0:
        faded_image = imgsmile.copy()
        faded_image.putalpha(alpha)
        
        processedimgsmile = CTR.CTkImage(light_image=faded_image, size=(140, 140))
        happy_smile.configure(image=processedimgsmile)
        happy_smile.imgsmile = processedimgsmile 

        picframe.after(40, fade_smile, picframe, happy_smile, imgsmile, alpha - 10)
    else:
        happy_smile.place_forget()
        
# JUST FOR LOGOUT #
def restarte(root, newlogin_window):
    root.destroy()
    newlogin_window()
