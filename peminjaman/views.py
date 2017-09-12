# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from peminjaman.forms import PeminjamanForm
from .models import Peminjaman
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Auth(LoginRequiredMixin):
    login_url = '/login/'

class ListPeminjaman(Auth, View):
    template_name = 'peminjaman/list.html'

    def get(self, request):
        data = {
            'list_peminjaman': Peminjaman.objects.all()
        }
        return render(request, self.template_name, data)


class addPeminjaman(Auth, View):
    template_name = 'peminjaman/insert.html'

    def get(self, request):
        form = PeminjamanForm(request.POST or None)
        return render(request, self.template_name, {'form': form})


class SavePeminjaman(Auth, View):

    def post(self, request):
        form = PeminjamanForm(request.POST or None)
        if form.is_valid():
            peminjaman = Peminjaman()
            peminjaman.tgl_pinjam = form.cleaned_data['tgl_pinjam']
            peminjaman.bts_pinjam = form.cleaned_data['bts_pinjam']
            peminjaman.buku = form.cleaned_data['buku']
            peminjaman.mahasiswa = form.cleaned_data['mahasiswa']
            peminjaman.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Simpan Jurnal Berhasil')
        return redirect('/peminjaman/')
