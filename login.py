import tkinter as TK
from tkinter import Canvas, W, E, N, CENTER
import customtkinter as CTR
from PIL import ImageTk, Image
from includes import SRSFunc


def runlogin_window():
   loginroot = CTR.CTk()
   loginroot.geometry("625x700")
   loginroot.title('Students Record System(Login) by Nesjohn, xyii@live.com.ph')
   loginroot.resizable(False,False)
   
   #font styles#
   my_font_HighLight = CTR.CTkFont(family="Small Fonts", size=44, weight="bold", slant="roman")
   my_font_16B = CTR.CTkFont(family="Verdana", size=16, weight="bold")
   my_font_8I = CTR.CTkFont(family="Verdana", size=8, slant="roman")
   
   #images#
   bgimg2 = ImageTk.PhotoImage(Image.open("loginbg.jpg"))
   img1 = CTR.CTkImage(dark_image=Image.open('schoollogo.png'),size=(200,200))
   
   
   mycanvas = Canvas(loginroot, width=625, height=700,background="black",border=-2)
   mycanvas.pack(fill="both", expand=True)
   mycanvas.create_image(0,0, image=bgimg2, anchor="nw")
   
   # FRAMES #
   loginrootframe1 = CTR.CTkFrame(master=mycanvas)
   loginrootframe1.pack(pady=20)
   loginrootframe2 = CTR.CTkFrame(master=mycanvas)
   loginrootframe2.pack(pady=60)
   loginrootframe3 = CTR.CTkFrame(master=mycanvas)
   loginrootframe3.pack(pady=20)
   
   LoginLogo = CTR.CTkLabel(master=loginrootframe1, image=img1, text="Your School Logo Here",anchor="nw", text_color="red", font=my_font_16B)
   LoginLogo.place(x=0,y=0)
   
   mycanvas.create_text(315,260, text="Login System", font=(my_font_HighLight), activefill="green", fill="white")
   
   username_entry = CTR.CTkEntry(loginrootframe2, height=32, width=160, placeholder_text='Username')
   username_entry.pack()
   password_entry = CTR.CTkEntry(loginrootframe2, height=32, width=160, placeholder_text='Password', show="*")
   password_entry.pack(pady=4)
   
   mycanvas.create_text(313,560, text="Dont have an account yet?", font=(my_font_8I), activefill="red", fill="white")
   
   regist_var = loginroot   
   buttn_login = CTR.CTkButton(loginrootframe3, text="LOGIN", command=lambda: SRSFunc.login(username_entry, password_entry, loginroot))
   buttn_login.pack()
   buttn_login = CTR.CTkButton(mycanvas, text="Click to Register", height=10, width=50, command=lambda: SRSFunc.registration_page(regist_var))
   buttn_login.place(x=260,y=572)
   
   cb_theme = CTR.CTkOptionMenu(master=loginroot, values=SRSFunc.choices_themes, width=120, height=24, font=my_font_8I,command=SRSFunc.changetheme)
   cb_theme.place(x=560,y=4, anchor=N)
   cb_theme.set("PICK A THEME")
      
   
   loginroot.mainloop()
if __name__ == "__main__":
    runlogin_window()