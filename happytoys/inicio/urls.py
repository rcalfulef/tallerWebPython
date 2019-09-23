from django.conf.urls import url, include
from inicio.views import *

urlpatterns = [
    url(r"^$",inicio),
    url(r'^descripcion/$',descripcion),
     
]
