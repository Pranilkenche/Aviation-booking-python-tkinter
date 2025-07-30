# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:06:27 2021

@author: PRANIL
"""
from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image #pip install pillow
from tkinter import messagebox
import pymysql
import imageio
from tkinter.font import Font


class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1650x850+-8+0")
        #BG IMage=====
        image11=Image.open(r"registerbg.png")
        image11=image11.resize((2050,1150),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(image11)
        lbl_bg=Label(image=self.photoimage4,borderwidth=5)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        

        #=====Left image======
        img1=Image.open(r"registerside.png") 
        img1=img1.resize((400,500), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1) 
        lblimg1=Label(root,image=self.photoimage1) 
        lblimg1.place(x=275,y=150, width=400,height=500)


        
         #=====regester frame==========
        Frame1=Frame(self.root,bg="white",)
        Frame1.place(x=675, y=150, height=500,width=700)
        title1=Image.open(r"registerwindow.png")
        title1=title1.resize((500,150), Image.ANTIALIAS)
        self.photoimage18=ImageTk.PhotoImage(title1)
        titleimg=Label(Frame1,image=self.photoimage18).place(x=40,y=-20, width=500,height=150)
        
        
        #===================row1
        
        fname=Label(Frame1,text="First Name",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=50,y=100)
        self.txt_fname=Entry(Frame1,font=("glacial indifference",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        lname=Label(Frame1,text="Last Name",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=370,y=100)
        self.txt_lname=Entry(Frame1,font=("glacial indifference",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        
        #====================row2
        contact=Label(Frame1,text="Contact No.",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=50,y=170)
        self.txt_contact=Entry(Frame1,font=("glacial indifference",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(Frame1,text="Email",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=370,y=170)
        self.txt_email=Entry(Frame1,font=("glacial indifference",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        #====================row3
        question=Label(Frame1,text="Security Question",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=50,y=240)

        self.cmb_quest=ttk.Combobox(Frame1,font=("glacial indifference",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(Frame1,text="Answer",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=370,y=240)
        self.txt_answer=Entry(Frame1,font=("glacial indifference",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
         #====================row4
        
        password=Label(Frame1,text="Password",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=50,y=310)
        self.txt_password=Entry(Frame1,font=("glacial indifference",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(Frame1,text="Confirm Password",font=("glacial indifference",15),fg="#1F2024", bg="white").place(x=370,y=310)
        self.txt_cpassword=Entry(Frame1,font=("glacial indifference",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
 
        #=============terms
        self.var_chk=IntVar()
        chk=Checkbutton(Frame1,text="I Agree The Terms And Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("time new roman",10)).place(x=50,y=380)
    
        self.btn_img=ImageTk.PhotoImage(file="register1.png")
        btn_register=Button(Frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420,width=200,height=55)
        
        self.btn_img1=ImageTk.PhotoImage(file="signin.png")
        btn_login=Button(self.root,image=self.btn_img1,bg="skyblue2",cursor="hand2",command=self.login_window).place(x=395,y=480, width=160,height=50)
        
    def login_window(self):
        self.root.destroy()
        import tkinterlogin
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)        
        self.txt_contact.delete(0,END)        
        self.txt_email.delete(0,END)        
        self.txt_answer.delete(0,END)        
        self.txt_password.delete(0,END)        
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)                

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree with Our Terms and Conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial2")
                cur=con.cursor()
                cur.execute("select * from user_info where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already Exists. Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into user_info (fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                     self.txt_lname.get(),
                                     self.txt_contact.get(),
                                     self.txt_email.get(),
                                     self.cmb_quest.get(),
                                     self.txt_answer.get(),
                                     self.txt_password.get()
                                     ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root)


                                

                
            
root=Tk()

obj=Login(root)
root.mainloop()


    



