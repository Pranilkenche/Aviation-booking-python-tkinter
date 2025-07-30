# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:38:47 2021

@author: PRANIL
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:02:28 2021

@author: 20man
"""

from tkinter import*
from tkinter import ttk,messagebox 
from PIL import Image,ImageTk
import pymysql
import datetime
import time
from tkcalendar import Calendar,DateEntry  #pip install tlcalendar
import random as rd
import string


class main_menu_window:
    def __init__(self,root):
        self.root=root
        self.root.title("main menu")
        self.root.geometry("1920x900+-8+0")
        self.bg=ImageTk.PhotoImage(file=r"india.png")
        lbl_bg=Label(root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        '''
        image1=Image.open("button.png")
        image1=image1.resize((40,40), Image.ANTIALIAS,)
        self.btn_image=ImageTk.PhotoImage(image1) 
        btn_flight=Button(image=self.btn_image,cursor="hand2",bd=0,bg="#7DD3EE",activebackground="#7DD3EE")
        btn_flight.place(x=80,y=75)
        '''
        
        #========menu frame====
        self.menu_frame=Frame(self.root,bg="white")
        self.menu_frame.place(x=50,y=120,width=600,height=600)
        
        #== title name & icon===
        image2=Image.open(r"bookflight.png")
        image2=image2.resize((115,35), Image.ANTIALIAS,)
        self.btn_bookfl=ImageTk.PhotoImage(image2) 
        btn_change_to_book=Button(self.menu_frame,image=self.btn_bookfl,cursor="hand2",bd=0,bg="white",activebackground="white",command=self.book_flight_window).place(x=15,y=15,width=130,height=50)
        #========real time clock =====
        self.my_label_time = Label(self.menu_frame,text="",font=("glacial indifference",18),fg="#545454",bg="white")
        self.my_label_time.place(x=425,y=20)
        self.clock_fxn()
        self.book_flight_window()            #calling book flight frame , journey details from user
        
    def clock_fxn(self):             #realtime clock fxn
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")  
        self.my_label_time.config(text=hour + ":" + minute + ":" + second)
        self.my_label_time.after(1000, self.clock_fxn)
    #====book flight====
    def book_flight_window(self):
        #=====book flight frame====
        self.book_flight_frame=LabelFrame(self.root,bd=0,fg="white",bg="white")
        self.book_flight_frame.place(x=53,y=180,height=530,width=595)
        self.book_flight_frame.focus()
        self.book_flight_frame.grab_set()
        #=====oneway roundtrip====
        self.route=StringVar()
        oneway=Radiobutton(self.book_flight_frame,text="One Way", value="One Way", variable=self.route, font=("glacial indifference", 19),fg="#545454",bg="white",command=self.date1).place(x=15,y=10)
        roundtrip=Radiobutton(self.book_flight_frame,text="Round Trip",value="Round trip", variable=self.route, font=("glacial indifference",19),fg="#545454",bg="white",command=self.date2).place(x=200,y=10)
        self.route.set('One Way')

        #====from and To====
        options = ['Ahmedabad (AMD)', 'Agra (AGR)' ,'Agartala (IXA)','Aizawal (AJL)','Amritsar (ATQ)','Aurangabad (IXU)','Bengaluru (BLR)','Bagdogra (IXB)','Belagavi (IXG)','Bhopal (BHO)','Bhubaneshwar (BBI)','Chandigarh (IXC)','Chennai (MAA)','Coimbatore (CJB)','Dehradun (DED)','Delhi (DEL)','Dibrugarh (DIB)','Dimapur (DMU)','Durgapur (RDP)','Gaya (GAY)','Goa (GOI)','Gorakhpur (GOP)','Guwahati (GAU)','Mizoram (AJL)','Hindon (HDX)','Hubli (HBX)','Hyderabad (HYD)','Imphal (IMF)'
        ,'Indore (IDR)','Jabalpur (JLR)','Jaipur (JAI)','Jammu (IXJ)','Jodhpur (JDH)','Jorhat (JRH)','Kannur (CNN)','Kochi (COK)','Kolhapur (KLH)','Kolkata (CCU)'
        ,'Kozhikode (CCJ)','Kurnool (KJB)','Leh (IXL)','Lucknow (LKO)','Madurai (IXM)','Mangaluru (IXE)','Mumbai (BOM)','Mysore (MYQ)','Nagpur (NAG)','Patna (PAT)'
        ,'Port Blair (IXZ)','Prayagraj (IXD)','Pune (PNQ)','Raipur (RPR)','Rajahmundry (RJA)','Rajkot(RKT)','Ranchi (IXR)','Shillong (SHL)','Shirdi (SAG)','Silchar (IXS)'
        ,'Srinagar (SXR)','Surat (STV)','Thiruvananthapuram (TRV)','Tiruchirappalli (TRZ)','Tirupati (TIR)','Tuticorin (TCR)','Udaipur (UDR)','Vadodara (BDQ)','Varanasi (VNS)'
        ,'Vijayawada (VGA)','Visakhapatnam (VTZ)']
        
        dpt_from=Label(self.book_flight_frame ,text="From",font=("glacial indifference",13),fg="#545454",bg="white").place(x=15,y=70)
        self.departure_cmb=StringVar()
        self.departure_cmb=ttk.Combobox(self.book_flight_frame,font=("glacial indifference",15),state='readonly',justify=CENTER)
        self.departure_cmb['values']=(options)
        self.departure_cmb.place(x=15,y=95,width=250)
        self.departure_cmb.set("Select Departure City")
        self.departure_cmb.bind('<<ComboboxSelected>>', self.combobox_from)
        
        arr_to=Label(self.book_flight_frame ,text="To",font=("glacial indifference",13),fg="#545454",bg="white").place(x=300,y=70)
        self.arrival_cmb=StringVar()
        self.arrival_cmb=ttk.Combobox(self.book_flight_frame,font=("glacial indifference",15),state='readonly',justify=CENTER)
        self.arrival_cmb['values']=(options)
        self.arrival_cmb.place(x=300,y=95,width=250)
        self.arrival_cmb.set("Select Arrival City")
        self.arrival_cmb.bind('<<ComboboxSelected>>', self.combobox_from)
   
    
        #====departure n return dates====
        self.my_label2=Label(self.book_flight_frame, text="Departure Date: ",font=("glacial indifference",13),fg="#545454",bg="white").place(x=15,y=160)
        self.my_label3=Label(self.book_flight_frame, text="Return Date: ",font=("glacial indifference",13),fg="#545454",bg="white").place(x=300,y=160)
        
        self.real_date=datetime.datetime.now()
        self.date=self.real_date.day
        self.year=(self.real_date.year)
        self.month=self.real_date.month
        self.mindate = datetime.date(year=self.year, month=self.month, day=self.date)

        self.cal_dep = DateEntry(self.book_flight_frame, width=25,font=("glacial indifference",13),mindate=self.mindate,weekendbackground="skyblue", headersbackground ="light gray",selectbackground ="#36477F",normalbackground ="sky blue",state='readonly',date_pattern='dd-mm-yyyy', justify=CENTER,day=self.date, month=self.month,year=self.year, background='#545454', foreground='white')
        self.cal_dep.place(x=15,y=185)
        self.cal_arr = DateEntry(self.book_flight_frame, width=25,font=("glacial indifference",13),mindate=self.mindate,weekendbackground="skyblue", headersbackground ="green",selectbackground ="red",normalbackground ="sky blue",state='disabled',date_pattern='dd-mm-yyyy', justify=CENTER,day=self.date, month=self.month,year=self.year, background='#545454', foreground='white')
        self.cal_arr.place(x=300,y=185)
        self.cal_arr1 = DateEntry(self.book_flight_frame, width=25,state='readonly',date_pattern='dd-mm-yyyy', justify=CENTER,day=24, month=3,year=2004, background='#545454', foreground='white')
        self.cal_arr1.place(x=1000,y=1000)
        #=====passenger num====
        self.var = IntVar()
        self.spin1 = Spinbox(self.book_flight_frame,from_=1, to=9,font=("glacial indifference",15),state='readonly',textvariable=self.var).place(x=15,y=290,width=250)
        self.var.set(1)
        self.my_label_passnum=Label(self.book_flight_frame, text="Passenger(s)",font=("glacial indifference",13),fg="#545454",bg="white").place(x=15,y=260)
        #======passenger class======       
        self.my_class=Label(self.book_flight_frame, text="Class: ",font=("glacial indifference",13),fg="#545454",bg="white").place(x=300,y=260)
        self.classs_cmb=ttk.Combobox(self.book_flight_frame,font=("glacial indifference",15),state='readonly',justify=CENTER)
        self.classs_cmb['values']=('Economy','Buisness','First')
        self.classs_cmb.place(x=300,y=290,width=250)
        self.classs_cmb.set("Economy")
        #======pay in currency======       
        self.my_currency=Label(self.book_flight_frame, text="Pay in(currency): ",font=("glacial indifference",13),fg="#545454",bg="white").place(x=15,y=350)
        self.curren_cmb=ttk.Combobox(self.book_flight_frame,font=("glacial indifference",15),state='readonly',justify=CENTER)
        self.curren_cmb['values']=('(₹)Indian_Rupees')
        self.curren_cmb.place(x=15,y=380,width=250)
        self.curren_cmb.set("(₹)Indian Rupees")
        #=====search flight btn=======
        image67=Image.open(r"searchflight.png")
        image67=image67.resize((320,170), Image.ANTIALIAS,)
        self.btn_searchflight=ImageTk.PhotoImage(image67) 
        btn_flightsearch=Button(self.book_flight_frame,image=self.btn_searchflight,cursor="hand2",bd=0,activebackground="white",command=self.call_search).place(x=270,y=370,width=300,height=170)
    #====oneway n round trip selection fxn=====
    def date1(self):
        oneway=Radiobutton(self.book_flight_frame,text="One Way", value="One Way", variable=self.route, font=("glacial indifference",19),fg="black",bg="white",command=self.date1).place(x=15,y=10)
        roundtrip=Radiobutton(self.book_flight_frame,text="Round Trip",value="Round trip", variable=self.route, font=("glacial indifference",19),fg="#545454",bg="white",command=self.date2).place(x=200,y=10)
        self.cal_arr = DateEntry(self.book_flight_frame, width=25,font=("glacial indifference",13),mindate=self.mindate,weekendbackground="skyblue", headersbackground ="green",selectbackground ="red",normalbackground ="sky blue",state='disabled',date_pattern='dd-mm-yyyy', justify=CENTER,day=self.date, month=self.month,year=self.year, background='#545454', foreground='white')
        self.cal_arr.place(x=300,y=185)
        
    def date2(self):
        roundtrip=Radiobutton(self.book_flight_frame,text="Round Trip",value="Round trip", variable=self.route, font=("glacial indifference",19),fg="black",bg="white",command=self.date2).place(x=200,y=10)
        oneway=Radiobutton(self.book_flight_frame,text="One Way", value="One Way", variable=self.route, font=("glacial indifference",19),fg="#545454",bg="white",command=self.date1).place(x=15,y=10)
        self.cal_arr = DateEntry(self.book_flight_frame, width=25,font=("glacial indifference",13),mindate=self.mindate,weekendbackground="skyblue", headersbackground ="light gray",selectbackground ="#36477F",normalbackground ="sky blue",state='readonly',date_pattern='dd-mm-yyyy', justify=CENTER,day=self.date, month=self.month,year=self.year, background='#545454', foreground='white')
        self.cal_arr.place(x=300,y=185)
    #=====departure/arrival cmb value get====
    def combobox_from(self,event):
        self.dep_cmb = self.departure_cmb.get()
        self.arr_cmb = self.arrival_cmb.get()
        self.currency = self.curren_cmb.get()
        self.class_type = self.classs_cmb.get()
        if self.dep_cmb==self.arr_cmb:
            self.arrival_cmb.set("Select Arrival City")
    #===== search btn function======
    def call_search(self):
        if self.departure_cmb.get()=="" or self.arrival_cmb.get()=="" or self.arrival_cmb.get()=="Select Arrival City":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
            return
        self.passengers=self.var.get()    #  use at search flight button function
        self.departure_date=self.cal_dep.get_date()
        self.triptype=self.route.get()
        if self.triptype=="Round trip":
            self.return_date=self.cal_arr.get_date()
        self.oneway_search_flight_window()
       # elif self.route=="Round Trip":
        #    self.roundtrip_search_window()
 #=================================================================================================================
    #=====oneway flight details screen=====       
    def oneway_search_flight_window(self):
        self.root.destroy()
        root2=Tk()
        self.root2=root2
        self.root2.title("Search Flight")
        self.root2.geometry("1920x900+-8+0")
        frame2=LabelFrame(self.root2,bg="#334584",bd=0)
        frame2.place(x=0,y=145,width=1740,height=100) 
        btn_flightsearch=Label(frame2,cursor="hand2",bd=0,background="#334584").place(x=0,y=0,width=1740,height=140)
        #=====date======
        lbl_date=Label(frame2,text="Departure Date: ",font=("glacial indifference",13),fg="white",bg="#334584").place(x=40,y=10)
        date=Label(frame2,text=self.departure_date,font=("glacial indifference",25,"underline"),fg="white",bg="#334584" ).place(x=40,y=35)
        #========from=====
        lbl_from=Label(frame2 ,text="From",font=("glacial indifference",13),fg="white",bg="#334584").place(x=330,y=10)
        from_city=Label(frame2,text=self.dep_cmb ,font=("glacial indifference",25,"underline"),fg="white",bg="#334584" ).place(x=330,y=35)
        #=====to======
        lbl_to=Label(frame2 ,text="To",font=("glacial indifference",13),fg="white",bg="#334584").place(x=680,y=10)
        to_city=Label(frame2,text=self.arr_cmb ,font=("glacial indifference",25,"underline"),fg="white",bg="#334584" ).place(x=680,y=35)
        #=====passenger=====
        lbl_pnum=Label(frame2 ,text="Passenger(s)",font=("glacial indifference",13),fg="white",bg="#334584").place(x=1050,y=10)
        pass_no=Label(frame2,text=self.passengers,font=("glacial indifference",25,"underline"),fg="white",bg="#334584").place(x=1050,y=35)
        #====pnr number====
        Pnr_Number="5"+str(rd.choice(string.ascii_letters))+str(rd.randint(100,999))
        self.pnr_num=Pnr_Number
        lbl_pnr=Label(frame2 ,text="Your Airlines Reference:",font=("glacial indifference",13),fg="white",bg="#334584").place(x=1340,y=10)
        pnr_show=Label(frame2,text=self.pnr_num,font=("glacial indifference",25,"underline"),fg="white",bg="#334584").place(x=1340,y=35)
        #========flight detail table 1========
        self.table1 = ttk.Treeview(self.root2)
        style = ttk.Style()
        #pick a theme
        style.theme_use("alt")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('glacial indifference', 17),rowheight=40,background="white",foreground="white",fieldbackground="white") # Modify the font of the body
        style.configure("Treeview.Heading", font=('glacial indifference', 15),background="#A7BCDC") # Modify the font of the headings
        style.map("Treeview", background=[('selected','#A7BCDC')])
        
        #stripped rows tags
        self.table1.tag_configure('oddrow',background="white")
        self.table1.tag_configure('evenrow',background="white")   #Paleturquoise

        self.table1['columns']=('Srno', 'Flight Number', 'Origin','Destination', 'Departure', 'Arrival','Days Of Operation', 'Aircraft Carrier', 'Fare')
        self.table1.column('#0', width=0, stretch=NO)
        self.table1.column('Srno', anchor=CENTER, width=100)
        self.table1.column('Flight Number', anchor=CENTER, width=150)
        self.table1.column('Origin', anchor=CENTER, width=270)
        self.table1.column('Destination', anchor=CENTER, width=270)
        self.table1.column('Departure', anchor=CENTER, width=150)
        self.table1.column('Arrival', anchor=CENTER, width=150)
        self.table1.column('Days Of Operation', anchor=CENTER, width=180)
        self.table1.column('Aircraft Carrier', anchor=CENTER, width=170)
        self.table1.column('Fare', anchor=CENTER, width=160)
 
        self.table1.heading('#0', text='', anchor=CENTER)
        self.table1.heading('Srno', text='Srno', anchor=CENTER)
        self.table1.heading('Flight Number', text='Flight Number', anchor=CENTER)
        self.table1.heading('Origin', text='Origin', anchor=CENTER)
        self.table1.heading('Destination', text='Destination', anchor=CENTER)
        self.table1.heading('Departure', text='Departure', anchor=CENTER)
        self.table1.heading('Arrival', text='Arrival', anchor=CENTER)
        self.table1.heading('Days Of Operation', text='Days Of Operation', anchor=CENTER)
        self.table1.heading('Aircraft Carrier', text='Aircraft Carrier', anchor=CENTER)
        self.table1.heading('Fare', text='Fare', anchor=CENTER)
        self.table1.place(x=0,y=245,height=250)
        self.table1.bind("<ButtonRelease-1>",self.select_record)
        self.query_database()
        #======table1 over ======
        #===heading poster====
        poster1=Image.open(r"seflight.png")
        poster1=poster1.resize((1740,140), Image.ANTIALIAS)
        self.poster1=ImageTk.PhotoImage(poster1)
       #=====covid guidline poster====
        poster2=Image.open(r"maskon.png")
        poster2=poster2.resize((1600,255), Image.ANTIALIAS)
        self.poster2=ImageTk.PhotoImage(poster2)
        
        #=====images==============
        self.lbl1=Label(self.root2,image=self.poster1,bd=0)
        self.lbl1.place(x=0, y=0)
        self.lbl2=Label(self.root2,image=self.poster2)
        self.lbl2.place(x=-2, y=465)
        
        #==============frame4 continue button, selected flight details shown =====
        self.frame4=Frame(self.root2,bg="#334584",bd=2)
        self.frame4.place(x=0,y=730,width=1600,height=200)
        
        continue_btn=Button(self.frame4,text="Continue",font=("glacial indifference",23),fg="white",bg="#7398D0",bd=2,cursor="hand2",command=self.passenger_info_window).place(x=1280,y=30,width=180,height=50)
        
        self.from_entry=Entry(self.frame4,font=("glacial indifference",15, "bold"),fg="black",bd=2,bg="white",state="readonly")
        self.from_entry.place(x=20,y=18,width=250)
        
        self.from_entry1=Entry(self.frame4,font=("glacial indifference",15, "bold"),fg="black",bd=2,bg="white",state="readonly")
        self.from_entry1.place(x=20,y=50,width=250)
        
        self.to_entry=Entry(self.frame4,font=("glacial indifference",15, "bold"),bd=2,fg="black",bg="white",state="readonly")
        self.to_entry.place(x=300,y=18,width=250)
        
        self.to_entry1 = Entry(self.frame4,font=("glacial indifference",15, "bold"),fg="black",bd=2,bg="white",state="readonly")
        self.to_entry1.place(x=300,y=50,width=250)
        
        self.Fare_entry = Entry(self.frame4,font=("glacial indifference",15, "bold"),fg="black",bd=2,bg="white",state='disabled')
        self.Fare_entry.place(x=590,y=18,width=250)
        
        self.Fare_entry1 = Entry(self.frame4,font=("glacial indifference",15, "bold"),fg="black",bd=2,bg="white",state='disabled')
        self.Fare_entry1.place(x=590,y=50,width=250)
        
        total_fare=Label(self.frame4 ,text="Total Fare",font=("glacial indifference",15),fg="white",bg="#334584").place(x=880,y=18)
        self.tfare_entry = Entry(self.frame4,font=("glacial indifference",15, "bold"),fg="black",bd=2,bg="white",state='disabled')
        self.tfare_entry.place(x=880,y=50,width=250)
        
        if self.triptype=="Round trip":
            self.roundtrip_search_window()


        #select record oneway search flight data selection 
    def select_record(self,e):
        #clear entry boxes
        self.Fare_entry.configure(state='normal')
        self.tfare_entry.configure(state='normal')
        self.to_entry.configure(state='normal')
        self.from_entry.configure(state='normal')

        self.from_entry.delete(0, END)
        self.to_entry.delete(0, END)
        self.Fare_entry.delete(0, END)
        self.tfare_entry.delete(0, END)

        self.selected = self.table1.focus()           # Grab record Number
        # Grab record values
        values = self.table1.item(self.selected, 'values')
        #====asign to variable==
        self.dep_flight_num=("Flight no. " + values[1])
        self.dep_flight_num_int=values[1]
        self.departing_from=values[2]
        self.departing_to=values[3]
        self.departure_time=values[4]
        self.departure_time2=values[5]
        # outpus to entry boxes
        self.from_entry.insert(0,values[2])
        self.to_entry.insert(0, values[3])
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial")
        cur=con.cursor()
        cur.execute("SELECT fare FROM onewayflight WHERE origin=%s and Destination=%s",(values[2],values[3]))
        result = cur.fetchall()
        for row in result:
            self.onewayfare = int("%10s"%row[0])*self.passengers  
        con.commit()
        con.close()
        if self.currency==("(₹)Indian Rupees"):
            tfare=("@","(₹)",self.onewayfare)
            self.t2fare=("₹",self.onewayfare)
       
        self.Fare_entry.insert(0,tfare)
        self.tfare_entry.insert(0,self.t2fare)
        self.Fare_entry.configure(state='disabled')
        self.tfare_entry.configure(state='disabled')
        self.to_entry.configure(state='disabled')
        self.from_entry.configure(state='disabled')
        #select record roundtrip search flight data selection 
    def select_record2(self,e):
        #clear entry boxes
        self.from_entry1.configure(state='normal')
        self.to_entry1.configure(state='normal')
        self.Fare_entry1.configure(state='normal')
        self.tfare_entry.configure(state='normal')

        self.from_entry1.delete(0, END)
        self.to_entry1.delete(0, END)
        self.Fare_entry1.delete(0, END)
        self.tfare_entry.delete(0, END)
        
        self.selected = self.table1.focus()           # Grab record Number
        # Grab record values
        values = self.table1.item(self.selected, 'values')
        #====asign to variable==
        self.dep_flight_num=("Flight no. " + values[1])
        self.arr_from=values[2]
        self.arr_to=values[3]
        self.arr_time=values[4]
        self.arr_time2=values[5]
        
        selected = self.table2.focus()           # Grab record Number
        # Grab record values
        values = self.table2.item(selected, 'values')
        # outpus to entry boxes
        self.arr_flight_num="Flight no. " + values[1]
        self.from_entry1.insert(0,values[2])
        self.to_entry1.insert(0,values[3])
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial")
        cur=con.cursor()
        cur.execute("SELECT fare FROM onewayflight WHERE origin=%s and Destination=%s",(values[2],values[3]))
        result1 = cur.fetchall()
        for row in result1:
            self.rtfare = int("%10s"%row[0])*self.passengers  
        con.commit()
        con.close()
        rt_tfare=("@",self.rtfare,"INR")
        self.rt_tfare2=(self.rtfare,"INR") 
        self.totalfare=((self.onewayfare+self.rtfare),"INR") 
        self.Fare_entry1.insert(0,(rt_tfare))
        self.tfare_entry.insert(0,self.totalfare)
        self.Fare_entry1.configure(state='disabled')
        self.tfare_entry.configure(state='disabled')
        self.from_entry1.configure(state='disabled')
        self.to_entry1.configure(state='disabled')

    def query_database(self):
         #=====connect sql to table 1====
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial")
        cur=con.cursor()
        cur.execute("SELECT * FROM onewayflight WHERE origin=%s and Destination=%s",(self.dep_cmb ,self.arr_cmb))
        records=cur.fetchall()
        # Add our data to the screen
        global count  
        count = 0
        for record in records:
            if count % 2 == 0:
                self.table1.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[3], record[4], record[5], record[6], record[2], record[7], record[8]), tags=('evenrow',))
            else:
                self.table1.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[3], record[4], record[5], record[6], record[2], record[7], record[8]), tags=('oddrow',))
               # increment counter
                count += 1
        con.commit()
        con.close()
        
    def query_database2(self):
         #=====connect sql to table 1====
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="trial")
        cur=con.cursor()
        cur.execute("SELECT * FROM onewayflight WHERE origin=%s and Destination=%s",(self.arr_cmb ,self.dep_cmb))
        records=cur.fetchall()
        # Add our data to the screen
        global count  
        count = 0
        for record in records:
            if count % 2 == 0:
                self.table2.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[3], record[4], record[5], record[6], record[2], record[7], record[8]), tags=('evenrow',))
            else:
                self.table2.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[3], record[4], record[5], record[6], record[2], record[7], record[8]), tags=('oddrow',))
               # increment counter
                count += 1
        con.commit()
        con.close()    
        
    def query_database3(self):
         #=====connect sql to table 1====
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="airlines")
        cur=con.cursor()
        pnr=str(self.pnr_num)
        cur.execute("SELECT title,Passenger_Name FROM pass_details WHERE PNR_no=%s",(pnr))
        result=cur.fetchall()
        # Add our data to the screen
        global count 
        count= 0
        for record in result:
            if count % 2 == 0:
                self.table3.insert(parent='', index='end', text='', values=(record[0],record[1]))
            else:
                self.table.insert(parent='', index='end', text='', values=(record[0],record[1]))
               # increment counter
                count += 1
        con.commit()
        con.close()           
    #=================roundtrip frame=========== 
    def roundtrip_search_window(self):
        self.lbl2.pack_forget()
        #=====return flight
        frame3=LabelFrame(self.root2,bg="#334584",text="Return trip",bd=2)
        frame3.place(x=0,y=410,width=1540,height=100)
        #=====date2====
        lbl_date2=Label(frame3,text="Return Date: ",font=("glacial indifference",13),fg="white",bg="#334584").place(x=0,y=5)
        date2=Label(frame3,text=self.return_date,font=("glacial indifference",25,"bold","underline"),fg="white",bg="#334584" ).place(x=0,y=30)
        #======== return from
        lbl_from=Label(frame3 ,text="From",font=("glacial indifference",13),fg="white",bg="#334584").place(x=290,y=5)
        from_city=Label(frame3,text=self.arr_cmb,font=("glacial indifference",25,"bold","underline"),fg="white",bg="#334584" ).place(x=290,y=30)
        #=====return to
        lbl_to=Label(frame3 ,text="To",font=("glacial indifference",13),fg="white",bg="#334584").place(x=640,y=5)
        to_city=Label(frame3,text=self.dep_cmb ,font=("glacial indifference",25,"bold","underline"),fg="white",bg="#334584" ).place(x=640,y=30)
        #=====passenger
        lbl_pnum=Label(frame3 ,text="Passenger(s)",font=("glacial indifference",13),fg="white",bg="#334584").place(x=1000,y=5)
        pass_no=Label(frame3,text=self.passengers,font=("glacial indifference",25,"bold","underline"),fg="white",bg="#334584").place(x=1000,y=30)
       
        #========table 1========
        self.table2 = ttk.Treeview(self.root2)
        style = ttk.Style()
        #pick a theme
        style.theme_use("alt")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 17),rowheight=40,background="white",foreground="white",fieldbackground="white") # Modify the font of the body
        style.configure("Treeview.Heading", font=('Calibri', 15,'bold'),background="light sky blue") # Modify the font of the headings
        style.map("Treeview", background=[('selected','Dodgerblue')])
        
        #stripped rows tags
        self.table2.tag_configure('oddrow',background="white")
        self.table2.tag_configure('evenrow',background="white")   #Paleturquoise

        self.table2['columns']=('Srno', 'Flight Number', 'Origin','Destination', 'Departure', 'Arrival','Days Of Operation', 'Aircraft Carrier', 'Fare')
        self.table2.column('#0', width=0, stretch=NO)
        self.table2.column('Srno', anchor=CENTER, width=100)
        self.table2.column('Flight Number', anchor=CENTER, width=150)
        self.table2.column('Origin', anchor=CENTER, width=240)
        self.table2.column('Destination', anchor=CENTER, width=240)
        self.table2.column('Departure', anchor=CENTER, width=150)
        self.table2.column('Arrival', anchor=CENTER, width=150)
        self.table2.column('Days Of Operation', anchor=CENTER, width=180)
        self.table2.column('Aircraft Carrier', anchor=CENTER, width=170)
        self.table2.column('Fare', anchor=CENTER, width=160)
 
        self.table2.heading('#0', text='', anchor=CENTER)
        self.table2.heading('Srno', text='Srno', anchor=CENTER)
        self.table2.heading('Flight Number', text='Flight Number', anchor=CENTER)
        self.table2.heading('Origin', text='Origin', anchor=CENTER)
        self.table2.heading('Destination', text='Destination', anchor=CENTER)
        self.table2.heading('Departure', text='Departure', anchor=CENTER)
        self.table2.heading('Arrival', text='Arrival', anchor=CENTER)
        self.table2.heading('Days Of Operation', text='Days Of Operation', anchor=CENTER)
        self.table2.heading('Aircraft Carrier', text='Aircraft Carrier', anchor=CENTER)
        self.table2.heading('Fare', text='Fare', anchor=CENTER)
        self.table2.place(x=0,y=510,height=215)
        self.table2.bind("<ButtonRelease-1>",self.select_record2)
        self.query_database2()
        #======table2 over ======
        
        
    def passenger_info_window(self):
        if self.Fare_entry.get()=="" or self.tfare_entry.get()=="" :
                messagebox.showerror("Error","Please select your flight",parent=self.root2)
                return
        elif self.triptype =="Round trip":
            if self.Fare_entry1.get()=="":
                messagebox.showerror("Error","Please select flight",parent=self.root2)
                return        
        self.root2.destroy()
        root3=Tk()
        self.root3=root3
        self.root3.title("Passenger Details")
        self.root3.geometry("1920x1080+-8+0")
        
        #======heading poster===
        poster1=Image.open(r"seflight.png")
        poster1=poster1.resize((1640,140), Image.ANTIALIAS)
        self.poster1=ImageTk.PhotoImage(poster1)
        self.lbl1=Label(self.root3,image=self.poster1)
        self.lbl1.place(x=-2, y=0)
        
        #===========frame2====
        frame2=LabelFrame(self.root3,bg="#334584")
        frame2.place(x=-2,y=140,width=1650,height=100)
        #=====date======
        lbl_date=Label(frame2,text="Departure Date: ",font=("glacial indifference",13),fg="white",bg="#334584").place(x=40,y=10)
        date=Label(frame2,text=self.departure_date,font=("glacial indifference",25,"underline"),fg="white",bg="#334584" ).place(x=40,y=35)
        #========from=====
        lbl_from=Label(frame2 ,text="From",font=("glacial indifference",13),fg="white",bg="#334584").place(x=330,y=10)
        from_city=Label(frame2,text=self.dep_cmb ,font=("glacial indifference",25,"underline"),fg="white",bg="#334584" ).place(x=330,y=35)
        #=====to======
        lbl_to=Label(frame2 ,text="To",font=("glacial indifference",13),fg="white",bg="#334584").place(x=680,y=10)
        to_city=Label(frame2,text=self.arr_cmb ,font=("glacial indifference",25,"underline"),fg="white",bg="#334584" ).place(x=680,y=35)
        #=====passenger=====
        lbl_pnum=Label(frame2 ,text="Passenger(s)",font=("glacial indifference",13),fg="white",bg="#334584").place(x=1040,y=10)
        pass_no=Label(frame2,text=self.passengers,font=("glacial indifference",25,"underline"),fg="white",bg="#334584").place(x=1040,y=35)
        #=======PNR number=====
        lbl_pnr=Label(frame2 ,text="Your Airlines Reference:",font=("glacial indifference",13),fg="white",bg="#334584").place(x=1340,y=10)
        pnr_show=Label(frame2,text=self.pnr_num,font=("glacial indifference",25,"underline"),fg="white",bg="#334584").place(x=1340,y=35)

         #===========frame3====
        frame3=Frame(self.root3,bg="white",bd=2)
        frame3.place(x=560,y=240,width=530,height=650)
        #====entry box variables=====
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_phoneno=IntVar()
        self.var_emailid=StringVar()
        
        #======seat bg 1===
        poster21=Image.open(r"plane_seats1.jpg")
        poster21=poster21.resize((560,640), Image.ANTIALIAS)
        self.poster21=ImageTk.PhotoImage(poster21)
        self.lbl1=Label(self.root3,image=self.poster21,bd=0)
        self.lbl1.place(x=-2, y=240)
        
        #======seat bg2 ===
        poster22=Image.open(r"plane_seat2.JPG")
        poster22=poster22.resize((590,640), Image.ANTIALIAS)
        self.poster22=ImageTk.PhotoImage(poster22)
        self.lbl1=Label(self.root3,image=self.poster22,bd=0)
        self.lbl1.place(x=1050, y=240)
        
        
        #=====passenger details heading======
        lbl_pass=Label(frame3,text="Passengers Details ",font=("glacial indifference",25,"bold"),fg="black",bg="white").place(x=85,y=45)
        
        lbl_title=Label(frame3,text="Title",font=("glacial indifference",15),fg="black",bg="white").place(x=85,y=110)
        self.title_cmb=StringVar()
        self.title_cmb=ttk.Combobox(frame3,font=("glacial indifference",15),state='readonly',justify=CENTER)
        self.title_cmb['values']=('MR','MRS','MS')
        self.title_cmb.place(x=85,y=140,width=120)
        self.title_cmb.set("Select Title")
        self.title_cmb.current(0)
        self.title_cmb.bind('<<ComboboxSelected>>', self.combobox_from)
        
        lbl_fname=Label(frame3,text="First Name ",font=("glacial indifference",15),fg="black",bg="white").place(x=85,y=180)
        self.fname_entry=Entry(frame3,font=("glacial indifference",15),textvariable=self.var_fname,fg="black",bd=2,bg="white")
        self.fname_entry.place(x=85,y=220,width=250)
        
        lbl_lnames=Label(frame3,text="Last Name ",font=("glacial indifference",15),fg="black",bg="white").place(x=85,y=260)
        self.lname_entry=Entry(frame3,font=("glacial indifference",15),textvariable=self.var_lname,fg="black",bd=2,bg="white")
        self.lname_entry.place(x=85,y=300,width=250)
        
        lbl_phoneno=Label(frame3,text="Phone no. ",font=("glacial indifference",15),fg="black",bg="white").place(x=85,y=340)
        self.phno_entry=Entry(frame3,font=("glacial indifference",15),textvariable=self.var_phoneno,fg="black",bd=2,bg="white")
        self.phno_entry.place(x=85,y=380,width=250)
        self.phno_entry.delete(0, END)
        
        lbl_lnames=Label(frame3,text="Email-Address",font=("glacial indifference",15),fg="black",bg="white").place(x=85,y=420)
        self.email_entry=Entry(frame3,font=("glacial indifference",15),textvariable=self.var_emailid,fg="black",bd=2,bg="white")
        self.email_entry.place(x=85,y=460,width=250)
        
        self.lbl_addpass=Label(self.root3,text="Save & Next",font=("glacial indifference",14),bg="#7398D0",fg="white",bd=5)
        self.lbl_addpass.place(x=1280,y=670,width=220,height=40)
        
        self.add_pass_btn=Button(self.root3,text="Add Passenger: 1",font=("glacial indifference",17,"bold"),fg="white",bg="#7398D0",bd=2,cursor="hand2",command=self.update_count)
        self.add_pass_btn.place(x=1280,y=720,width=220,height=50)
        self.bttn_clicks = 1
        
        
    def update_count(self):
        try:
            if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_phoneno.get()=="" or self.var_emailid.get()=="" or self.title_cmb.get()=="":
                messagebox.showerror("Error","All Fiels Are Required, please fill all details",parent=self.root3)
                return
            else:
                self.add_pass_Details_db()
                self.title_cmb.current(0)
                self.fname_entry.delete(0, END )
                self.lname_entry.delete(0, END )
                self.phno_entry.delete(0, END )
                self.email_entry.delete(0, END )
                
                self.bttn_clicks += 1
                self.add_pass_btn['text'] = "add Passenger️: " + str(self.bttn_clicks)
                
                if self.bttn_clicks > self.passengers:
                    self.title_cmb.configure(state='disabled')
                    self.fname_entry.configure(state='disabled')
                    self.lname_entry.configure(state='disabled')
                    self.phno_entry.configure(state='disabled')
                    self.email_entry.configure(state='disabled')
                    self.add_pass_btn.destroy()
                    self.lbl_addpass.configure(text="Passenger details added")
                    self.continue_btn=Button(self.root3,text="Continue",font=("glacial indifference",17,"bold"),borderwidth=5,fg="white",bg="#7398D0",bd=2,cursor="hand2",command=self.payment_window)
                    self.continue_btn.place(x=1280,y=720,width=220,height=50)
        except Exception as es:
                messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root3)
            #======add passenger details into sql database ======
    def add_pass_Details_db(self):
        self.pass_name = self.var_fname.get() + "" + self.var_lname.get()
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="airlines")
        cur=con.cursor()
        cur.execute("insert into pass_details (PNR_no,title,Passenger_Name,Phone_no,email_id) values(%s,%s,%s,%s,%s)",(self.pnr_num,self.title_cmb.get(),self.pass_name,self.var_phoneno.get(),self.var_emailid.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success","Passenger Added Successfully",parent=self.root3)
        
    
    def payment_window(self):
        self.root3.destroy()
        root4=Tk()
        self.root4=root4
        self.root4.title("Search Flight")
        self.root4.geometry("1920x1080+-8+0")
        
        #======heading poster===
        poster10=Image.open(r"seflight.png")
        poster10=poster10.resize((1920,150), Image.ANTIALIAS)
        self.poster10=ImageTk.PhotoImage(poster10)
        self.lbl1=Label(self.root4,image=self.poster10,bd=0)
        self.lbl1.place(x=0, y=0)
        #===========frame2====
        frame1=Frame(self.root4,bg="#E8EEFF",bd=2)
        frame1.place(x=0,y=150,width=1920,height=1080)
        self.lbl_payheading=Label(frame1,text="Payment Method",font=("glacial indifference",20),fg="black",bg="#E8EEFF")
        self.lbl_payheading.place(x=30,y=30)
        self.creditdebit_btn=Button(frame1,text="Credit/Debit Card",font=("glacial indifference",15,),bg="#334584",fg="white",activebackground="#334584",activeforeground="white",bd=0,command=self.credit_debit_card)
        self.creditdebit_btn.place(x=30,y=100,width=170,height=40)
        self.creditdebit_btn=Button(frame1,text="UPI ",font=("glacial indifference",15,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.upi)
        self.creditdebit_btn.place(x=30,y=155,width=170,height=40)
        self.creditdebit_btn=Button(frame1,text="Net Banking",font=("glacial indifference",15,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.netbanking)
        self.creditdebit_btn.place(x=30,y=210,width=170,height=40)
        self.credit_debit_card()
        
        myframe1=Frame(self.root4,bg="white",bd=2)
        myframe1.place(x=1050,y=212,width=470,height=570)
        
        my_canvas=Canvas(myframe1)
        my_canvas.pack(side=LEFT,fill="both", expand=1)
        
         # Add A Scrollbar To The Canvas
        my_scrollbar=ttk.Scrollbar(myframe1, orient="vertical", command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        
        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta/ 120)), "units")
        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
      
        # Create ANOTHER Frame INSIDE the Canvas
        self.framebs1=Frame(my_canvas)
        self.framebs1.config(bg="white")
        self.framebs1.pack(side=LEFT,fill="both", expand=1)
        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=self.framebs1, anchor="nw")
        
        for thing in range(40):
        	my_label = Label(self.framebs1, text="",bg="white").grid(row=thing, column=thing,padx=10,pady=10)



        self.lbl_bs_heading=Label(self.framebs1,text="Booking summary",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=10,y=10)
        self.lbl_departing=Label(self.framebs1,text="Departing",font=("glacial indifference",17,"bold"),fg="black",bg="white").place(x=10,y=60)
        self.lbl_flight_no=Label(self.framebs1,text=(self.dep_flight_num),font=("glacial indifference",11),fg="black",bg="white").place(x=10,y=90)

        self.lbl_dep_from1=Label(self.framebs1,text=self.departing_from,font=("glacial indifference",14),fg="black",bg="white").place(x=10,y=130)
        self.lbl_dep_Date1=Label(self.framebs1,text=self.departure_date ,font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=155)
        self.lbl_dep_time1=Label(self.framebs1,text=self.departure_time,font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=175)
        self.lbl_arrow=Label(self.framebs1,text="➡️",font=("glacial indifference",25),fg="gray",bg="white").place(x=190,y=130)
        
        self.lbl_arr_from1=Label(self.framebs1,text=self.departing_to,font=("glacial indifference",14),fg="black",bg="white").place(x=270,y=130)
        self.lbl_arr_Date1=Label(self.framebs1,text=self.departure_date ,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=155)
        self.lbl_arr_time1=Label(self.framebs1,text=self.departure_time2,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=175)
        if self.triptype =="Round trip":
            self.return_details()
        else:
            pass

        #========table 3, passenger info table show========
        self.table3 = ttk.Treeview(self.framebs1)
        
        style = ttk.Style()
        #pick a theme
        style.theme_use("alt")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('glacial indifference',13),background="white",foreground="white",fieldbackground="white") # Modify the font of the body
        style.configure("Treeview.Heading", font=('glacial indifference', 12),background="#334584",foreground="white") # Modify the font of the headings
        style.map("Treeview", background=[('selected','gray')])
        
        #stripped rows tags
        self.table3.tag_configure('oddrow',background="white")
        self.table3.tag_configure('evenrow',background="white")   #Paleturquoise

        self.table3['columns']=('title','Passenger(s)')
        self.table3.column('#0', width=0, stretch=NO)
        self.table3.column('title', anchor=W, width=100,stretch=NO)
        self.table3.column('Passenger(s)', anchor=W, width=328,stretch=NO)
        self.table3.heading('#0', text='', anchor=W)
        self.table3.heading('Passenger(s)', text='Passenger(s)', anchor=W)
        self.table3.heading('title', text='Title', anchor=W)
        self.table3.place(x=10,y=385,width=430,height=200)
        self.query_database3()
        
        self.lbl_bs_heading2=Label(self.framebs1,text="Price summary",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=10,y=590)
        self.lbl_departing=Label(self.framebs1,text="Regular Fare -",font=("glacial indifference",12,"bold"),fg="black",bg="white").place(x=10,y=650)
        self.lbl_dep_from1=Label(self.framebs1,text=(self.departing_from+"  To"),font=("glacial indifference",12,"bold"),fg="black",bg="white").place(x=130,y=650)
        self.lbl_arr_from1=Label(self.framebs1,text=self.departing_to,font=("glacial indifference",12,"bold"),fg="black",bg="white").place(x=300,y=650)

        self.lbl_airfare=Label(self.framebs1,text="Airfare charges",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=690)
        self.lbl_1waycharge=Label(self.framebs1,text=(self.t2fare),font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=690)
        self.lbl_feesntaxes=Label(self.framebs1,text="Fees & Taxes",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=720)
       # fare=int(self.onewayfare)
        tax=(((self.onewayfare*7.5)/100),"INR")
        tax_int=((self.onewayfare*7.5)/100)
        self.lbl_1waycharge1=Label(self.framebs1,text=tax,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=720)
        if self.triptype =="Round trip":
            self.return_details2()
        self.lbl_convi_fee=Label(self.framebs1,text="Convenience fee",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=850)
        if self.triptype =="Round trip":
            fees=(600,"INR")
            fee=600
        elif self.triptype =="One Way":
            fees=(300,"INR")
            fee=300
        #======class charge n  details====
        if self.triptype == "One Way":
            if self.class_type=="Economy":
                class_fee=(0*self.passengers,'0% charge')
                class_fee_int=0*self.passengers
            elif self.class_type=="Buisness":
                class_fee = ((self.onewayfare*30)/100)*self.passengers,"30% extra charges"
                class_fee_int=((self.onewayfare*30)/100)
            elif self.class_type=="First":
                class_fee=(((self.onewayfare*40)/100),"(40% extra charges)")
                class_fee_int=((self.onewayfare*40)/100)
           
        if self.triptype =="Round trip":
            if self.class_type=="Economy":
                class_fee=(0*self.passengers*2,'0% charge')
                class_fee_int=0*self.passengers*2
            elif self.class_type=="Buisness":
                class_fee = ((self.onewayfare*30)/100)*self.passengers*2,"30% extra charges"
                class_fee_int=((self.onewayfare*30)/100)*2
            elif self.class_type=="First":
                class_fee=(((self.onewayfare*40)/100)*self.passengers*2,"(40% extra charges)")
                class_fee_int=((self.onewayfare*40)/100)*2
                
        self.lbl_cinvi_fees2=Label(self.framebs1,text=fees,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=850)
        self.lbl_class=Label(self.framebs1,text="Class type",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=890)
        self.lbl_class=Label(self.framebs1,text=self.class_type,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=890)
        self.lbl_class2=Label(self.framebs1,text="Class charges",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=920)
        self.lbl_class2=Label(self.framebs1,text=class_fee,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=920)


        self.lbl_total_amt=Label(self.framebs1,text="Total amount:",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=950)
        if self.triptype=="Round trip":
            self.total=((self.onewayfare+self.rtfare+tax_int+self.tax2_int+fee+class_fee_int),"INR")
        elif self.triptype =="One Way":
             self.total=((self.onewayfare+tax_int+fee+class_fee_int),"INR")
        self.lbl_totalcharge=Label(self.framebs1,text=self.total,font=("glacial indifference",12,"bold"),fg="black",bg="white").place(x=270,y=950)
        
    def return_details(self):
        #====return
        self.lbl_departing=Label(self.framebs1,text="Returning",font=("glacial indifference",17,"bold"),fg="black",bg="white").place(x=10,y=230)
        self.lbl_flight_no=Label(self.framebs1,text=(self.arr_flight_num),font=("glacial indifference",11),fg="black",bg="white").place(x=10,y=260)

        self.lbl_dep_from1=Label(self.framebs1,text=self.arr_from,font=("glacial indifference",14,),fg="black",bg="white").place(x=10,y=300)
        self.lbl_dep_Date1=Label(self.framebs1,text=self.return_date ,font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=325)
        self.lbl_dep_time1=Label(self.framebs1,text=self.arr_time,font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=345)
        self.lbl_arrow=Label(self.framebs1,text="➡️",font=("glacial indifference",25),fg="gray",bg="white").place(x=180,y=310)
        
        self.lbl_arr_from1=Label(self.framebs1,text=self.arr_to,font=("glacial indifference",14),fg="black",bg="white").place(x=270,y=300)
        self.lbl_arr_Date1=Label(self.framebs1,text=self.return_date ,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=325)
        self.lbl_arr_time1=Label(self.framebs1,text=self.arr_time2,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=345)
        
#====return detail label=====
    def return_details2(self):
        self.lbl_regularfare2=Label(self.framebs1,text="Regular Fare -",font=("glacial indifference",12,"bold"),fg="black",bg="white").place(x=10,y=750)
        self.lbl_aee_from1=Label(self.framebs1,text=(self.arr_from+"  To"),font=("glacial indifference",12,"bold"),fg="black",bg="white").place(x=130,y=750)
        self.lbl_arr_to=Label(self.framebs1,text=self.arr_to,font=("glacial indifference",12,"bold"),fg="black",bg="white").place(x=300,y=750)

        self.lbl_airfare2=Label(self.framebs1,text="Airfare charges",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=790)
        self.lbl_2waycharge=Label(self.framebs1,text=(self.rt_tfare2),font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=790)
        self.lbl_feesntaxes2=Label(self.framebs1,text="Fees & Taxes",font=("glacial indifference",12),fg="black",bg="white").place(x=10,y=820)
        tax2=(((self.rtfare*7.5)/100),"INR")
        self.tax2_int=((self.rtfare*7.5)/100)
        self.lbl_2waycharge1=Label(self.framebs1,text=tax2,font=("glacial indifference",12),fg="black",bg="white").place(x=270,y=820)
        self.lbl_class3=Label(self.framebs1,text="*class charges for both flight (oneway & roundtrip) incl.",font=("glacial indifference",12),fg="grey",bg="white").place(x=10,y=990)
        
    def credit_debit_card(self):
        frame11=Frame(self.root4,bg="white",bd=2)
        frame11.place(x=230,y=252,width=800,height=520)
        posters=Image.open(r"cardsaccepted.png")
        posters=posters.resize((900,100), Image.ANTIALIAS)
        self.posters=ImageTk.PhotoImage(posters)
        self.lbl1=Label(frame11,image=self.posters,bd=0)
        self.lbl1.place(x=10, y=20)
        
        self.lbl_payheading=Label(frame11,text="Card Number",font=("glacial indifference",15),fg="black",bg="white")
        self.lbl_payheading.place(x=25,y=160)
        self.cardno_entry1=Entry(frame11,font=("glacial indifference",15),fg="black",bg="white",state="normal")
        self.cardno_entry1.place(x=170,y=160,width=250)
        #====from and To====
        optionse = ['1' ,'2','3','4','5','6','7','8','9','10','11','12']
        optionse1 = ['2021' ,'2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042',
                    '2043','2044','2045','2046','2047','2048','2049','2050','2051','2052','2053','2054','2055','2056','2057','2058','2059','2060']

        
        expiry_month=Label(frame11 ,text="Expiry Month",font=("glacial indifference",15),fg="black",bg="white").place(x=25,y=220)
        self.expiry_month=StringVar()
        self.expiry_month=ttk.Combobox(frame11,font=("glacial indifference",13),state='readonly',justify=CENTER)
        self.expiry_month['values']=(optionse)
        self.expiry_month.place(x=170,y=220,width=250)
        self.expiry_month.set("Expiry Month")
        #self.expiry_month.bind('<<ComboboxSelected>>')
        
        arr_to=Label(frame11 ,text="Expiry Year",font=("glacial indifference",15),fg="black",bg="white").place(x=25,y=280)
        self.expiry_year=ttk.Combobox(frame11,font=("glacial indifference",13),state="readonly",justify=CENTER)
        self.expiry_year['values']=(optionse1)
        self.expiry_year.place(x=170,y=280,width=250)
        self.expiry_year.set("Expiry Year")
        #self.expiry_year.bind('<<ComboboxSelected>>')
        self.lbl_payheading=Label(frame11,text="Full Name",font=("glacial indifference",15),fg="black",bg="white")
        self.lbl_payheading.place(x=25,y=340)
        self.fullname_entry=Entry(frame11,font=("glacial indifference",15),fg="black",bg="white",state="normal")
        self.fullname_entry.place(x=170,y=340,width=250)
        self.lbl_payheading=Label(frame11,text="CVV",font=("glacial indifference",15),fg="black",bg="white")
        self.lbl_payheading.place(x=25,y=400)
        self.cvv_entry=Entry(frame11,font=("glacial indifference",15),fg="black",bg="white",state="normal")
        self.cvv_entry.place(x=170,y=400,width=250)
        self.var_chk=IntVar()
        chk=Checkbutton(frame11,text="I have read and understood all of the fare restrictions. I agree to the Terms And Conditions.",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("glacial indifference",10)).place(x=25,y=460)
        self.paynow_btn_cdc=Button(frame11,text="  Pay now  ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.paynow_cdc)
        self.paynow_btn_cdc.place(x=600,y=460,width=180,height=40)
        
        #if self.var_chk.get()==0:
            #messagebox.showerror("Error","Please Agree with Our Terms and Conditions",parent=self.root4)
    def paynow_cdc(self):
        if (self.cardno_entry1.get()=='' or self.expiry_month.get()=='' or self.expiry_year.get()=='' or self.fullname_entry.get()=='' or self.cvv_entry.get()=='' or self.var_chk.get()==0 or self.expiry_year.get()=='Expiry Year' or self.expiry_month.get()=="Expiry Month"):
            messagebox.showerror("Error","All Fields Are Required, please fill all details",parent=self.root4)
            return
        root6=Tk()
        self.root6=root6
        self.root6.title("otp")
        self.root6.geometry("500x450+350+200")
        self.framecdc=Frame(self.root6,bg="white")
        self.framecdc.place(x=0,y=0,width=500,height=450)
        lbl_otp=Label(self.framecdc,text="OTP",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=200,y=15)
        otpmesg="enter your 6-digit OTP sent on your registered \n phone number for amount:           _          "
        lbl_otpmesg=Label(self.framecdc,text=otpmesg,font=("glacial indifference",15,"bold"),fg="black",bg="white").place(x=25,y=100)
        lbl_otpamt=Label(self.framecdc,text=self.total,font=("glacial indifference",14,"bold"),fg="black",bg="white").place(x=315,y=125)
        self.otp2=IntVar()
        self.otpentry=Entry(self.framecdc,font=("glacial indifference",15),textvariable=self.otp2,fg="black",bg="white",state="normal")
        self.otpentry.place(x=110,y=170,width=250)
        self.submitbtn=Button(self.framecdc,text=" SUBMIT OTP ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.paynow_cdc2)
        self.submitbtn.place(x=150,y=210,width=180,height=40)
    
    def paynow_cdc2(self):
        otp=self.otpentry.get()
        if len(otp)==6:
            self.framecdc.destroy()
            self.framecdc2=Frame(self.root6,bg="white")
            self.framecdc2.place(x=0,y=0,width=500,height=450)
            lbl_bookmesg=Label(self.framecdc2,text="Booked successfully!!!",font=("glacial indifference",20,"bold"),fg="red",bg="white").place(x=100,y=25)
            lbl_bookmesg1=Label(self.framecdc2,text="Congratulations! Your Flight Booking Is Confirmed. ",font=("glacial indifference",15),fg="black",bg="white").place(x=15,y=100)
            lbl_bookmesg2=Label(self.framecdc2,text="Your refrence no./PNR no. :  ",font=("glacial indifference",15),fg="black",bg="white").place(x=15,y=150)
            lbl_bookmesg3=Label(self.framecdc2,text=self.pnr_num,font=("glacial indifference",15,"bold"),fg="black",bg="white").place(x=270,y=150)
            lbl_bookmesg4=Label(self.framecdc2,text="*kindly generate your boarding pass after check in*",font=("glacial indifference",13,"bold"),fg="black",bg="white").place(x=15,y=200)
            self.returnmenu=Button(self.framecdc2,text="Check In ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.cdcfinal)
            self.returnmenu.place(x=130,y=240,width=180,height=40)
        else:
            messagebox.showerror("Error","Invalid otp, Please try again",parent=self.root6)
            self.otpentry.delete(0, END )
    
    def cdcfinal(self):
         self.root6.destroy()
         self.root4.destroy()
         self.checkinbtn()
         
    def upi(self):
        frame12=Frame(self.root4,bg="white",bd=2)
        frame12.place(x=230,y=252,width=800,height=520)
        posters1=Image.open(r"upi.png")
        posters1=posters1.resize((900,100), Image.ANTIALIAS)
        self.posters1=ImageTk.PhotoImage(posters1)
        self.lbl1=Label(frame12,image=self.posters1,bd=0)
        self.lbl1.place(x=10, y=20)
        self.lbl_upiid=Label(frame12,text="Enter your UPI ID",font=("glacial indifference",15),fg="black",bg="white")
        self.lbl_upiid.place(x=25,y=160)
        self.cardno_entry=Entry(frame12,font=("glacial indifference",15),fg="black",bg="white",state="normal")
        self.cardno_entry.place(x=25,y=210,width=250)
        self.verify_btn=Button(frame12,text="Verify",font=("glacial indifference",15,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.upi2)
        self.verify_btn.place(x=25,y=270,width=150,height=40)
        self.paynow_btn=Button(frame12,text="Pay Now",font=("glacial indifference",15,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",state="disabled",command=self.upipaynow)
        self.paynow_btn.place(x=25,y=460,width=150,height=40)
        Pnr_Number1=str(rd.randint(1000000,9999999))+str(rd.choice(string.ascii_letters))+str(rd.choice(string.ascii_letters))+str(rd.randint(10000000000000,99999999999999))+str(rd.choice(string.ascii_letters))
        self.pnr_num1=Pnr_Number1
        lbl_trnum=Label(frame12 ,text="Transaction ID:",font=("glacial indifference",14),fg="black",bg="white").place(x=25,y=350)
        trnum_show=Label(frame12,text=self.pnr_num1,font=("glacial indifference",14),fg="black",bg="white").place(x=160,y=350)
        self.var_chk=IntVar()
        chk=Checkbutton(frame12,text="I have read and understood all of the fare restrictions. I agree to the Terms And Conditions.",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("glacial indifference",11)).place(x=25,y=405)
        
    def upi2(self):
        if self.cardno_entry.get()=='':
            messagebox.showerror("Error","Please Enter Your UPI ID",parent=self.root4)
            return
        root5=Tk()
        self.root5=root5
        self.root5.title("Search Flight")
        self.root5.geometry("500x570+250+200")
        frameup=Frame(self.root5,bg="#E8EEFF")
        frameup.place(x=0,y=0,width=500,height=150)
        frameup=Frame(self.root5,bg="white")
        frameup.place(x=0,y=150,width=500,height=420)
        self.lbl_payinitiated=Label(self.root5,text="Payment Initiated!",font=("glacial indifference",20),fg="black",bg="#E8EEFF")
        self.lbl_payinitiated.place(x=30,y=30)
        self.lbl_payinitiated=Label(self.root5,text="Your payment of is in process.",font=("glacial indifference",13),fg="black",bg="#E8EEFF")
        self.lbl_payinitiated.place(x=30,y=80)
        self.lbl_payinitiated1=Label(self.root5,text="Please find your transaction and booking details below.",font=("glacial indifference",13),fg="black",bg="#E8EEFF")
        self.lbl_payinitiated1.place(x=30,y=100)
        self.lbl_pnr=Label(self.root5,text="PNR/Booking Ref. No:",font=("glacial indifference",13),fg="black",bg="white")
        self.lbl_pnr.place(x=30,y=170)
        self.lbl_pnrno=Label(self.root5,text=self.pnr_num,font=("glacial indifference",15),fg="black",bg="white")
        self.lbl_pnrno.place(x=30,y=200)
        self.lbl_transactionid=Label(self.root5,text="Transaction Id:",font=("glacial indifference",13),fg="black",bg="white")
        self.lbl_transactionid.place(x=30,y=270)
        self.lbl_transaction=Label(self.root5,text=self.pnr_num1,font=("glacial indifference",15),fg="black",bg="white")
        self.lbl_transaction.place(x=30,y=300)
        self.continue_btn=Button(self.root5,text="Continue",font=("glacial indifference",15,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.upifinal)
        self.continue_btn.place(x=160,y=400,width=180,height=40)
        
        
    def upifinal(self):
        self.root5.destroy()
        self.verified=Label(self.root4,text="Status: Verified",font=("glacial indifference",15,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white")
        self.verified.place(x=255,y=524,width=200,height=40)
        self.lbl_upiid.configure(text="Provided UPI ID: ")
        self.cardno_entry.configure(state='disabled')
        self.paynow_btn.configure(state='normal')
        
    def upipaynow(self):
        if self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree with Our Terms and Conditions",parent=self.root4)
            return
        root7=Tk()
        self.root7=root7
        self.root7.title("upi paynow")
        self.root7.geometry("500x450+350+200")
        self.frameupi1=Frame(self.root7,bg="white")
        self.frameupi1.place(x=0,y=0,width=500,height=450)
        lbl_otp=Label(self.frameupi1,text="UPI PIN",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=200,y=15)
        lbl_otpmesg=Label(self.frameupi1,text="Enter your 6-digit UPI pin for amount: ",font=("glacial indifference",13,"bold"),fg="black",bg="white").place(x=15,y=100)
        lbl_otpamt=Label(self.frameupi1,text=self.total,font=("glacial indifference",14,"bold"),fg="black",bg="white").place(x=345,y=100)
        self.upipin=Entry(self.frameupi1,font=("glacial indifference",15),fg="black",bg="white",state="normal")
        self.upipin.place(x=110,y=170,width=250)
        self.proceedbtn=Button(self.frameupi1,text=" PROCEED ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.upifinal2)
        self.proceedbtn.place(x=150,y=210,width=180,height=40)
        
    def upifinal2(self):
        pin=self.upipin.get()
        if len(pin)==6:
            self.frameupi1.destroy()
            self.frameupi2=Frame(self.root7,bg="white")
            self.frameupi2.place(x=0,y=0,width=500,height=450)
            lbl_bookmesg=Label(self.frameupi2,text="Booked successfully!!!",font=("glacial indifference",20,"bold"),fg="red",bg="white").place(x=100,y=25)
            lbl_bookmesg1=Label(self.frameupi2,text="congratulations! Your Flight Booking Is Confirmed. ",font=("glacial indifference",15),fg="black",bg="white").place(x=15,y=100)
            lbl_bookmesg2=Label(self.frameupi2,text="Your refrence no./PNR no. :  ",font=("glacial indifference",15),fg="black",bg="white").place(x=15,y=150)
            lbl_bookmesg3=Label(self.frameupi2,text=self.pnr_num,font=("glacial indifference",15,"bold"),fg="black",bg="white").place(x=270,y=150)
            lbl_bookmesg4=Label(self.frameupi2,text="*kindly generate your boarding pass after check in*",font=("glacial indifference",13,"bold"),fg="black",bg="white").place(x=15,y=200)
            self.returnmenu=Button(self.frameupi2,text="Check In ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.upifinal3)
            self.returnmenu.place(x=130,y=240,width=180,height=40)
        else:
            messagebox.showerror("Error","Invalid otp, Please try again",parent=self.root7)
            self.otpentry.delete(0, END )
    def upifinal3(self):
           self.root4.destroy()
           self.root7.destroy()
           self.checkinbtn()
           
    def netbanking(self):
        frame12=Frame(self.root4,bg="white",bd=2)
        frame12.place(x=230,y=252,width=800,height=520)
        posters1=Image.open(r"netbanking.png")
        posters1=posters1.resize((900,200), Image.ANTIALIAS)
        self.posters1=ImageTk.PhotoImage(posters1)
        self.lbl2=Label(frame12,image=self.posters1,bd=0)
        self.lbl2.place(x=10, y=20)
        self.route=StringVar()
        hdfc=Radiobutton(frame12,text="HDFC", value="HDFC", variable=self.route, font=("glacial indifference", 15),fg="black",bg="white").place(x=25,y=220)
        axis=Radiobutton(frame12,text="Axis",value="Axis", variable=self.route, font=("glacial indifference",15),fg="black",bg="white").place(x=160,y=220)
        icici=Radiobutton(frame12,text="ICICI",value="ICICI", variable=self.route, font=("glacial indifference",15),fg="black",bg="white").place(x=300,y=220)
        sbi=Radiobutton(frame12,text="SBI",value="SBI", variable=self.route, font=("glacial indifference",15),fg="black",bg="white").place(x=470,y=220)
        self.route.set("HDFC")
        self.lbl_info=Label(frame12,text="Few net banking options have been disabled due to a delay in response(s) from the bank(s).",font=("glacial indifference",13),fg="black",bg="white")
        self.lbl_info.place(x=30,y=290)
        chk=Checkbutton(frame12,text="I have read and understood all of the fare restrictions. I agree to the Terms And Conditions.",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("glacial indifference",11)).place(x=25,y=350)
        self.continuebtn=Button(frame12,text="Continue",font=("glacial indifference",15,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.netbanking2)
        self.continuebtn.place(x=25,y=420,width=150,height=40)
        
    def netbanking2(self):
        if self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree with Our Terms and Conditions",parent=self.root4)
            return
        root8=Tk()
        self.root8=root8
        self.root8.title("Net banking")
        self.root8.geometry("500x450+350+200")
        self.framenb1=Frame(self.root8,bg="white")
        self.framenb1.place(x=0,y=0,width=500,height=450)
        lbl_otp=Label(self.framenb1,text="Net Banking",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=150,y=15)
        lbl_otpmesg=Label(self.framenb1,text="Initiating the requested payment for amount:       ",font=("glacial indifference",13,"bold"),fg="black",bg="white").place(x=15,y=100)
        lbl_otpamt=Label(self.framenb1,text=self.total,font=("glacial indifference",13,"bold"),fg="black",bg="white").place(x=170,y=100)
        
        lbl_ocusid=Label(self.framenb1,text="Customer Id ",font=("glacial indifference",15,"bold"),fg="black",bg="white").place(x=15,y=170)
        self.entrybox_id=Entry(self.framenb1,font=("glacial indifference",15),fg="black",bg="white",state="normal")
        self.entrybox_id.place(x=200,y=170,width=200)
        
        lbl_cuspin=Label(self.framenb1,text="Password",font=("glacial indifference",15,"bold"),fg="black",bg="white").place(x=15,y=210)
        self.entrybxx_pass=Entry(self.framenb1,font=("glacial indifference",15),fg="black",bg="white",state="normal")
        self.entrybxx_pass.place(x=200,y=210,width=200)
        
        self.proceedbtn=Button(self.framenb1,text=" PROCEED ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.netbanking21)
        self.proceedbtn.place(x=150,y=280,width=180,height=40)
        
        
    
    def netbanking21(self):
        if self.entrybox_id.get()=="" or self.entrybxx_pass.get()=="":
           messagebox.showerror("Error","Please Agree with Our Terms and Conditions",parent=self.root8)
           return
        root9=Tk()
        self.root9=root9
        self.root9.title("Net banking")
        self.root9.geometry("500x450+350+200")
        self.framenb2=Frame(self.root9,bg="white")
        self.framenb2.place(x=0,y=0,width=500,height=450)
        lbl_otp=Label(self.framenb2,text="Net Banking",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=150,y=15)
        lbl_otp=Label(self.framenb2,text="You Have Successfully Logged In To Your Account.",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=125,y=50)
        lbl_otp=Label(self.framenb2,text=" Payment Initiated.. ",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=125,y=80)
        self.paynowbtn=Button(self.framenb2,text=" Pay now ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.netbankingbooked)
        self.paynowbtn.place(x=150,y=120,width=180,height=40)
       
    def netbankingbooked(self):
        
        self.framenb2.destroy()
        self.framenb3=Frame(self.root9,bg="white")
        self.framenb3.place(x=0,y=0,width=500,height=450)
        lbl_bookmesg=Label(self.framenb3,text="Booked successfully!!!",font=("glacial indifference",20,"bold"),fg="red",bg="white").place(x=100,y=25)
        lbl_bookmesg1=Label(self.framenb3,text="Congratulations! Your Flight Booking Is Confirmed. ",font=("glacial indifference",15),fg="black",bg="white").place(x=15,y=100)
        lbl_bookmesg2=Label(self.framenb3,text="Your refrence no./PNR no. :  ",font=("glacial indifference",15),fg="black",bg="white").place(x=15,y=150)
        lbl_bookmesg3=Label(self.framenb3,text=self.pnr_num,font=("glacial indifference",15,"bold"),fg="black",bg="white").place(x=270,y=150)
        lbl_bookmesg4=Label(self.framenb3,text="*kindly generate your boarding pass after check in*",font=("glacial indifference",13,"bold"),fg="black",bg="white").place(x=15,y=200)
        self.returnmenu=Button(self.framenb3,text=" Check In ",font=("glacial indifference",17),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.netbankingfinal)
        self.returnmenu.place(x=130,y=240,width=180,height=40)
        
    def netbankingfinal(self):
        self.root4.destroy()
        self.root9.destroy()
        self.checkinbtn()
        
    def checkinbtn(self):
        
        root10=Tk()
        self.root10=root10
        self.root10.title("Search Flight")
        self.root10.geometry("1920x1080+0+0")
        
        #======heading poster===
        poster10=Image.open(r"seflight.png")
        poster10=poster10.resize((1920,150), Image.ANTIALIAS)
        self.poster10=ImageTk.PhotoImage(poster10)
        self.lbl1=Label(self.root10,image=self.poster10,bd=0)
        self.lbl1.place(x=0, y=0)
        #===========frame2====
        self.frameckb=Frame(self.root10,bg="white",bd=2)
        self.frameckb.place(x=0,y=250,width=1920,height=1080)
        
        poster15=Image.open(r"seatcheckin.jpeg")
        poster15=poster15.resize((1920,300), Image.ANTIALIAS)
        self.poster15=ImageTk.PhotoImage(poster15)
        self.lbl1=Label(self.root10,image=self.poster15,bd=0)
        self.lbl1.place(x=0,y=130)
        
    
        self.airlineslbl=Label(self.frameckb,text=(self.departing_from, "-",self.departing_to),font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=10,y=200)
        self.triallb2=Label(self.frameckb,text=(self.departure_date,"~",self.departure_time,"~",self.dep_flight_num,"~",self.pnr_num ),font=("glacial indifference",15),fg="black",bg="white").place(x=10,y=230)
        lbl_pnum=Label(self.frameckb,text="Passenger(s)",font=("glacial indifference",20,"bold"),fg="black",bg="white").place(x=650,y=200)
        pass_no=Label(self.frameckb,text=self.passengers,font=("glacial indifference",15,"underline"),fg="black",bg="white").place(x=650,y=230)
        
        self.table3 = ttk.Treeview(self.frameckb)
        style = ttk.Style()
        #pick a theme
        style.theme_use("alt")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('glacial indifference',13),background="white",foreground="white",fieldbackground="white") # Modify the font of the body
        style.configure("Treeview.Heading", font=('glacial indifference', 12),background="#334584",foreground="white") # Modify the font of the headings
        style.map("Treeview", background=[('selected','gray')])
        
        #stripped rows tags
        self.table3.tag_configure('oddrow',background="white")
        self.table3.tag_configure('evenrow',background="white")   #Paleturquoise

        self.table3['columns']=('title','Passenger(s)')
        self.table3.column('#0', width=0, stretch=NO)
        self.table3.column('title', anchor=W, width=100,stretch=NO)
        self.table3.column('Passenger(s)', anchor=W, width=328,stretch=NO)
        self.table3.heading('#0', text='', anchor=W)
        self.table3.heading('Passenger(s)', text='Passenger(s)', anchor=W)
        self.table3.heading('title', text='Title', anchor=W)
        self.table3.place(x=10,y=270,width=430,height=200)
        self.query_database3()

        self.lbl_addseat=Label(self.frameckb,text="Save & add next seat:",font=("glacial indifference",15),fg="black",bg="white")
        self.lbl_addseat.place(x=1100,y=360)
        self.btn_selectseats=Button(self.frameckb,text=("Select Seat for passenger: 1"),cursor="hand2",bd=0,font=('Candara',18),bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.selectseats_btn)
        self.btn_selectseats.place(x=1100,y=400,width=300,height=80)
        self.bttn_clicks2 = 1
        
    def selectseats_btn(self):
        root11=Tk()
        self.root11=root11
        self.root11.title("Select Seat(s)12")
        self.root11.geometry("900x650+300+130")
        self.frameseat=Frame(self.root11,bg="white")
        self.frameseat.place(x=0,y=0,width=900,height=650)
        
        self.frameseatlayout=Frame(self.root11,bg="black")        #seat layout photo to be placed
        self.frameseatlayout.place(x=0,y=0,width=900,height=300)
        self.lbl_seatplan=Label(self.frameseatlayout,text="==================================W I N D O W   S I D E==================================",font=("glacial indifference",14),bg="black",fg="white").place(x=20,y=10)
        self.lbl_seatplan=Label(self.frameseatlayout,text="A ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜",font=("glacial indifference",13),bg="black",fg="white").place(x=20,y=40)
        self.lbl_seatplan=Label(self.frameseatlayout,text="B ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜",font=("glacial indifference",13),bg="black",fg="white").place(x=20,y=70)
        self.lbl_seatplan=Label(self.frameseatlayout,text="C ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜" ,font=("glacial indifference",13),bg="black",fg="white").place(x=20,y=100)
        self.lbl_seatplan=Label(self.frameseatlayout,text="   1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30",font=("glacial indifference",14),bg="black",fg="white").place(x=20,y=140)
        self.lbl_seatplan=Label(self.frameseatlayout,text="D ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜",font=("glacial indifference",13),bg="black",fg="white").place(x=20,y=180)
        self.lbl_seatplan=Label(self.frameseatlayout,text="E ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜",font=("glacial indifference",13),bg="black",fg="white").place(x=20,y=210)
        self.lbl_seatplan=Label(self.frameseatlayout,text="F ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜",font=("glacial indifference",13),bg="black",fg="white").place(x=20,y=240)
        self.lbl_seatplan=Label(self.frameseatlayout,text="==================================W I N D O W   S I D E==================================",font=("glacial indifference",14),bg="black",fg="white").place(x=20,y=270)

 

        lbl_pass=Label(self.frameseat,text="Choose Your seat: ",font=("glacial indifference",25,"bold"),fg="black",bg="white").place(x=30,y=325)
        lbl_pass=Label(self.frameseat,text="Select seat Row",font=("glacial indifference",20),fg="black",bg="white").place(x=30,y=380)
        self.seatrow=StringVar()
        self.seatrow=ttk.Combobox(self.frameseat,font=("glacial indifference",15),state='readonly',justify=CENTER)
        self.seatrow['values']=('A','B','C','D','E','F')
        self.seatrow.place(x=35,y=420,width=180)
        self.seatrow.set("Select row")
        self.seatrow.bind('<<ComboboxSelected>>')
        
        lbl_pass=Label(self.frameseat,text="Select seat column",font=("glacial indifference",20),fg="black",bg="white").place(x=560,y=380)
        self.seatcolumn=StringVar()
        self.seatcolumn=ttk.Combobox(self.frameseat,font=("glacial indifference",15),state='readonly',justify=CENTER)
        self.seatcolumn['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
        self.seatcolumn.place(x=565,y=420,width=180)
        self.seatcolumn.set("Select column")
        self.seatcolumn.bind('<<ComboboxSelected>>')
        
        self.selectseatbtn=Button(self.frameseat,text="Select Seat ",font=("glacial indifference",20,),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",command=self.addseatdetails)
        self.selectseatbtn.place(x=380,y=520,width=200,height=50)

    def addseatdetails(self):
        try:
            if self.seatrow.get()=="Select row" or self.seatcolumn.get()=="Select column":
                messagebox.showerror("Error","All Fields Are Required, please fill all details",parent=self.root11)
                return
            else:
                self.addseatdetails_db()
                self.root11.destroy()
                self.bttn_clicks2 += 1
                self.btn_selectseats['text'] = "Select Seat for passenger: " + str(self.bttn_clicks2)
                
                if self.bttn_clicks2 > self.passengers:
                    self.btn_selectseats.destroy()
                    self.lbl_addseat.configure(text="Passenger seats added")
                    self.continue_btnseat=Button(self.frameckb,text="Generate boarding pass",font=("glacial indifference",15,"bold"),bd=0,bg="#334584",fg="white",activebackground="#334584",activeforeground="white",cursor="hand2",command=self.gen_boardingpass).place(x=1100,y=400,width=300,height=80)
                    messagebox.showinfo("Success","Passenger seat Added Successfully, you may generate boarding pass now",parent=self.root10)
        except Exception as es:
                messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root10)

    def addseatdetails_db(self):
        self.pass_seat=self.seatrow.get()+self.seatcolumn.get()
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="airlines")
        cur=con.cursor()
        cur.execute("insert into seat_details (PNR_no,Passenger_no,seat) values(%s,%s,%s)",(self.pnr_num,self.bttn_clicks2,self.pass_seat))
        con.commit()
        con.close()
        messagebox.showinfo("Success","Passenger seat Added Successfully",parent=self.root11)
        
    def gen_boardingpass(self):
        self.root10.destroy()
        root12=Tk()
        self.root12=root12
        self.root12.title("Generate boarding pass")
        self.root12.geometry("1920x1080+0+0")
        self.boarding_pass=Frame(self.root12,bg="#E8EEFF")
        self.boarding_pass.place(x=0,y=0,width=1920,height=1080)
        
        #======heading poster===
        poster30=Image.open(r"seflight.png")
        poster30=poster30.resize((1920,150), Image.ANTIALIAS)
        self.poster30=ImageTk.PhotoImage(poster30)
        self.lbl1=Label(self.root12,image=self.poster30,bd=0)
        self.lbl1.place(x=0,y=0)
        
        self.lbl_bp_heading=Label(self.boarding_pass,text="Your Boarding Pass",font=("glacial indifference",20,"bold"),fg="black",bg="#E8EEFF")
        self.lbl_bp_heading.place(x=50,y=160)
        self.lbl_bp_heading1=Label(self.boarding_pass,text="Please carry a printed copy of your health declaration",font=("glacial indifference",10),fg="grey",bg="#E8EEFF")
        self.lbl_bp_heading1.place(x=50,y=200)
        self.lbl_bp_heading2=Label(self.boarding_pass,text="form & boarding pass before reaching the airport.",font=("glacial indifference",10),fg="grey",bg="#E8EEFF")
        self.lbl_bp_heading2.place(x=50,y=220)
        
        posterbp=Image.open(r"Boardingpass.png")
        posterbp=posterbp.resize((1350,480), Image.ANTIALIAS)
        self.posterbp=ImageTk.PhotoImage(posterbp)
        self.lbl1=Label(self.root12,image=self.posterbp,bd=0)
        self.lbl1.place(x=120, y=280)
        #fetch passenger name % email adress for boarding pass
        con=pymysql.connect(host="localhost",user="root",password="pranil123",database="airlines")
        cur=con.cursor()
        cur.execute("select Passenger_Name from pass_details where PNR_no=%s",self.pnr_num)
        myresult=cur.fetchone()
        for row in myresult:
            self.nameofpass=row
        cur.execute("select email_id from pass_details where PNR_no=%s",self.pnr_num)
        myresult2=cur.fetchone()
        for row in myresult2:
            self.emailofpass=row
        con.commit()
        con.close()
        
        self.xnamelbl=Label(self.root12,text=self.nameofpass,bg="white",font=("glacial indifference",20)).place(x=390,y=445)
        self.xnamelbl1=Label(self.root12,text=self.nameofpass,bg="white",fg="black",font=("glacial indifference",20)).place(x=1120 ,y=435)
        self.boardfrom=Label(self.root12,text=self.dep_cmb,font=("glacial indifference",20),bd=0,bg="white")
        self.boardfrom.place(x=390,y=545)
        self.boardfrom1=Label(self.root12,text=self.dep_cmb,font=("glacial indifference",15),bd=0,bg="white")
        self.boardfrom1.place(x=1210,y=483)
        self.boardto=Label(self.root12,text=self.arr_cmb,font=("glacial indifference",20),bd=0,bg="white")
        self.boardto.place(x=390,y=650)
        self.boardto1=Label(self.root12,text=self.arr_cmb,font=("glacial indifference",15),bd=0,bg="white")
        self.boardto1.place(x=1210,y=525)
        self.boardtime=Label(self.root12,text=self.departure_time,font=("glacial indifference",20),bd=0,bg="white")
        self.boardtime.place(x=920,y=445)
        self.boarddate=Label(self.root12,text=self.departure_date,font=("glacial indifference",20),bd=0,bg="white")
        self.boarddate.place(x=705,y=445)
        self.boarddate1=Label(self.root12,text=self.departure_date,font=("glacial indifference",15),bd=0,bg="white")
        self.boarddate1.place(x=1210,y=652)
        self.boardflight=Label(self.root12,text=self.dep_flight_num_int,font=("glacial indifference",20),bd=0,bg="white")
        self.boardflight.place(x=705,y=545)
        self.boardflight1=Label(self.root12,text=self.dep_flight_num_int,font=("glacial indifference",15),bd=0,bg="white")
        self.boardflight1.place(x=1210,y=610)
        self.boardseat=Label(self.root12,text=self.pass_seat,font=("glacial indifference",20),bd=0,bg="white")
        self.boardseat.place(x=920,y=545)        
        self.boardseat1=Label(self.root12,text=self.pass_seat,font=("glacial indifference",15),bd=0,bg="white")
        self.boardseat1.place(x=1210,y=697)
        self.lblpnrnum=Label(self.root12,text=self.pnr_num,font=("glacial indifference",15),bd=0,bg="white")
        self.lblpnrnum.place(x=1210,y=570)
        self.lblgateno=Label(self.root12,text=(rd.randint(0,20)),font=("glacial indifference",20),bd=0,bg="white")
        self.lblgateno.place(x=705,y=650)
        self.lblboardingtill=Label(self.root12,text="30 Min ago",font=("glacial indifference",20),bd=0,bg="white")
        self.lblboardingtill.place(x=920,y=650)

        self.lblbnotice1=Label(self.root12,text="THANKS FOR BOOKING YOUR FLIGHT WITH AVIATION INDIA",font=("glacial indifference",20,"bold"),bd=0,fg="black",bg="#E8EEFF")
        self.lblbnotice1.place(x=695,y=160)
        self.lblbnotice2=Label(self.root12,text=("A copy of boarding pass in the above format with "),font=("glacial indifference",12),bd=0,fg="grey",bg="#E8EEFF")
        self.lblbnotice2.place(x=695,y=190)
        self.lblbnotice3=Label(self.root12,text=("the required passenger details will be mailed to you on "+ self.emailofpass),font=("glacial indifference",12),bd=0,fg="grey",bg="#E8EEFF")
        self.lblbnotice3.place(x=695,y=210)

root=Tk()
obj=main_menu_window(root)
root.mainloop()