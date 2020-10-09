from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import LancamentoForm2, LancamentoForm, FaturamentoForm, ExpenseForm, RevenueForm
from django.contrib import messages
from dateutil.relativedelta import relativedelta
from django.db.models.functions import ExtractMonth, ExtractYear

from django.db.models import Sum, Q, Count
from django.forms.models import modelformset_factory, inlineformset_factory
from extra_views import ModelFormSetView
from django.forms import formset_factory
from django.views.generic.edit import FormView


from django_pandas.io import read_frame
import pandas as pd
import numpy as np
from IPython.display import HTML, display, display_html
from django.db.models.functions import Concat

from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

from tasks.models import Task, ExpenseType, FaturamentoOrigem
from .models import Budget, Lancamento, Faturamento, Expense, Revenue, Revenue2
from dates.models import Date

from django.http import JsonResponse


@login_required
def expenseAdd(request):
    now = datetime.now()
    end_date = now+timedelta(days=365)
    if request.method == 'POST':

        repeater = request.POST.get('repetir')
        amount = request.POST.get('amount')
        expenseType = request.POST.get('expenseType')
        date_get = request.POST.get('date')
        date = datetime.strptime(date_get, '%d/%m/%Y')
        repeat = int(repeater)
        for instance in range(repeat):
            date_id = get_object_or_404(Date, pk=date)
            Expense.objects.create(amount=amount, date_id=date_id.pk+relativedelta(months=instance), expenseType_id=expenseType)
        list = Expense.objects.last()
        obj = get_object_or_404(Expense, pk=list.pk)
        revenue = Revenue.objects.filter(date__range=(now, end_date))\
            .annotate(value=Sum('amount'))\
            .values('value')
        # return render(request, 'budgets/expenseedit.html', {'revenue': revenue})
        return redirect('expense-edit', id=list.expenseType_id)
   
    else:
        revenue = Revenue.objects.filter(date__range=(now, end_date))\
            .annotate(value=Sum('amount'))\
            .values('value')
        expenses = ExpenseType.objects.all()
        # categories = Expense.objects.values('expenseType__category__category').filter(date__range=(now, end_date))\
        #     .annotate(value=Sum('amount'))\
        #     .values('value', 'expenseType__category__category')
        
        return render(request, 'budgets/expenseadd.html', {'revenue':revenue, 'expenses': expenses})


@login_required
def expenseEdit(request, id):
    obj_id = id
    if request.method == 'POST':
        
        repeater = request.POST.get('repetir')
        amount = request.POST.get('amount')
        expenseType = request.POST.get('expenseType')
        date_get = request.POST.get('date')
        date = datetime.strptime(date_get, '%d/%m/%Y')
        repeat = int(repeater)
        for instance in range(repeat):
            Expense.objects.create(amount=amount, date=date+relativedelta(months=instance), expenseType_id=expenseType)
        list = Expense.objects.last()
        obj = get_object_or_404(Expense, pk=list.pk)
        return redirect('expense-edit', id=list.expenseType_id)

    else:
        now = datetime.now().date()
        end_date = now+timedelta(days=365)
        revenue = Revenue.objects.filter(date__range=(now, end_date))\
            .annotate(value=Sum('amount'))\
            .values('value')
        categories = Expense.objects.filter(expenseType=obj_id).filter(date__range=(now, end_date))\
            .annotate(value=Sum('amount'))\
            .values('value')
        expense = get_object_or_404(ExpenseType, pk=obj_id)
        
        return render(request, 'budgets/expenseedit.html', {'revenue':revenue, 'categories':categories, 'expense': expense})


@login_required
def expenseListEdit(request, id):
    obj_id = id
    now = datetime.now()
    end_date = now+timedelta(days=365)
    expenses = Expense.objects.filter(expenseType__id=obj_id).filter(date__range=(now, end_date))\
            .values('id', 'expenseType__title', 'amount', 'date').order_by('date')  
    
    list = Expense.objects.all()

    return render(request, 'budgets/expenselistedit.html', 
        {'list': list, 'expenses': expenses })


@login_required
def expenseFullEdit(request, id):
    expense = get_object_or_404(ExpenseType, pk=id)
    form = ExpenseForm(instance=expense)

    if(request.method == 'POST'):
        form = ExpenseForm(request.POST, instance=expense)

        if(form.is_valid()):
            expense.save()
            return redirect('/')
        else:
            return render(request, 'budgets/expensefulledit.html', {'form': form, 'expense': expense})
    else:
        obj_id = id
        now = datetime.now()
        past = now-timedelta(days=1000)
        end_date = now+timedelta(days=365)
        expenses = Expense.objects.filter(expenseType__id=id).filter(date__range=(now, end_date))\
                .values('id', 'expenseType__title', 'amount', 'date').order_by('date')
        expenses_past = Expense.objects.filter(expenseType__id=id).filter(date__range=(past, now))\
                .values('id', 'expenseType__title', 'amount', 'date').order_by('date')     
        
        return render(request, 'budgets/expensefulledit.html', {'form': form, 'expenses': expenses, 'expenses_past': expenses_past, 'expense': expense, 'past': past, 'now':now})


@login_required
def expenseDelete(request, id):
    expense = get_object_or_404(Expense, pk=id)
    expense.delete()

    messages.info(request, 'Despesa deletada com sucesso.')

    return redirect('expense_full_edit', id=expense.expenseType_id)


@login_required
def revenueAdd(request):
    if request.method == 'POST':
        repeater = request.POST.get('repetir')
        amount = request.POST.get('amount')
        revenue = request.POST.get('Revenue_origin')
        date_get = request.POST.get('date')
        date = datetime.strptime(date_get, '%d/%m/%Y')
        repeat = int(repeater)
        for instance in range(repeat):
            date_id = get_object_or_404(Date, pk=date)
            Revenue2.objects.create(amount=amount, date_id=date_id.pk+relativedelta(months=instance), Revenue_origin_id=1)
        list = Revenue2.objects.last()
        # obj = get_object_or_404(Revenue2, pk=list.pk)
        return render(request, 'budgets/expensefulledit.html', {})

    else:
        now = datetime.now()
        end_date = now+timedelta(days=365)
        form = RevenueForm()
        revenues = FaturamentoOrigem.objects.all()
        # revenue = Revenue.date_obj.values('conc').filter(date__range=(now, end_date))\
        #     .annotate(value=Sum('amount'), period=Count('conc'))\
        #     .values('value', 'conc')
        
        return render(request, 'budgets/revenue_add.html', {'revenues': revenues})