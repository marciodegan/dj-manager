from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from dashboard.models import Order
from django.core import serializers
from django.views.generic import TemplateView
from django.db.models import Sum, Count
from functools import reduce
from operator import add


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from budgets.models import Budget, Lancamento, Faturamento, Revenue2, Expense
from products.models import Product
from dates.models import Date


class LancamentoChartView(TemplateView):
    template_name = 'tasks/index2.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"] = Lancamento.objects.all()
        category = Lancamento.objects\
            .values('lancamento__category__category')\
            .annotate(value=Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12'))\
            .order_by('lancamento__category__category')
        
        context['spendings'] = category.aggregate(total = (Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12'))/12)
        context['spendings_total'] = category.aggregate(total = (Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12')))

        sales = Faturamento.objects\
            .values('faturamentoorigem')\
            .annotate(value=Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12'))\
            .order_by('faturamentoorigem') 
        context['sales_period'] = Faturamento.objects\
            .values('amount', 'amount2').filter(faturamentoorigem=1)

        context['sales'] = sales.aggregate(total = (Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12'))/12)
        context['sales_total'] = sales.aggregate(total = (Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12')))

        faturamento = Faturamento.objects.all().filter(faturamentoorigem=1)
        listalocal = []


  
def categories_sum(request):
    product = get_object_or_404(Product, id=1)
    budget = get_object_or_404(Budget, pk=1)
    sales = Faturamento.objects\
        .values('faturamentoorigem')\
        .annotate(value=Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12'))
    salessum = sales.aggregate(Sum('value'))['value__sum']
    buy_sell = product.buyprice/product.salesprice*100
    package_total = product.package_cost/100 * product.salesprice
    tax_format = (budget.tax/100) * product.salesprice
    tax_total = '{:.2f}'.format(tax_format)
    sales_comission = product.sales_comission/100 * product.salesprice
    bonus = product.bonus/100 * product.salesprice
    spending_all = Lancamento.objects.filter(budget=1)
    spending_agg = spending_all.aggregate(soma=(Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12')))
    spending_total = spending_agg['soma']
    spending_percentage = spending_total/salessum*100
    total_geral = 100-(spending_percentage + buy_sell + package_total + budget.tax + product.sales_comission + product.bonus)
    total_cash = total_geral/100 * product.salesprice

    categories = Lancamento.objects\
        .values('lancamento__category__category')\
        .annotate(value=Sum('amount')+Sum('amount2')+Sum('amount3')+Sum('amount4')+Sum('amount5')+Sum('amount6')+Sum('amount7')+Sum('amount8')+Sum('amount9')+Sum('amount10')+Sum('amount11')+Sum('amount12'))\
        .order_by('lancamento__category__category')
    
    data = {
        'data': [
            {
                'label': item['lancamento__category__category'],
                'value': item['value'],
                
            }
          
            for item in categories
        ], 'product': product, 'salessum': salessum, 'tax_total': tax_format,'budget':budget, 'package_total': package_total, 'total_geral':spending_total, 'total_geral':total_geral, 'buy_sell': buy_sell, 'spending_percentage':spending_percentage, 'sales_comission': sales_comission, 'bonus': bonus, 'total_cash': total_cash
    }
    return render(request, 'products/product.html', data)


def dashboard_all(request):
    revenue = Revenue2.objects.all()
    revdate = Revenue2.objects.values('date__month_year')\
        .annotate(counter=Count('date__month_year')).order_by('date')
    revyear = Revenue2.objects.values('date__year')\
        .annotate(counter=Count('date__year'))
 
    data = {
        "revenue": revenue, "revdate": revdate, "revyear": revyear
        }
    return render(request, 'dashboard/dash_all.html', data)


def dashboard_month(request, id):
    dates = Date.objects.values('year').annotate(counter=Count('year')).values('year')
    monthyear = Date.objects.values('year','month_year').annotate(counter=Count('month_year')).values('month_year', 'year')
    semester = Date.objects.values('year','semester').annotate(counter=Count('semester')).values('semester', 'year')
    trimester = Date.objects.values('year','trimester').annotate(counter=Count('trimester')).values('trimester', 'year')
    quartile = Date.objects.values('year','quartile').annotate(counter=Count('quartile')).values('quartile', 'year')
    revenue = Revenue2.objects.filter(date_id__month_year=id)
    revdate2020 = Revenue2.objects.filter(date__year=2020).values('date__month_year')\
        .annotate(counter=Count('date__month_year')).order_by('date')
    revdate2021 = Revenue2.objects.filter(date__year=2021).values('date__month_year')\
        .annotate(counter=Count('date__month_year')).order_by('date')
    
    revyear2020 = Revenue2.objects.filter(date__year=2020).values('date__year')\
        .annotate(counter=Count('date__year'))
    revyear2021 = Revenue2.objects.filter(date__year=2021).values('date__year')\
        .annotate(counter=Count('date__year'))

    data = {
        "revenue": revenue, "revdate2020": revdate2020, "revdate2021": revdate2021, 
        "revyear2020": revyear2020, "revyear2021": revyear2021, 'dates': dates, 'monthyear': monthyear,
        "semester": semester, "trimester": trimester, "quartile": quartile
        }
    return render(request, 'dashboard/dash_all.html', data)


def dashboard_semester(request, year, id):
    dates = Date.objects.values('year').annotate(counter=Count('year')).values('year')
    monthyear = Date.objects.values('year','month_year').annotate(counter=Count('month_year')).values('month_year', 'year')
    semester = Date.objects.values('year','semester').annotate(counter=Count('semester')).values('semester', 'year')
    trimester = Date.objects.values('year','trimester').annotate(counter=Count('trimester')).values('trimester', 'year')
    quartile = Date.objects.values('year','quartile').annotate(counter=Count('quartile')).values('quartile', 'year')
    
    revenue = Revenue2.objects.values('date__month_year').filter(date_id__semester=id, date_id__year=year).annotate(counter=Count('date__month_year')).annotate(total=Sum('amount')).values('total', 'date__month_year')
    revenue_total = Revenue2.objects.values('amount').filter(date_id__semester=id, date_id__year=year).aggregate(Sum('amount'))['amount__sum']
    expense = Expense.objects.values('date__month_year').filter(date_id__semester=id, date_id__year=year).annotate(counter=Count('date__month_year')).annotate(total=Sum('amount')).values('total', 'date__month_year')
    expense_total = Expense.objects.values('amount').filter(date_id__semester=id, date_id__year=year).aggregate(Sum('amount'))['amount__sum']
    yea = year
    sem = id

    data = {
        "revenue": revenue, 
        'dates': dates, 'monthyear': monthyear,
        "semester": semester, "trimester": trimester, "quartile": quartile, 'expense': expense,
        "revenue_total": revenue_total, 'expense_total': expense_total, 'yea': yea, 'sem': sem  
        }

    return render(request, 'dashboard/dash_all.html', data)

