from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

 #v1
#def inicio(request):
#    return HttpResponse('Hola soy la vista')

def inicio(request):
    archivo=open(r'C:\Users\Agustin\Desktop\mi_primer_Django\templates\inicio.html', 'r')
    
    template=Template(archivo.read())
    
    archivo.close()
    
    contexto=Context()
    
    renderizar_template=template.render(contexto)
    
    return HttpResponse(renderizar_template)
    
def segunda_vista(request):
    return HttpResponse('<h1>soy la segunda vista</h1>')

def fecha_actual(request):
    
    fecha=datetime.now()

    return HttpResponse(f'<h1>Fecha actaual: {fecha}</h1>')

def saludar(request):
    return HttpResponse('Bienvenide!!!')

def bienvenide(request,nombre,apellido):
    return HttpResponse(f'Bienvenide {nombre.title()} {apellido.title()}!!!')