from django.shortcuts import render,redirect
from .models import Trainer
from app_TrainerForm import forms
# Create your views here.


def retrieve_trainer(request):
    trainers = Trainer.objects.all()
    return render(request,'TrainerForm_app/trainer_list.html',{'trainer':trainers})

def create_trainer(request):
    form = forms.TrainerForms()
    if request.method == 'POST':
        form = forms.TrainerForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'TrainerForm_app/create_employee.html',{'form':form})

def trainer_delete(request,id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect('/')

def trainer_update(request,id):
    trainer = Trainer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.TrainerForms(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'TrainerForm_app/update_trainer.html',{'trainer':trainer})