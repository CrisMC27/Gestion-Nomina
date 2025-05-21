from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, DesprendibleForm
from .models import Usuario, Desprendible
from decimal import Decimal


# Vista para registrar un nuevo usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige al inicio tras guardar el usuario
    else:
        form = UsuarioForm()

    return render(request, 'registro_usuario.html', {'form': form})

# Vista para listar todos los usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtiene todos los usuarios de la base de datos
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista de calcular y guardar
def calcular_horas_extras(request, cedula):
    usuario = get_object_or_404(Usuario, cedula=cedula)
    
    if request.method == 'POST':
        form = DesprendibleForm(request.POST)
        if form.is_valid():
            desprendible = form.save(commit=False)
            
            # Guardar la cédula en lugar de la relación con el modelo Usuario
            desprendible.usuario_cedula = usuario.cedula
            
            # Cálculo del auxilio de transporte
            sueldo = usuario.sueldo
            auxilio_transporte = Decimal('162000') if sueldo <= Decimal('2600000') else Decimal('0')
            
            # Descuentos de salud y pensión (4% cada uno)
            descuento_salud = sueldo * Decimal('0.04')
            descuento_pension = sueldo * Decimal('0.04')

            # Cálculo de horas extras
            horas_extra_diurna = form.cleaned_data['horas_extra_diurna']
            horas_extra_nocturna = form.cleaned_data['horas_extra_nocturna']
            horas_extra_diurna_dominical = form.cleaned_data['horas_extra_diurna_dominical']
            horas_extra_nocturna_dominical = form.cleaned_data['horas_extra_nocturna_dominical']
            
            total_hed = (sueldo / Decimal('240')) * horas_extra_diurna * Decimal('1.25')
            total_hen = (sueldo / Decimal('240')) * horas_extra_nocturna * Decimal('1.75')
            total_hedd = (sueldo / Decimal('240')) * horas_extra_diurna_dominical * Decimal('2')
            total_hend = (sueldo / Decimal('240')) * horas_extra_nocturna_dominical * Decimal('2.5')
            
            total_horas_extras = total_hed + total_hen + total_hedd + total_hend

            # Cálculo del sueldo a pagar
            total = sueldo + total_horas_extras + auxilio_transporte - descuento_salud - descuento_pension

            # Guardar el desprendible
            desprendible.horas_extra_diurna = horas_extra_diurna
            desprendible.horas_extra_nocturna = horas_extra_nocturna
            desprendible.horas_extra_diurna_dominical = horas_extra_diurna_dominical
            desprendible.horas_extra_nocturna_dominical = horas_extra_nocturna_dominical
            desprendible.total_horas_extras = total_horas_extras
            desprendible.total_hed = total_hed
            desprendible.total_hen = total_hen
            desprendible.total_hedd = total_hedd
            desprendible.total_hend = total_hend
            desprendible.total = total
            desprendible.auxilio_transporte = auxilio_transporte
            desprendible.descuento_salud = descuento_salud
            desprendible.descuento_pension = descuento_pension
            desprendible.save()

            return redirect('resumen', cedula=usuario.cedula)

        else:
            print(form.errors)

    else:
        form = DesprendibleForm()

    return render(request, 'calcular_horas_extras.html', {'form': form, 'usuario': usuario})

def resumen(request, cedula):
    usuario = get_object_or_404(Usuario, cedula=cedula)
    desprendible = get_object_or_404(Desprendible, usuario_cedula=usuario.cedula)

    return render(request, 'resumen.html', {
        'usuario': usuario,
        'desprendible': desprendible
    })

# Vista para elimanar empleados
def eliminar_empleados(request):
    if request.method == 'POST':
        empleados_a_eliminar = request.POST.getlist('empleados')
        Usuario.objects.filter(cedula__in=empleados_a_eliminar).delete()
        return redirect('inicio')

    usuarios = Usuario.objects.all()
    return render(request, 'eliminar_empleados.html', {'usuarios': usuarios})

# Vista para editar la información de un usuario (excepto la cédula)
def editar_usuario(request, cedula):
    usuario = get_object_or_404(Usuario, cedula=cedula)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
        form.fields['cedula'].disabled = True  # Deshabilitar el campo de cédula
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})
