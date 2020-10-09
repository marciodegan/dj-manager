from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count

import matplotlib.pyplot as plt
from budgets.models import Expense, Revenue2
from products.models import Product


def expenses(request):
    expenses = Expense.objects\
        .values('expenseType__category__category')\
        .annotate(value=Sum('amount'))\
        .order_by('expenseType__category__category')
       
    data = {
        'data': [
            {
                'label': item['expenseType__category__category'],
                'value': item['value']
            }
            for item in expenses
        ]
    }
    return JsonResponse(data)


def expensesSemester(request, year, id):
    expense = Expense.objects.values('date__month_year').filter(date_id__semester=id, date_id__year=year).annotate(counter=Count('date__month_year')).annotate(total=Sum('amount')).values('total', 'date__month_year')
    revenue = Revenue2.objects.values('date__month_year').filter(date_id__semester=id, date_id__year=year).annotate(counter=Count('date__month_year')).annotate(total=Sum('amount')).values('total', 'date__month_year')
   
    data = {
        'data': [
            {
                'label': item['date__month_year'],
                'value': item['total']
            }
            for item in expense
        ],
        'data2': [
            {
                'label': item['date__month_year'],
                'value': item['total']
            }
            for item in revenue
        ]
    }
    return JsonResponse(data)


def expensesSemesterByCategory(request, year, id):
    expense = Expense.objects.values('expenseType__category__category').filter(date_id__semester=id, date_id__year=year).annotate(counter=Count('date__month_year')).annotate(total=Sum('amount')).values('total', 'expenseType__category__category')
   
    data = {
        'data': [
            {
                'label': item['expenseType__category__category'],
                'value': item['total']
            }
            for item in expense
        ]
    }
    return JsonResponse(data)