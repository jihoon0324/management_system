from django.shortcuts import render

from staff.form import StaffForm
from staff.models import Staff
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'staff/index.html', {
        'staff': Staff.objects.all()

    })

def add(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():

            form.save()
            return render(request, 'staff/add.html', {
                'form': StaffForm(),
                'success': True
            })

    else:
        form = StaffForm()

    return render(request, 'staff/add.html', {
        'form': StaffForm()
    })


def edit(reqeust, id):
    if reqeust.method == 'POST':
        staff_memeber = Staff.objects.get(pk=id)
        form = StaffForm(reqeust.POST, instance=staff_memeber)
        if form.is_valid():
            form.save()
            return render(reqeust, 'staff/edit.html', {
                'form': form,
                'success': True,
            })
    else:
        staff_memeber =Staff.objects.get(pk=id)
        form = StaffForm(instance=staff_memeber)
    return render(reqeust,'staff/edit.html',{
        'form':form
    })

def delete(request , id):
    if request.method =="POST":
        staff = Staff.objects.get(pk=id)
        staff.delete()
    return HttpResponseRedirect(reverse('index'))