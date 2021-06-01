from django.shortcuts import render
from .import pool
from django.contrib import auth
def AdminLogin(request):
    return render(request,'adminlogin.html',{'msg':''})
def admindashboard(request):
    return render(request,'admindashboard.html',{'msg':''})
def adminchklogin(request):
    adminemail=request.POST['adminemail']
    password=request.POST['password']
    query="select * from adminlogin where adminemailid='{0}' and password='{1}'".format(adminemail,password)
    db, cmd = pool.connection()
    cmd.execute(query)
    row=cmd.fetchone()
    if (row):

        return render(request, "admindashboard.html", {'row': row})
    else:
        return render(request, "adminlogin.html", {"msg": "Invalid  ID/Password"})


def AdminLogout(request):
    auth.logout(request)
    return render(request, "adminlogin.html", {'msg': ''})
