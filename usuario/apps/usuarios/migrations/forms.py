from apps.usuarios.models import User
from django import forms


class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'rol',
            'password',

        ]
        labels = {
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'rol': 'Rol',
            'password': 'Ingrese un Password',

        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.TextInput({'type': 'password'}),

        }

    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        print('legal pio?')
        cleaned_data = super(RegistroForm, self).clean()
        print(cleaned_data.get('email'))
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            print(confirm_password)
            print(cleaned_data.get('email'))
            raise forms.ValidationError(
                "Los passwords no coinciden"
            )
