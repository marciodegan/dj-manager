from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileModelForm, FileLancamentoModelForm, FileDateModelForm
from .models import File, FileLancamento, FileDate
import csv

from products.models import Product
from budgets.models import Expense
from dates.models import Date


def upload_file_lancamento_view(request):
    form = FileLancamentoModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = FileLancamentoModelForm()
        obj = FileLancamento.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:                                                       
                    Expense.objects.create(
                        expenseType_id = row[0],
                        amount = row[1] or 0,
                        date = row[2],
                    )
                    # print(row[0] "JA CADASTRADO")
                    # print(type(row))
            obj.activated = True
            obj.save()
    return render(request, 'files/upload.html', {'form': form})


def upload_file_view(request):
    form = FileModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = FileModelForm()
        obj = File.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                                                          
                    if Product.objects.filter(ref=row[1]).exists():
                        pass
                    else:
                        Product.objects.create(
                            name = row[0] or 'Não informado',
                            ref = row[1] or 'Não informado',
                            salesprice = row[2] or 0,
                            buyprice = row[3],
                            quantity = row[4],
                            sales_comission = row[5] or 0,
                            bonus = row[6] or 0,
                            package_cost = row[7] or 0
                            )
                    # print(row[0] "JA CADASTRADO")
                    # print(type(row))
            obj.activated = True
            obj.save()
    return render(request, 'files/upload.html', {'form': form})


def upload_file_date_view(request):
    form = FileDateModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = FileDateModelForm()
        obj = FileDate.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            Date.objects.all().delete()
            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                                                                             
                    Date.objects.create(
                            date = row[0],
                            month = row[1],
                            year = row[2],
                            month_year = row[3],
                            semester = row[4],
                            trimester = row[5],
                            quartile = row[6]
                            )
            obj.activated = True
            obj.save()
    return render(request, 'files/upload.html', {'form': form})