from django import forms
from .models import Buku
class BukuForm(forms.Form):

    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    nama = forms.CharField(max_length=100)
    pengarang = forms.CharField(max_length=100)
    penerbit = forms.CharField(max_length=100)
    thn_terbit = forms.CharField(max_length=5)

    class Meta :
        model = Buku

