# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:46:13 2021

@author: PRANIL
"""

from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
from tkinter.font import Font

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login") 
        self.root.geometry("1650x850+-8+0")
        #=====bg image===
        image11=Image.open(r"loginbg.png")
        image11=image11.resize((1650,900),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(image11)
        lbl_bg=Label(image=self.photoimage4,borderwidth=5)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        #=====Left image======
        img9=Image.open(r"registerside.png") 
        img9=img9.resize((400,500), Image.ANTIALIAS)
        self.photoimage16=ImageTk.PhotoImage(img9) 
        lblimg9=Label(root,image=self.photoimage16) 
        lblimg9.place(x=405,y=200, width=400,height=450)
        
        #========login frame====
        login_frame=Frame(self.root,bg="white",relief=SUNKEN)
        login_frame.place(x=805,y=200,width=340,height=450)
        #====login icon====
        img1=Image.open(r"loginicon.png") 
        img1=img1.resize((80,80), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1) 
        lblimg1=Label(image=self.photoimage1,bg="white", borderwidth=8) 
        lblimg1.place(x=920,y=205, width=100,height=100)
  
        title=Label(login_frame,text="Login Window",font=("glacial indifference",20),fg="#1F2024",bg="white").place(x=80,y=100)
        #===labek email n password====
        email=Label(login_frame,text="Email Address",font=("glacial indifference",15),fg="#1F2024",bg="white").place(x=65,y=150)
        self.txt_email=Entry(login_frame,font=("glacial indifference",15),bg="lightgray")
        self.txt_email.place(x=30,y=180,width=280)
        
        password=Label(login_frame,text="Password",font=("glacial indifference",15),fg="#1F2024",bg="white").place(x=65,y=220)
        self.txt_password=Entry(login_frame,font=("glacial indifference",15),bg="lightgray")
        self.txt_password.place(x=30,y=250,width=280)
        
        # ======Icon email&password Images=================
        img2=Image.open(r"loginicon.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk. PhotoImage (img2)
        lblimg1=Label(image=self.photoimage2, bg="black", borderwidth=8)
        lblimg1.place(x=840,y=353,width=25, height=25)
        
        img3=Image.open(r"passicon.png")
        img3=img3.resize((25,25), Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3, bg="black", borderwidth=8)
        lblimg1.place(x=840,y=422, width=25, height=25)
        
        #=====login button=====
        btn_login=Button(login_frame,text="Log In",font=("glacial indifference",20),fg="white",bg="#172243",cursor="hand2",activeforeground="white",activebackground="#1F2024",command=self.login).place(x=90,y=300,width=135,height=40)
        #=====register button=====
        btn_forgot=Button(login_frame,text="Forgot Password",font=("glacial indifference",15),borderwidth=0,fg="#172243",bg="white",cursor="hand2",activeforeground="white",activebackground="black",command=self.forget_password_window).place(x=30,y=370,width=160)
        
        self.btn_img17=ImageTk.PhotoImage(file=r"registerbtn.png")
        btn_register=Button(self.root,image=self.btn_img17,bg="skyblue2",cursor="hand2",command=self.register_window).place(x=525,y=500, width=160,height=50)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)
        
    def forget_password(self):
       if self.cmb_quest.get()=="select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
           messagebox.showerror("Error","A;; fields are required",parent=self.root2)
       else:
           try:
               con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial2")
               cur=con.cursor()
               cur.execute("select * from user_info where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Please Select The Correct Security Question/Enter Answer",parent=self.root2)
               else:
                   cur.execute("update user_info set password=%s where email=%s",(self.txt_new_password.get(),self.txt_email.get()))
                   con.commit()
                   con.close()
                   messagebox.showinfo("Success","your Password has been reset, Please login with new Password",parent=self.root2)
                   self.reset()
                   self.root2.destroy()
           except Exception as es:
               messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
            
            
           
           

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the  email address to reset your password",parent=self.root)
        else:
             try:
                con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial2")
                cur=con.cursor()
                cur.execute("select * from user_info where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+170")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("glacial indifference",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                     #====================forget password
                    question=Label(self.root2,text="Security Question",font=("times new roman",15, "bold"),fg="black", bg="white").place(x=50,y=100)

                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("glacial indifference",15, "bold"),fg="black", bg="white").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("glacial indifference",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    new_password=Label(self.root2,text="New Password",font=("glacial indifference",15, "bold"),fg="black", bg="white").place(x=50,y=260)
                    self.txt_new_password=Entry(self.root2,font=("glacial indifference",15),bg="lightgray")
                    self.txt_new_password.place(x=50,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("glacial indifference",15,"bold")).place(x=90,y=340)
     
                    
                
             except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
            
    def login_window(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
            
        else:
            self.root.destroy()
            import latest
            
        
        
    def register_window(self):
        self.root.destroy()
        import register
        
        
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial2")
                cur=con.cursor()
                cur.execute("select*from user_info where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid EMAIL and PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import latest_mainmenu
                con.close()
                
            
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
        

root=Tk()
obj=Login_Window(root)
root.mainloop()