from django.urls import path
from .views import inicio, registrar_usuario, lista_usuarios, calcular_horas_extras, resumen, eliminar_empleados, editar_usuario

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('calcular/<str:cedula>/', calcular_horas_extras, name='calcular'),
    path('resumen/<str:cedula>/', resumen, name='resumen'),
    path('eliminar_empleados/', eliminar_empleados, name='eliminar_empleados'),
    path('actualizar/<int:cedula>/', editar_usuario, name='editar_usuario'),
]
