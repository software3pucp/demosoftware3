from django import forms

from authentication.models import User

# temporal
gen_aux = [
    (1, "Masculino"),
    (2, "Femenino"),
    (3, "No especifica")
]

estatus_aux = [
    (1, "Activo"),
    (2, "Inactivo")
]


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

    genero = forms.ChoiceField(
        choices=gen_aux,
        label='Genero',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control selectpicker', 'id': 'genero'})
    )

    estado = forms.ChoiceField(
        choices=estatus_aux,
        label='Estado',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control selectpicker', 'id': 'estado' })
    )

    class Meta:
        model = User
        fields = ['first_name', 'codigo', 'email', 'genero', 'estado']
