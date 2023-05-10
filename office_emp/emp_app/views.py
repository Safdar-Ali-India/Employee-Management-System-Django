from django.shortcuts import render, HttpResponse
from .models import Employee,Title,Department
from datetime import datetime
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request, 'index.html')
def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'all_emp.html',context)
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        phone_number = int(request.POST['phone_number'])
        department = int(request.POST['department'])
        # email = request.POST['email']
        print("request.POST['first_name']---------->",request.POST['first_name'])
        print("request.POST['department']---------->",request.POST['department'])
        print("request.POST['job_title']---------->",request.POST['job_title'])
        job_title = int(request.POST['job_title'])
        title=Title.objects.get(id=job_title)
        dept=Department.objects.get(id=department)
        # print("job_title,type(job_title)------------------>",job_title,type(job_title))
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, phone_number=phone_number, department=dept, job_title=title, hire_date=datetime.now())
        new_emp.save()
        return render(request, 'success.html', {'message': 'Employee added Successfully'})
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occurred! Employee has not been added")





    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     salary = int(request.POST['salary'])
    #     phone_number = int(request.POST['phone_number'])
    #     department = int(request.POST['department'])
    #     # email = request.POST['email']
    #     job_title = int(request.POST['job_title'])
    #     new_emp =Employee(first_name = first_name, last_name= last_name, salary=salary,phone_number=phone_number,department_id=department, job_title=job_title,hire_date=datetime())
    #     new_emp.save()
    #     return render('Employee added Successfully')
    # elif request.method == 'GET':
    #     return render(request, 'add_emp.html')
    # else:
    #     return HttpResponse("An Exception Occured ! Employee has not been added")
def remove_emp(request, emp_id=0):
    if emp_id:
        print("emp_id===>",emp_id)
        try:
            emp_to_removed = Employee.objects.get(id=emp_id)
            emp_to_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter a Valid Emp id")
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request, 'remove_emp.html',context)
def filter_emp(request):
    return render(request, 'filter_emp.html')