from .models import *
from django.forms import ModelForm, TextInput, Textarea


class SvazForm(ModelForm):
    class Meta:
        model = Svaz
        fields = ['last_name', 'first_name', 'sposob', 'pravki',]
        widgets = {
            'last_name': TextInput(attrs={
                'placeholder': 'Фамилия'
            }),
            'first_name': TextInput(attrs={
                'placeholder': 'Имя'
            }),
            'sposob': TextInput(attrs={
                'placeholder': 'Способ обратной связи'
            }),
            'pravki': Textarea(attrs={
                'placeholder': 'Внесите правки'
            }),
        }