from django import forms 

class PerroFormularioBase(forms.Form):
    nombre=forms.CharField(max_length=20)
    edad=forms.IntegerField()
  
class CrearPerroFormulario(PerroFormularioBase):
    ...
    
class ModificarPerroFormulario(PerroFormularioBase):    
    ...    
    
class BuscarPerroFormulario(forms.Form):
    nombre=forms.CharField(max_length=20, required=False)
    
