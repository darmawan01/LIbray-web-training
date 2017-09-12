# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from buku.models import Buku
from mahasiswa.models import Mahasiswa

# Create your models here.
class Peminjaman(models.Model):
    
    tgl_pinjam = models.DateField()
    bts_pinjam = models.DateField()
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='bukus')
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='mahasiswas')

    def __str__(self):
        return str(self.tgl_pinjam)

    class Meta:
        db_table = 'peminjam'
        ordering = ['-id']

