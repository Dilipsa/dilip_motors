from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee_detail
from .forms import Employee_detailForm
from django.utils import timezone

def employee_list(request):
    detail=Employee_detail.objects.all()
    return render(request,'employee/employee_list.html',{'detail':detail})

def employee_detail(request, pk):
    emp_detail=get_object_or_404(Employee_detail, pk=pk)
    return render(request,'employee/employee_detail.html',{'emp_detail':emp_detail})

def employee_new(request):
    # form=Employee_detailForm()
    # return render(request, 'employee/employee_create.html',{'form':form})
    if request.method=="POST":
        form=Employee_detailForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.joined=timezone.now
            post.save()
            return redirect('Employee_detail', pk=post.pk)
    else:
        post=Employee_detailForm()
    return render(request, 'employee/employee_create.html',{'post':post})
