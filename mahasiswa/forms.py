from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.Form):
    
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    nim = forms.CharField(max_length=10)
    nama = forms.CharField(max_length=100)
    prodi = forms.CharField(max_length=100)
    semester = forms.IntegerField()

    class Meta:
        model = Mahasiswa