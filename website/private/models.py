from django.db import models
import sqlite3
import datetime

'''class Students_data(models.Model):
    sid = models.PositiveIntegerField(primary_key = True)
    sname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    wmobile = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=4)
    qualification = models.CharField(max_length=40)
    address = models.TextField()
    district = models.CharField(max_length = 20)'''
  
def table_exists(conn,table_name):
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+table_name+"'")
    result_data = result.fetchall()
    if len(result_data)>0 and result_data[0][0] == table_name:
        return True
    else: 
        return False

def store_data(name,fname,fmobile,occupation,dob,mobile,wmobile,email,gender,qualification,address,district):
    conn = sqlite3.connect('db.sqlite3')
    if(table_exists(conn,'students_data')):
        student_details = (name,fname,fmobile,occupation,dob,mobile,wmobile,email,gender,qualification,address,district)
        query = '''insert into students_data(name,fname,fmobile,occupation,dob,mobile,wmobile,email,gender,qualification,address,district)values(?,?,?,?,?,?,?,?,?,?,?,?)'''
        conn.execute(query,student_details)
        conn.commit()
    else:
        student_details = (1,name,fname,fmobile,occupation,dob,mobile,wmobile,email,gender,qualification,address,district)
        conn.execute('create table students_data (sid INTEGER PRIMARY KEY AUTOINCREMENT,name char(30),fname char(30),fmobile char(15),occupation char(30),dob char(15),mobile char(15),wmobile char(15),email char(30),gender char(5),qualification char(30),address text(150),district char(20))')
        query = '''insert into students_data(sid,name,fname,fmobile,occupation,dob,mobile,wmobile,email,gender,qualification,address,district)values(?,?,?,?,?,?,?,?,?,?,?,?)'''
        conn.execute(query,student_details)
        conn.commit()
    conn.close()
        
def getmails():
    conn = sqlite3.connect('db.sqlite3')
    if(table_exists(conn,'students_data')):
        cursor = conn.cursor()
        cursor.execute('select name,email from students_data')
        data = cursor.fetchall()
        li_email = {}
        for row in data:
            li_email[row[0]] = row[1]
        conn.close()
        return li_email
        #print(li_email)
    else:
        return 0

def save_notification(notification):
    #print(notification)
    conn = sqlite3.connect('db.sqlite3')
    if(table_exists(conn,'notifications')):
        details = (str(datetime.datetime.now()),notification)
        query = '''insert into notifications(date,notification)values(?,?)'''
        conn.execute(query,details)
        conn.commit()
    else:
        details = (1,str(datetime.datetime.now()),notification)
        conn.execute('create table notifications (nid INTEGER PRIMARY KEY AUTOINCREMENT,date char(30),notification text)')
        query = '''insert into notifications(nid,date,notification)values(?,?,?)'''
        conn.execute(query,details)
        conn.commit()
    conn.close()

def get_notification_data():
    conn = sqlite3.connect('db.sqlite3')
    if(table_exists(conn,'notifications')):
        cursor = conn.cursor()
        cursor.execute('select notification from notifications')
        result = cursor.fetchall()
        return result
    else:
        return '{}'