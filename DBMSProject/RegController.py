from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from .import pool


@xframe_options_exempt
def RegistrationInterface(request):
    return render(request, "Registration.html")

@xframe_options_exempt
def submitregistration(request):



    try:

        distributorname = request.POST['distributorname']
        distributormobno=request.POST['distributormobno']
        city = request.POST['city']
        state=request.POST['state']

        db,cmd=pool.connection()
        q="insert into distributor (name,mobilenumber,city,state)values ('{0}','{1}','{2}','{3}')".format(distributorname,distributormobno,city,state)
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request,"Registration.html",{'msg':"Record Submitted"})
    except Exception as e:

        print(e)
        return render(request, "Registration.html", {'msg': "Server Error"})

@xframe_options_exempt
def Listallregistrations(request):

    db,cmd=pool.connection()
    q="select * from distributor"
    cmd.execute(q)
    rows=cmd.fetchall()
    return render(request,"allregistration.html",{"data":rows})
def ProductInterface(request):
    return render(request, "Registration.html")
def submitproducts(request):



    try:

        distributorname = request.POST['distributorname']
        distributormobno=request.POST['distributormobno']
        city = request.POST['city']
        state=request.POST['state']

        db,cmd=pool.connection()
        q="insert into distributor (name,mobilenumber,city,state)values ('{0}','{1}','{2}','{3}')".format(distributorname,distributormobno,city,state)
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request,"Registration.html",{'msg':"Record Submitted"})
    except Exception as e:

        print(e)
        return render(request, "Registration.html", {'msg': "Server Error"})
def Listallproducts(request):

    db,cmd=pool.connection()
    q="select * from "
    cmd.execute(q)
    rows=cmd.fetchall()
    return render(request,"allregistration.html",{"data":rows})
