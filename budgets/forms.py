from django import forms

from .models import Lancamento, Faturamento, Expense, Revenue2
from tasks.models import Category

class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ('amount', 'amount2', 'amount3', 'amount4', 'amount5','amount6', 'amount8','amount9', 'amount10', 'amount11', 'amount12')
        labels = {
            'lancamento': 'Despesa',
            'amount': '1° mês',
            'amount2': '2° mês',
            'amount3': '3° mês',
            'amount4': '4° mês',
            'amount5': '5° mês',
            'amount6': '6° mês',
            'amount7': '7° mês',
            'amount8': '8° mês',
            'amount9': '9° mês',
            'amount10': '10° mês',
            'amount11': '11° mês',
            'amount12': '12° mês'

        }


class LancamentoForm2(forms.ModelForm):
    class Meta:
        model = Lancamento

        fields = ('lancamento', 'amount', 'amount2', 'amount3', 'amount4', 'amount5','amount6', 'amount8','amount9', 'amount10', 'amount11', 'amount12')
        labels = {
            'lancamento': 'Despesa Fixa',
            'amount': '1° mês',
            'amount2': '2° mês',
            'amount3': '3° mês',
            'amount4': '4° mês',
            'amount5': '5° mês',
            'amount6': '6° mês',
            'amount7': '7° mês',
            'amount8': '8° mês',
            'amount9': '9° mês',
            'amount10': '10° mês',
            'amount11': '11° mês',
            'amount12': '12° mês'

        }


class FaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = ('faturamentoorigem', 'amount')
        labels = {
            'faturamentoorigem': 'Origem',
            'amount': 'Valor'
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('expenseType', 'amount', 'date', 'repetir')
        labels = {
            'expenseType': 'Despesa',
            'amount': 'Valor',
            'date': 'Data inicial',
            'repetir': 'Repetir X meses' 
        }
 

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue2
        fields = ('Revenue_origin', 'amount', 'date')
        labels = {
            'Revenue_origin': 'Origem',
            'amount': 'Valor',
            'date': 'Data'
        }