from django import forms

from .models import Task, FaturamentoOrigem

class LancamentoForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'category')


class FaturamentoOrigemForm(forms.ModelForm):

    class Meta:
        model = FaturamentoOrigem
        fields = ('origem',)