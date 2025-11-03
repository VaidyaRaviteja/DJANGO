from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Employees


def employee_details(request,pk):
    # try:
    #     employee = Employees.objects.get(pk=pk)
    #     print(employee)
    # except:
    #     raise Http404
    employee = get_object_or_404(Employees,pk=pk)
    # print(employee)
    context = {
        'employee':employee,
    }
    return render(request,'employee_details.html',context)