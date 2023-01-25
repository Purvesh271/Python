import os
import platform

import mysql .connector
import pandas as pd

mydb = mysql.connector .connect (host='localhost',user='root',passwd='1234',database='service')


print("----------WELCOME TO INSTANT MESSAGING APP------------") 

'''def create_table():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE service")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE ims (msg_id VARCHAR(10),rnameVARCHAR (30), sname VARCHAR(30),rmail VARCHAR(50),smail VARCHAR (50) ,msg VARCHAR (250) )")
        print ("Table Created")
    except:
        print ("Databse or Table Already Created")'''

 

def add_msg():
    mycursor=mydb. cursor ()
    msg_id=input ("Enter Message ID: ")
    rname=input ("Enter the Name of Receiver: ")
    sname=input ("Enter the Name of Sender: ")
    rmail=input ("Enter Receiver E-mail : ")
    smail=input ("Enter the Sender E-mail : ")
    msg=input ("Enter the Message : ")
    sql=("INSERT INTO ims (msg_id,rname, sname, rmail, smail,msg) VALUES(%s,%s,%s,%s,%s,%s)")
    val=(msg_id, rname, sname, rmail, smail,msg)
    mycursor.execute (sql, val)
    mydb.commit ()
    print (mycursor.rowcount, "Record inserted.")
    c=input('do you want to continue (y/[n]:)')
    if c =='y':
        Main_Menu()
    else:
        print("Program going to Exit")
        exit("\n! Thanks")



def search_msg():
    mycursor=mydb. cursor ()
    print ("Search the message using ")
    print ("1. Message ID ")
    print ("2. Search the Name of Receiver ")
    print ("3. All Details")
    ch=int (input ("Enter the choice : "))
    if (ch==1):
        s=input ("Enter Message ID : ")
        mycursor.execute ("SELECT * FROM ims")
        myresult = mycursor.fetchall()
        for x in myresult:
            if(x[0]==s):
                print(x)
        if (myresult):
            print ("No More Record Found for ID: ",s)
        c=input('do you want to continue (y/[n]:)')
        if c =='y' :
            Main_Menu()
        else:
            print("Program going to Exit")
            exit("\n! Thanks")
    elif(ch==2):
        s=input ("Enter Sender Name : ")
        mycursor.execute("SELECT * FROM ims")
        myresult = mycursor.fetchall()
        for x in myresult:
            if(x[2]==s):
                print(x)
        if(myresult):
            print("No More Record Found For The Sender Name:",s)
        c=input('do you want to continue (y/[n]:)')
        if c =='y' :
            Main_Menu()
        else:
            print("Program going to Exit")
            exit("\n! Thanks")
    elif(ch==3):
        mycursor.execute("SELECT * FROM ims")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        if(myresult):
            print("No More Record Found !!")
        c=input('do you want to continue (y/[n]:)')
        if c =='y' :
            Main_Menu()
        else:
            print("Program going to Exit")
            exit("\n! Thanks")
def delete_msg():
    mycursor = mydb.cursor()
    ms=input("Enter the Message ID to be deleted (in apostrophe): ")
    sql = "DELETE FROM ims WHERE msg_id = %s"%ms
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted")
    c=input('do you want to continue (y/[n]:)')
    if c =='y' :
        Main_Menu()
    else:
        print("Program going to Exit")
        exit("\n! Thanks")
def Main_Menu():
    print("ENTER 1 :TO ADD NEW MESSAGE")
    print("ENTER 2 :TO SEARCH MESSAGE")
    print("ENTER 3 :TO DELETE MESSAGE")
    print("ENTER 4 :TO EXIT")
    try:
        userInput = int(input("Please select  an above option: "))
        if (userInput==1):
            print("\n")
            add_msg()
        elif(userInput==2):
            search_msg()
        elif(userInput==3):
            delete_msg()
        else:
            
            print("Program going to Exit")

            exit("\n! Thanks")
    except():
        print("Something Wrong in Code")
Main_Menu()
#create_table()
        
        

            
