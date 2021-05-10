from django import forms

from authentication.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nombres',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'Ingrese su nombre...'})

    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'celular']