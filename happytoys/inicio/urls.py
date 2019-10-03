from django.conf.urls import url, include
from inicio.views import *

urlpatterns = [
    url(r"^$",inicio),
    url(r'^descripcion/$',descripcion),
    url(r'^login/$',login),
    url(r'^login/logueado/$',vista_logueado),
    url(r'^buscador/$',buscador),
     
]
