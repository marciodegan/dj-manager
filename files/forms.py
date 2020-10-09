from django import forms
from .models import File, FileLancamento, FileDate


class FileModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file_name',)


class FileLancamentoModelForm(forms.ModelForm):
    class Meta:
        model = FileLancamento
        fields = ('file_name',)


class FileDateModelForm(forms.ModelForm):
    class Meta:
        model = FileDate
        fields = ('file_name',)
