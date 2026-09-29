from mastery_over_django.models import Mastery
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect

from mastery_over_django import forms


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def masteries(request):
    masteries = Mastery.objects.all()
    context = {'masteries': masteries}
    return render(request, 'masteries.html', context)

def insert_mastery(request):
    if request.method == 'POST':
        form = forms.MasteryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('masteries')
    context = {'form': forms.MasteryForm}
    return render(request, 'insert_mastery.html',context)
