# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 12:24:11 2021

@author: 20man
"""

#creating main database
import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                                   password="pranil123",)
mycursor = mydb.cursor()
mycursor.execute("create database airlines")


#login info table
import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                                   password="pranil123",\
                                       database="airlines")
mycursor = mydb.cursor()
mycursor.execute("create table user_info(id int(11) primary key,fname char(50),lname char(40),contact char(50),email char(50),question char(50),answer char(50),password char(50))")

#passenger details table
import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                                   password="pranil123",\
                                       database="airlines")
mycursor = mydb.cursor()
mycursor.execute("create table pass_details(PNR_no char(20),title char(10),Passenger_Name char(50),Phone_no char(10),email_id char(30))")


#seat details table
import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                                   password="pranil123",\
                                       database="airlines")
mycursor = mydb.cursor()
mycursor.execute("create table seat_details(PNR_no char(20),passenger_no char(10),seat char(50))")


#databse table
import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                                   password="pranil123",\
                                       database="airlines")
mycursor = mydb.cursor()
mycursor.execute("create table onewayflight(Srno char(4),Flight_Number char(20),Days_Of_Operation char(50),origin char(50),Destination char(50),Departure char(50),Arrival char(50),Aircraft_Carrier char(50),Fare char(50))")