#from django.shortcuts import render
import os
import json
#Email Imports 
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from . import models

def index(request):
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    return render(request,"index.html",{})
    #return HttpResponse("<h1>This is my first page</h1>")

def reg(request):
    return render(request,'reg.html',{})

def home(request):
    return render(request,'index.html',{})

def storedata(request):
    name = request.POST.get('sname')
    fname = request.POST.get('fname')
    fmobile = request.POST.get('fmobile')
    occupation = request.POST.get('occupation')
    dob = request.POST.get('dob')
    mobile = request.POST.get('mobile')
    wmobile = request.POST.get('wmobile')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    qualification = request.POST.get('qualification')
    address = request.POST.get('address')
    district = request.POST.get('district')
    #models.store_data(name,fname,fmobile,occupation,dob,mobile,wmobile,email,gender,qualification,address,district)
    
    #print(name,fname,fmobile,occupation,dob,mobile,wmobile,email,gender,qualification,address,district)
    return HttpResponse("<h2><a href='../home'>back</a>Successfully Stored</h2>")
    #return render(request,'index.html',{})

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        #print(template_file_content)
    return Template(template_file_content)

def email(mailid,name,subject1):
    try:
        message_template = read_template('MailTemplate.txt')
        # set up the SMTP server
        #   s = smtplib.SMTP(host='smtp.gmail.com', port='587')
        s.starttls()
        s.login('privatejobsofindia@gmail.com','bgt54rfv')
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=name.title())
        msg['From']='privatejobsofindia@gmail.com'
        msg['To']=mailid
        msg['Subject']=subject1
        msg.attach(MIMEText(message, 'plain'))
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        # Terminate the SMTP session and close the connection
        s.quit()
    except Exception as e:
        print(e)
        
#email('s4rcva@gmail.com','siva')
    
def send_mail(request):
    subject1 = request.POST.get('subject')
    message = request.POST.get('message')
    heading = "Dear $PERSON_NAME,\n       "+message
    file_access = open('MailTemplate.txt','w')
    file_access.write(heading)
    file_access.close()
    get_emails = models.getmails()
    if(get_emails==0):
        return HttpResponse("<h2><a href='../home'>back</a>No mails Exist</h2>")
    else:
        for name in get_emails.keys():
            email(get_emails[name],name,subject1)
        return HttpResponse("<h2><a href='../notification'>back</a>Email sent</h2>")

#method for staff login
def stafflogin(request):
    uname = request.POST.get('uname')
    psw = request.POST.get('psw')
    if(uname=='admin' and psw=='admin'):
        return render(request,'notification.html',{})
    else:
        #print(uname,psw)
        return HttpResponse("<h2>failed</h2>")

#method for notificationnupdate
def update_notifications(request):
    notification = request.POST.get('notification')
    #print(notification)
    models.save_notification(notification)
    return HttpResponse("<h2><a href='../notification'>back</a>Notification Updated</h2>")
def notification(request):
    return render(request,'notification.html',{})

def get_notifications(request):
    data = models.get_notification_data()
    if(data=='{}'):
        message= json.dumps(data)
        return HttpResponse(message,content_type="application/json")
    else:
        dict_data ={}
        i = 0
        for row in data:
            dict_data[i] = row[0]
            i = i+1
        message= json.dumps(dict_data)
        return HttpResponse(message,content_type="application/json")