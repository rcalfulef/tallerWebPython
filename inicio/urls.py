from django.conf.urls import url, include
from inicio.views import *

app_name = 'inicio'


urlpatterns = [
    url(r"^$",inicio),
    url(r'^descripcion/$',descripcion),
    url(r'^login/$',login),
    url(r'^login/logueado/$',vista_logueado),
    url(r'^juguetes/$',juguetes,name='juguetes'),
    url(r'^buscador/$',buscador),
    url(r'^logout/$',logout,name ='logout'),
    url(r'^juguetes/(?P<juguete_id>\d+)/$', juguete_detail,name='jugueteDetail'),
    url(r'^juguetes/agregar/$',newJuguete,name='newJuguete'),
    url(r'^juguetes/new/$',newToy,name='newToy'),
    url(r'^images/$',showImage,name='showImage'),
]
