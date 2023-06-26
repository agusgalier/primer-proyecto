from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('prueba/', views.prueba,name='prueba'),
    path('segunda-vista/', views.segunda_vista,name='segunda_vista'),
    path('fecha-actual/', views.fecha_actual,name='fecha_actual'),
    path('saludar/', views.saludar,name='saludar'),
    path('bienvenide/<str:nombre>/<str:apellido>/', views.bienvenide,name='bienvenide'),
    #v1 crear perro
    # path('crear-perro/<str:nombre>/<int:edad>/', views.crear_perro,name='crear_perro')  
    #v2 crear perro
    path('perros/', views.listar_perros,name='listar_perros'),  
    path('perros/crear/', views.crear_perro,name='crear_perro'),  
]
