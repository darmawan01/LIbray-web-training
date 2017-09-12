from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListBuku.as_view(), name='view'),
    url(r'^add/$', views.TambahBuku.as_view(), name='add'),
    url(r'^save/$', views.SaveBuku.as_view(), name='save'),
    url(r'^edit/(?P<id>\d+)$', views.EditBuku.as_view(), name='edit'),
    url(r'^update/$', views.UpdateBuku.as_view(), name='update'),
    url(r'^remove/(?P<id>\d+)$', views.HapusBuku.as_view(), name='remove'),
]
