# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Buku(models.Model):
    
    nama = models.TextField(max_length=100)
    pengarang = models.TextField(max_length=100)
    penerbit = models.TextField(max_length=100)
    thn_terbit = models.CharField(max_length=5)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'buku'
        ordering = ['-id']