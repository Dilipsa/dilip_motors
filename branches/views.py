from django.shortcuts import render
from .models import Branch

def branch_detail(request):
    branch_det=Branch.objects.all()
    return render(request, 'branches/branch_list.html', {'branch_det':branch_det})
