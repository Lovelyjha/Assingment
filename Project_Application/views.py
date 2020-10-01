from django.shortcuts import render, redirect
from Project_Application.models import Manager
from Project_Application.forms import ManagerForm
# Create your views here.

def retrive_view(request):
    managers=Manager.objects.all()
    return render(request,'Project_Application/index.html',{'managers':managers})


def create_view(request):
    form=ManagerForm()
    if request.method=='POST':
        form=ManagerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/retrive')
    return render(request,'Project_Application/create.html',{'form':form})

def delete_view(request,id):
    manager=Manager.objects.get(id=id)
    manager.delete()
    return redirect('/retrive')

def update_view(request,id):
    manager=Manager.objects.get(id=id)
    if request.method=='POST':
        form=ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
        return redirect('/retrive')        
    return render(request,'Project_Application/update.html',{'manager':manager})