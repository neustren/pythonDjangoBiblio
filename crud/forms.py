from django import forms

from .models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
