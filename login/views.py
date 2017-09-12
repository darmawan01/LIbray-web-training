# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from login.forms import Login
from django.contrib import messages
from django.http import HttpResponse
import requests

# Create your views here.
class LoginView(View):
    template_name = "login/login.html"

    def get(self, request) :
        if request.user.is_authenticated:
            return redirect('/peminjaman/')
        form = Login(request.POST or None)
        data = {
            'form': form
        }

        return render(request,self.template_name, data)
    
class DoLogin(View):
    def post(self, request):
        form = Login(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)
            if user :
                login(request, user)
                return redirect('/peminjaman/')
            else:
                messages.add_message(request, messages.WARNING, 'Username atau Password anda salah !!!')
        return redirect('/login/')

class DoLogout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/login/')
