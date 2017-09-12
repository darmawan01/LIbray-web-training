# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from buku.forms import BukuForm
from .models import Buku
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Auth(LoginRequiredMixin):
    login_url = '/login/'

class ListBuku(Auth, View):
    template_name = 'buku/list.html'

    def get(self, request):
        data ={
            'list_buku' : Buku.objects.all()
        }

        return render(request,self.template_name, data)

class TambahBuku(Auth, View):
    template_name = 'buku/insert.html'

    def get(self, request):
        form = BukuForm(request.POST or None)
        return render(request, self.template_name, {'form': form})

class SaveBuku(Auth, View):

    def post(self, request):
        form = BukuForm(request.POST or None)
        if form.is_valid():
            buku = Buku()
            buku.nama = form.cleaned_data['nama']
            buku.pengarang = form.cleaned_data['pengarang']
            buku.penerbit = form.cleaned_data['penerbit']
            buku.thn_terbit = form.cleaned_data['thn_terbit']
            buku.save()

            messages.add_message(request, messages.SUCCESS,'Data Berhasil Di tambah !!!')

        return redirect('/buku/')

class EditBuku(Auth, View):
    template_name = 'buku/update.html'

    def get(self, request, id):
        buku = Buku.objects.get(pk=id)
        initial = {
            'id': buku.pk,
            'nama': buku.nama,
            'pengarang': buku.pengarang,
            'penerbit': buku.penerbit,
            'thn_terbit': buku.thn_terbit,
        }

        form = BukuForm(initial=initial)
        data = {
            'form': form
        }

        return render(request, self.template_name, data)

class UpdateBuku(Auth, View):
    
    def post(self, request):
    
        form = BukuForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            buku = Buku.objects.get(pk=id)
            buku.nama = form.cleaned_data['nama']
            buku.pengarang = form.cleaned_data['pengarang']
            buku.penerbit = form.cleaned_data['penerbit']
            buku.thn_terbit = form.cleaned_data['thn_terbit']
            buku.save(force_update=True)
            
            return redirect('/buku/')

class HapusBuku(Auth, View):
    
    def get(self, request, id):
        buku = Buku.objects.get(pk=id)
        if buku:
            buku.delete()
            return redirect('/buku/')
