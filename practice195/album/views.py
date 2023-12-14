# album/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView

@login_required
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_instance = album_form.save(commit=False)
            album_instance.author = request.user
            album_instance.save()
            return redirect('music_album')
    else:
        album_form = forms.AlbumForm()

    return render(request, 'album/add_album.html', {'form': album_form})


@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def edit_album(request, id_no):
    album = models.AlbumModel.objects.get(pk=id_no)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('music_album')

    return render(request, 'album/add_album.html', {'form': album_form})


@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album/add_album.html'
    pk_url_kwarg = 'id_no'
    success_url = reverse_lazy('music_album')


@login_required
def detete_entry(request, id_no):
    try:
        album = models.AlbumModel.objects.get(pk=id_no)
        album.delete()
        return redirect("music_album")
    except models.Album.DoesNotExist:
        return render(request, 'album/add_album_not_found.html', {'id_no': id_no})
    

@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.AlbumModel
    template_name = 'album/delete.html'
    success_url = reverse_lazy('music_album')
    pk_url_kwarg = 'id_no'