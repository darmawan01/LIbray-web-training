# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from mahasiswa.forms import MahasiswaForm
from .models import Mahasiswa
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Auth(LoginRequiredMixin):
    login_url = '/login/'

class ListMahasiswa(Auth, View):
    template_name = 'mahasiswa/list.html'

    def get(self, request):
        data ={
            'list_mhs' : Mahasiswa.objects.all()
        }

        return render(request,self.template_name, data)

class TambahMahasiswa(Auth, View):
    template_name = 'mahasiswa/insert.html'

    def get(self, request):
        form = MahasiswaForm(request.POST or None)
        return render(request, self.template_name, {'form': form})

class SaveMahasiswa(Auth, View):

    def post(self, request):
        form = MahasiswaForm(request.POST or None)
        if form.is_valid():
            mhs = Mahasiswa()
            mhs.nim = form.cleaned_data['nim']
            mhs.nama = form.cleaned_data['nama']
            mhs.prodi = form.cleaned_data['prodi']
            mhs.semester = form.cleaned_data['semester']
            mhs.save()

            messages.add_message(request, messages.SUCCESS,'Data Berhasil Di tambah !!!')

        return redirect('/mahasiswa/')

class EditMahasiswa(Auth, View):
    template_name = 'mahasiswa/update.html'

    def get(self, request, id):
        mhs = Mahasiswa.objects.get(pk=id)
        initial = {
            'id': mhs.pk,
            'nim': mhs.nim,
            'nama': mhs.nama,
            'prodi': mhs.prodi,
            'semester': mhs.semester,
        }

        form = MahasiswaForm(initial=initial)
        data = {
            'form': form
        }

        return render(request, self.template_name, data)

class UpdateMahasiswa(Auth, View):
    
    def post(self, request):
    
        form = MahasiswaForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            mhs = Mahasiswa.objects.get(pk=id)
            mhs.nim = form.cleaned_data['nim']
            mhs.nama = form.cleaned_data['nama']
            mhs.prodi = form.cleaned_data['prodi']
            mhs.semester = form.cleaned_data['semester']
            mhs.save(force_update=True)
            
            return redirect('/mahasiswa/')

class HapusMahasiswa(Auth, View):
    
    def get(self, request, id):
        mhs = Mahasiswa.objects.get(pk=id)
        if mhs:
            mhs.delete()
            return redirect('/mahasiswa/')

