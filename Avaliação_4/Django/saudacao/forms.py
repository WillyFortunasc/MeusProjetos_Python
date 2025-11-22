from django import forms
import re

class NomeForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome'
        }),
        label='Nome'
    )
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        # Validar se contém apenas letras e espaços
        if not re.match("^[a-zA-ZÀ-ÿ\s]+$", nome):
            raise forms.ValidationError("O nome deve conter apenas letras.")
        return nome