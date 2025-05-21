from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario, Desprendible

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombres', 'apellidos', 'celular', 'sueldo', 'fecha_ingreso', 'cargo', 'eps', 'pension']
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'eps': forms.TextInput(attrs={'class': 'form-control'}),
            'pension': forms.TextInput(attrs={'class': 'form-control'}),
        }

    #Validación para los campos numericos del registro
    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if int(cedula) < 0:
            raise ValidationError("La cédula no puede ser un valor negativo.")
        return cedula

    def clean_celular(self):
        celular = self.cleaned_data['celular']
        if int(celular) < 0:
            raise ValidationError("El número de celular no puede ser negativo.")
        if len(str(celular)) < 10:
            raise ValidationError("El número de celular debe tener al menos 10 dígitos.")
        return celular

    def clean_sueldo(self):
        sueldo = self.cleaned_data['sueldo']
        if sueldo <= 0:
            raise ValidationError("El sueldo debe ser un valor positivo.")
        return sueldo

class DesprendibleForm(forms.ModelForm):
    class Meta:
        model = Desprendible
        fields = ['horas_extra_diurna', 'horas_extra_nocturna', 'horas_extra_diurna_dominical', 'horas_extra_nocturna_dominical']
        widgets = {
            'horas_extra_diurna': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas_extra_nocturna': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas_extra_diurna_dominical': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas_extra_nocturna_dominical': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Validación para que solo permita números positivos en cada campo de horas extra
    def clean_horas_extra_diurna(self):
        horas_extra_diurna = self.cleaned_data.get('horas_extra_diurna')
        if horas_extra_diurna is not None and horas_extra_diurna < 0:
            raise forms.ValidationError("Las horas extra diurnas no pueden ser negativas.")
        return horas_extra_diurna

    def clean_horas_extra_nocturna(self):
        horas_extra_nocturna = self.cleaned_data.get('horas_extra_nocturna')
        if horas_extra_nocturna is not None and horas_extra_nocturna < 0:
            raise forms.ValidationError("Las horas extra nocturnas no pueden ser negativas.")
        return horas_extra_nocturna

    def clean_horas_extra_diurna_dominical(self):
        horas_extra_diurna_dominical = self.cleaned_data.get('horas_extra_diurna_dominical')
        if horas_extra_diurna_dominical is not None and horas_extra_diurna_dominical < 0:
            raise forms.ValidationError("Las horas extra diurnas dominicales no pueden ser negativas.")
        return horas_extra_diurna_dominical

    def clean_horas_extra_nocturna_dominical(self):
        horas_extra_nocturna_dominical = self.cleaned_data.get('horas_extra_nocturna_dominical')
        if horas_extra_nocturna_dominical is not None and horas_extra_nocturna_dominical < 0:
            raise forms.ValidationError("Las horas extra nocturnas dominicales no pueden ser negativas.")
        return horas_extra_nocturna_dominical