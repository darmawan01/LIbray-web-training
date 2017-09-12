from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListMahasiswa.as_view(), name='view'),
    url(r'^add/$', views.TambahMahasiswa.as_view(), name='add'),
    url(r'^save/$', views.SaveMahasiswa.as_view(), name='save'),
    url(r'^edit/(?P<id>\d+)$', views.EditMahasiswa.as_view(), name='edit'),
    url(r'^update/$', views.UpdateMahasiswa.as_view(), name='update'),
    url(r'^remove/(?P<id>\d+)$', views.HapusMahasiswa.as_view(), name='remove'),
]