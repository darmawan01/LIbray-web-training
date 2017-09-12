from django import forms
from .models import Peminjaman
from buku.models import Buku
from mahasiswa.models import Mahasiswa
import datetime

class PeminjamanForm(forms.Form):
    
    tgl_pinjam = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)
    bts_pinjam = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)
    buku = forms.ModelChoiceField(queryset=Buku.objects.all())
    mahasiswa = forms.ModelChoiceField(queryset=Mahasiswa.objects.all())

    class Meta:
        model = Peminjaman