from django.shortcuts import render
from app.models import Employees

def home(req):
    emps = Employees.objects.all()
    context = {
        'employees':emps
    }
    # return HttpResponse("Hey hi")
    return render(req,'home.html',context)