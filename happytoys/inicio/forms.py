from django import forms
from .models import *

class JugueteForm(forms.ModelForm):
    
    class Meta:
        model = Juguete
        fields = ("nombre","precio","cantidad","descripcion","imageFile")
    def __init__(self,*args,**kwargs):
        super(JugueteForm,self).__init__(*args,**kwargs)
        self.fields["nombre"].widget.attrs.update({'class':'form-control','placeholder':'Ingrese nombre juguete'})
        self.fields["precio"].widget.attrs.update({'class':'form-control','placeholder':'Ingrese precio'})
        self.fields["cantidad"].widget.attrs.update({'class':'form-control','placeholder':'Ingrese cantidad'})
        self.fields["descripcion"].widget.attrs.update({'class':'form-control','placeholder':'Ingrese alguna descripción'})
        self.fields["imageFile"].widget.attrs.update({'class': 'form-control-file'})


class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ("name", "imageFile")