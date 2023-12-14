from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

@login_required
def add_musician(request):
    musician_form = forms.MusicianForm()
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
        else:
            musician_form = forms.MusicianForm()
    return render(request, 'musician/add_musician.html', {'form1': musician_form})


@login_required
def edit_musician(request, id_no):
    musician = models.MusicianModel.objects.get(pk=id_no)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.instance.author = request.user
            musician_form.save()
            return redirect('music_album')

    return render(request, 'musician/add_musician.html', {'form1': musician_form})
