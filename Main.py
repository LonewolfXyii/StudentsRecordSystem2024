import tkinter as TK
import customtkinter as CTR
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk, Image
from includes import SRSFunc
import login

##callable dimentions##
HEIGHT = 700
WIDTH = 1250

def MainWindow():
    
    root = CTR.CTk()
    root.geometry((F"{WIDTH}x{HEIGHT}"))
    root.title("Students Record System by Nesjohn, xyii@live.com.ph")
    root.resizable(True,False)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", backround="#D3D3D3", foreground="black", rowheight=28, fieldbackround="#D3D3D3")
    style.map("Treeview", background=[("selected", "blue")])

  

    presentdate = datetime.now()
    currentdate = presentdate.date()
    currenttime = presentdate.strftime("%I:%M:%S %p")
    displaytime = (f"Logged in at: {currentdate}")


    choices_genders = ["Select Gender", "Male", "Female", "LGBTQIA+"]
    choices_class = ["All", "BSIS", "BFA", "BMA"]
    selected_gender_search = CTR.StringVar(value="Select Gender")
    selected_class_search = CTR.StringVar(value="All")
    search_fn = CTR.StringVar()


    #images#
    imgschoollogo = CTR.CTkImage(light_image=Image.open("schoollogo.png"),size=(140,140))
    imguploadicon = CTR.CTkImage(light_image=Image.open("upload_icon.png"))
    imgsmile_path = "images/smile.png"
    imgsmile = Image.open(imgsmile_path).convert("RGBA")
    processedimgsmile = CTR.CTkImage(light_image=imgsmile)
    #fonts#
    my_font_HighLight44 = CTR.CTkFont(family="Small Fonts", size=44, weight="bold", slant="roman")
    my_font_HighLight28 = CTR.CTkFont(family="Tahoma", size=28, weight="bold")
    my_font_16B = CTR.CTkFont(family="Verdana", size=16, weight="bold")
    my_font_16= CTR.CTkFont(family="Tahoma", size=16)
    my_font_8I = CTR.CTkFont(family="Verdana", size=8, slant="roman")
    my_font_Btn= CTR.CTkFont(family="Small Fonts", size=24)
    my_font_Btn1= CTR.CTkFont(family="Small Fonts", size=20)
    my_font_Btn2= CTR.CTkFont(family="Small Fonts", size=18, weight="bold")
    my_font_11B = CTR.CTkFont(family="Tahoma", size=11, weight="bold")

    #frames#
    mainframe1 = CTR.CTkFrame(master=root, width=220, corner_radius=0)
    mainframe1.grid(row=0, column=0, sticky="nsw")
    mainframe2 = CTR.CTkFrame(master=root, height=32, width=500, corner_radius=0)
    mainframe2.grid(row=0, column=1, sticky="swe",)
    mainframe3 = CTR.CTkFrame(master=root, corner_radius=0)
    mainframe3.grid(row=0, column=2, sticky="nswe")
    picframe1 = CTR.CTkFrame(master=mainframe3, height=160, width=160, fg_color="yellow")
    picframe1.place(relx=0.22, rely=0.18, anchor=TK.NW)
    maintreeview_frame1 = TK.Frame(master=root, height=412, width=747, background="#D3D3D3")
    maintreeview_frame1.place(relx=0.160, rely=0.65, anchor=TK.W, relwidth=0.60)
    maintreeview_frame2 = TK.Frame(master=root, height=412, width=747, background="black")
    maintreeview_frame2.place(relx=0.160, rely=0.65, anchor=TK.W, relwidth=0.60)
    student_widg_frame = CTR.CTkFrame(master=root, height=412, width=747)
    student_widg_frame.place(relx=0.455, rely=0.332, anchor=TK.CENTER, relwidth=0.59, relheight=0.04)
    graphframe = CTR.CTkFrame(master=mainframe3, height=150)
    graphframe.place(relx=0.5, rely=0.612, anchor=TK.CENTER, relwidth=0.99)

    #tree view#
    tree_frame1, tree1 = SRSFunc.create_tree1(maintreeview_frame1)
    tree_frame2, tree2 = SRSFunc.create_tree2(maintreeview_frame2)

    #labels#
    #---images---#
    studpic = CTR.CTkLabel(master=picframe1, height=160, width=160, text="")
    studpic.grid(row=0,column=2, sticky="n", padx=2, pady=2)
    schoollogo = CTR.CTkLabel(master=mainframe1, image=imgschoollogo, height=120, width=120, text="")
    schoollogo.grid(row=0,column=0, sticky="n", pady=10)
    happy_smile = CTR.CTkLabel(picframe1, image=processedimgsmile, text="Im Happy!!")
    #---images---#
    #---text only---#
    textlabel = CTR.CTkLabel(master=mainframe1, text=".:.:Menu:.:.", font=my_font_HighLight28)
    textlabel.grid(row=0,column=0, sticky="n", pady=160)
    welcometextlabel = CTR.CTkLabel(master=root, text=f"Hello, {SRSFunc.WhoLoggedIn[0]}!", font=my_font_HighLight28)
    welcometextlabel.grid(row=0,column=1, sticky="nw",pady=60, padx=16)
    textlabel = CTR.CTkLabel(master=root, text="Welcome to Enchanced Students Grading System.", font=my_font_16)
    textlabel.grid(row=0,column=1, sticky="nw", pady=96, padx=16)
    pageInformation = CTR.CTkLabel(master=root, text="Students Information Page", font=my_font_HighLight28)
    pageInformation.grid(row=0,column=1, sticky="nw", pady=162, padx=16)
    textlabel = CTR.CTkLabel(master=mainframe3, text=" STUDENT STATUS ", font=my_font_HighLight28)
    textlabel.grid(row=0,column=2, sticky="new", pady=80, padx=8)
    failpassed = CTR.CTkLabel(master=mainframe3, text=("FAILING !!"), font=my_font_Btn2, text_color="#ff7070", bg_color="#2a0000")
    failpassed.place(relx=0.5, rely=0.78, anchor=TK.CENTER, relwidth=0.9)
    textlabel = CTR.CTkLabel(master=mainframe3, text=("PROGRESS: "), font=my_font_11B)
    textlabel.place(relx=0.5, rely=0.74, anchor=TK.CENTER, relwidth=0.28)
    dateandtime = CTR.CTkLabel(master=root, text=(str(currenttime)), font=my_font_HighLight28)
    dateandtime.grid(row=0,column=1, sticky="ne", pady=4, padx=8)
    dateandtime = CTR.CTkLabel(master=root, text=displaytime, font=my_font_Btn2)
    dateandtime.grid(row=0,column=1, sticky="ne", pady=36, padx=8)
    ViewingWarning = CTR.CTkLabel(master=root, text="FOR STUDENT VIEWING ONLY", font=my_font_HighLight28, text_color="red", corner_radius=4)
    #---text only---#

    #other widgets#
    buttn_logout = CTR.CTkButton(master=mainframe1, width=100, height=30, text="LOGOUT", font=my_font_Btn2, border_width=5 , command=lambda: SRSFunc.restarte(root, login.runlogin_window))
    buttn_logout.grid(row=0,column=0, sticky="sw", pady= 84, padx=32)

    buttn_uploadpic= CTR.CTkButton(master=mainframe3, width=140, height=40, text="UPLOAD", font=my_font_Btn1, border_width=5, command=lambda: SRSFunc.upload_image(tree1, SRSFunc.students))
    buttn_uploadpic.grid(row=0,column=2, sticky="n", pady=300)
    buttn_MERCY = SRSFunc.AdminOnlyAccess(master=mainframe3, height=80, text="MERCY", font=my_font_Btn2, fg_color="red", border_width=21, corner_radius=28,border_color="yellow", command=lambda: SRSFunc.show_mercy(graphframe, failpassed, root, picframe1, happy_smile, imgsmile))
    buttn_MERCY.place (relx=0.74, rely=0.88, anchor=TK.E, relwidth=0.48)
    #just giving variable#
    items_inplace= [buttn_MERCY, buttn_uploadpic]

    buttn_upload_studs = CTR.CTkButton(student_widg_frame, image=imguploadicon, text="Upload a Student List", compound="left", font=my_font_11B, corner_radius=12, command=lambda: SRSFunc.upload_studlist(tree1, SRSFunc.students))
    buttn_upload_studs.grid(row=0,column=1, sticky="e", pady= 0, padx=95)
 
    cb_gender = CTR.CTkComboBox(master=student_widg_frame, variable=selected_gender_search, values=choices_genders, font=my_font_11B, corner_radius=12, command=lambda value: SRSFunc.search_gender(tree1, value))
    cb_gender.grid(row=0,column=1, sticky="nw", pady= 0, padx=0)
    cb_class = CTR.CTkComboBox(master=student_widg_frame, variable=selected_class_search, values=choices_class, font=my_font_11B, corner_radius=12, command=lambda value: SRSFunc.search_class(tree1, value))
    cb_class.grid(row=0,column=1, sticky="nw", pady= 0, padx=160)
    cb_theme = CTR.CTkOptionMenu(master=mainframe3, values=SRSFunc.choices_themes, width=140, height=20, font=my_font_11B, command=SRSFunc.changetheme)
    cb_theme.grid(row=0,column=2, sticky="nw", pady= 12, padx=12)
    cb_theme.set("PICK A THEME")
    studentsearch_box = CTR.CTkEntry(master=student_widg_frame, textvariable=search_fn, font=my_font_11B, width=180,placeholder_text="By Student Name",corner_radius=12)
    studentsearch_box.grid(row=0,column=1, sticky="nw", pady= 0, padx=324)
    buttn_add_stud = SRSFunc.AdminOnlyAccess(master=maintreeview_frame1, width=40, height=30, text="ADD DATA", font=my_font_Btn2, state="normal", command=lambda: SRSFunc.add_studData(tree1, SRSFunc.students))
    buttn_add_stud.place(relx=0.19, rely=0.85, anchor=TK.CENTER, relwidth=0.28)
    buttn_lightsoff = CTR.CTkButton(master=mainframe3, width=100, height=20, text="LIGHTS ON/OFF", font=my_font_11B, border_width=0, command=SRSFunc.turnOnturnOff)
    buttn_lightsoff.grid(row=0,column=2, sticky="ne", pady= 12, padx=12)
    buttn_remove_stud = SRSFunc.AdminOnlyAccess(master=maintreeview_frame1, width=40, height=30, text="REMOVE SELECTED", font=my_font_Btn2, state="normal",  command=lambda: SRSFunc.remove_selected(tree1, SRSFunc.students))
    buttn_remove_stud.place(relx=0.79, rely=0.85, anchor=TK.CENTER, relwidth=0.28)
    buttn_update_stud = SRSFunc.AdminOnlyAccess(master=maintreeview_frame1, width=40, height=30, text="UPDATE DATA", font=my_font_Btn2, state="disabled")
    buttn_update_stud.place(relx=0.49, rely=0.85, anchor=TK.CENTER, relwidth=0.28)
    buttn_update_grad = SRSFunc.AdminOnlyAccess(master=maintreeview_frame2, width=40, height=30, text="UPDATE DATA", font=my_font_Btn2, state="normal", command=lambda: SRSFunc.COURSES_UPDATE())
    buttn_update_grad.place(relx=0.49, rely=0.85, anchor=TK.CENTER, relwidth=0.28)

# MENU #
    buttn_mystudents= CTR.CTkButton(master=mainframe1, width=160, height=48, text="STUDENTS", font=my_font_Btn, border_width=5, command=lambda: toggle_tree1())
    buttn_mystudents.grid(row=0,column=0, sticky="n", pady=212, padx=12)
    buttn_grades = CTR.CTkButton(master=mainframe1, width=160, height=48, text="GRADES", font=my_font_Btn, border_width=5, command=lambda: toggle_tree2())
    buttn_grades.grid(row=0,column=0, sticky="n", pady=282, padx=12)
    buttn_activities = CTR.CTkButton(master=mainframe1, width=160, height=48, text="ACTIVITIES", font=my_font_Btn, border_width=5)
    buttn_activities.grid(row=0,column=0, sticky="n", pady=352, padx=12)   

## initialize ##
    SRSFunc.check_and_disable(SRSFunc.WhoLoggedIn, SRSFunc.LOGINS, ViewingWarning, items_inplace, buttn_upload_studs, buttn_remove_stud, buttn_update_stud, buttn_add_stud)    
    SRSFunc.assign_grades_to_students(SRSFunc.students, SRSFunc.grades)
    SRSFunc.update_final_grades(SRSFunc.students)
    tree_frame2.place_forget()
    ViewingWarning.place_forget
    maintreeview_frame2.place_forget()
    buttn_mystudents.configure(state="disabled") 
    tree1.bind("<<TreeviewSelect>>", lambda event: SRSFunc.on_tree_select(event, tree1, studpic, SRSFunc.students))
    SRSFunc.start_treeview1(tree1, SRSFunc.students)
    SRSFunc.apply_row_colors(tree1)
    studentsearch_box.bind("<KeyRelease>", lambda event: SRSFunc.search_first_name(tree1, event, search_fn, SRSFunc.students))
    buttn_mystudents.configure(state="disabled")
    SRSFunc.forGraph(graphframe)

# MENU BUTTONS TOGGLES #
    def toggle_tree1():
# what will hide and show---------------------------------------------------------
        student_widg_frame.place(relx=0.455, rely=0.33, anchor=TK.CENTER, relwidth=0.61, relheight=0.04)
        maintreeview_frame1.place(relx=0.160, rely=0.65, anchor=TK.W, relwidth=0.60)
        maintreeview_frame2.place_forget()
        SRSFunc.clear_treeview(tree1)
        SRSFunc.clear_treeview(tree2)
        pageInformation.configure(text="Students Information Page")

        if tree1:
             tree_frame1.place(relx=0.5, rely=0.382, anchor=TK.CENTER, relwidth=0.994)
#-------------------------------------------------------------------------------#            
        try:
            buttn_mystudents.configure(state="disabled")
            buttn_grades.configure(state="normal")
            tree1.bind("<<TreeviewSelect>>", lambda event: SRSFunc.on_tree_select(event, tree1, studpic, SRSFunc.students))
            SRSFunc.start_treeview1(tree1, SRSFunc.students)
            SRSFunc.apply_row_colors(tree1)
            buttn_mystudents.configure(state="disabled") 

        except Exception as e:
            print(f"Error: {e}")

    def toggle_tree2():
# what will hide and show---------------------------------------------------------
        maintreeview_frame2.place(relx=0.160, rely=0.65, anchor=TK.W, relwidth=0.60)
        student_widg_frame.place_forget()
        maintreeview_frame1.place_forget()
        SRSFunc.clear_treeview(tree2)
        SRSFunc.clear_treeview(tree1)    
        pageInformation.configure(text="Grades and Averages")

        if tree2:
            tree_frame2.place(relx=0.5, rely=0.382, anchor=TK.CENTER, relwidth=0.994)
#-------------------------------------------------------------------------------#
        try:
            buttn_grades.configure(state="disabled")
            buttn_mystudents.configure(state="normal")
            tree2.bind("<<TreeviewSelect>>", lambda event: SRSFunc.on_tree_select(event, tree2, studpic, SRSFunc.students))
            SRSFunc.start_treeview2(tree2, SRSFunc.students, SRSFunc.courses)
            SRSFunc.apply_row_colors(tree2)


        except Exception as e:
            print(f"Error: {e}")
            

    root.mainloop()
if __name__ == "__main__":
    MainWindow()
