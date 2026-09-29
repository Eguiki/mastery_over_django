from mastery_over_django.models import Mastery
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect, aget_object_or_404, get_object_or_404

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

def mastery(request, mastery_id):
    mastery = get_object_or_404(Mastery, pk=mastery_id)
    context = {'mastery': mastery}
    return render(request, 'mastery.html', context)


def edit_mastery(request,mastery_id):
    mastery = get_object_or_404(Mastery, pk=mastery_id)
    form = forms.MasteryForm(instance=mastery)
    if request.method == 'POST':
        form = forms.MasteryForm(request.POST, instance=mastery)
        if form.is_valid():
            form.save()
            return redirect('masteries')
        return render(request, 'masteries.html')
    context = {'form': form, 'id':mastery_id}
    return render(request, 'edit_mastery.html', context)

def delete_mastery(request, mastery_id):
    mastery = get_object_or_404(Mastery, pk=mastery_id)
    mastery.delete()
    return redirect('masteries')