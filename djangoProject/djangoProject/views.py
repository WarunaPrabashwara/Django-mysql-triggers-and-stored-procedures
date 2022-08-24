from django.shortcuts import render 
from django.db import connection
from djangoProject.models  import getempdetails

def showdetails(request) :
    cursor = connection.cursor()
    # cursor.callproc( 'GetEmployeeRecordsSP')
    cursor.execute( "call GetEmployeeRecordsSP()" )
    results = cursor.fetchall()
    return render(request , 'index.html' ,  {'getempdetails' :  results }) 

def page2funct(request):    
    return render(request , 'page2.html'  )