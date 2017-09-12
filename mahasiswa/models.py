# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mahasiswa(models.Model):

    nim = models.CharField(max_length=10)
    nama = models.TextField(max_length=100)
    prodi = models.TextField(max_length=100)
    semester = models.IntegerField()
    
    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'mahasiswa'
        ordering = ['-id']
        
        
