from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
     template=loader.get_template('index.html')
     template=loader.get_template('index.html')
     return HttpResponse(template.render())

     #import mysql.connector
    # mydb = mysql.connector.connect(
     #host="localhost",
     #user="root",
     #password="",
     #database="mabase")
     
    # mycursor = mydb.cursor()
    
     #mycursor.execute("select * from customers")
     #liste=[]
     #myresult = mycursor.fetchall()
     #for x in myresult:
      #    liste.append(x)
     #return HttpResponse(" 44 hamdolilah welcome " + str(liste) )

    