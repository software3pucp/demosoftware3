from django import forms

from authentication.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'Ingrese su nombres y apellidos...'})

    )

    codigo = forms.CharField(
        label='Codigo',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'codigo', 'placeholder': 'Ingrese su codigo PUCP...'})

    )
    email = forms.CharField(
        label='Correo',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Ingrese su correo...'})

    )

    genero = forms.CharField(
        label='Genero',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'genero', 'placeholder': 'Ingrese su genero...', })
    )


    estado = forms.CharField(
        label='Estado',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'estado', 'placeholder': 'Ingrese su estado...',})
    )

    class Meta:
        model = User
        fields = ['first_name', 'codigo', 'email', 'genero','estado']