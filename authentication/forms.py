from django import forms

from authentication.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nombres',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'Ingrese su nombre...'})

    )

    last_name = forms.CharField(
        label='Apellidos',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'last_name', 'placeholder': 'Ingrese sus apellidos...'})

    )
    email = forms.CharField(
        label='Correo',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Ingrese su correo...'})

    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Ingrese su contraseña...',
                   'type': 'password'})
    )

    celular = forms.CharField(
        label='Celular',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'celular', 'placeholder': 'Ingrese su celular...'})

    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'celular']