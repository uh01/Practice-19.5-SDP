# album/forms.py
from django import forms
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        exclude = ['author']
        # fields = '__all__'