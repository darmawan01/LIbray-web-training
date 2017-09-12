from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListPeminjaman.as_view(), name='view'),
    url(r'^add/$', views.addPeminjaman.as_view(), name='add'),
    url(r'^save/$', views.SavePeminjaman.as_view(), name='save'),
]
