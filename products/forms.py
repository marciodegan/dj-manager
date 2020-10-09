from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Product

# class ProductForm(forms.ModelForm):

#     class Meta:
#         model = Product
#         fields = ('name', 'salesprice', 'buyprice', 'quantity', 'sales_comission', 'bonus', 'package_cost')
#         labels = {
#             "name": "nome"
#         }
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'salesprice': forms.TextInput(attrs={'class':'form-control'}),
#             'buyprice': forms.TextInput(attrs={'class':'form-control'}),
#             'quantity': forms.TextInput(attrs={'class':'form-control'}),
#             'sales_comission': forms.TextInput(attrs={'class':'form-control'}),
#             'bonus': forms.TextInput(attrs={'class':'form-control'}),
#             'package_cost': forms.TextInput(attrs={'class':'form-control'})
#         }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'salesprice', 'buyprice', 'quantity', 'sales_comission', 'bonus', 'package_cost')
       
        labels = {
               'name': 'Nome',
               'salesprice': 'Preço de Venda',
               'buyprice': 'Preço de Compra',
               'quantity': 'Quantidade prevista a ser vendida',
               'sales_comission': 'Comissão',
               'bonus': 'bônus',
               'package_cost': 'Embalagem'
            }

        error_messages = {
               'name': {
               'max_length': "Name can only be 25 characters in length"
                }
            }
            
       
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'ref', 'salesprice', 'buyprice', 'quantity', 'sales_comission', 'bonus', 'package_cost')
       
