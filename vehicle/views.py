from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm

def car_list(request):
    list=Car.objects.all()
    return render(request, 'vehicle/car_list.html',{'list': list})

def car_detail(request, pk):
    detail=get_object_or_404(Car, pk=pk)
    return render(request, 'vehicle/car_detail.html', {'detail': detail})

def car_new(request):
    # form = CarForm()
    # return render(request, 'vehicle/car_new.html', { 'form': form})
    if request.method=="POST":
        form =CarForm(request.POST)
        detail=form.save(commit=False)
        detail.save()
        return redirect('car_detail', pk=detail.pk)
    else:
        form=CarForm()
    return render(request,'vehicle/car_new.html', {'form':form})

def car_edit(request ,pk):
    post=get_object_or_404(Car, pk=pk)
    if request.method=="POST":
        form = CarForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('car_detail', pk=post.pk)
    else:
        form=CarForm(instance=post)
    return render(request, 'vehicle/car_new.html', {'form':form})
