from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from products.forms import ProductForm
from django.contrib import messages
from django.db.models import Sum, Q, Count
from django.db.models import Q
from django.forms import formset_factory

from .models import Product
from budgets.models import Budget, Lancamento, Faturamento, Revenue, Expense

'''
@login_required
def ProductView(request, id):
    product = get_object_or_404(Product, pk=id)
    data = Lancamento.objects\
        .values('lancamento__title','lancamento__category__category', 'amount', 'amount2', 'amount3', 'amount4', 'amount5', 'amount6', 'amount7', 'amount8', 'amount9', 'amount10', 'amount11', 'amount12')\
        .order_by('lancamento__category__category')
    soma = data.aggregate(Sum('amount'))['amount__sum']



    return render(request, 'tasks/product.html', {'product': product})

'''

@login_required
def newProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('/product/productlist')
    else:
        form = ProductForm()
        return render(request, 'products/productadd.html', {'form': form})


@login_required
def editProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)

    if(request.method == 'POST'):
        form = ProductForm(request.POST, instance=product)

        if(form.is_valid()):
            product.save()
            return redirect('/dashboard/budget2')
        else:
            return render(request, 'products/editproduct.html', {'form': form, 'product': product})
    else:
        return render(request, 'products/editprod.html', {'form': form, 'product': product })


def productPricing(request, id):
    product = get_object_or_404(Product, id=id)
    budget = get_object_or_404(Budget)
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
    spending_all = Lancamento.objects.all()
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
    return render(request, 'products/productpricing.html', data)


def productPricing2(request, id):
    now = datetime.now()
    end_date = now+timedelta(days=365)
    product = get_object_or_404(Product, id=id)
    budget = get_object_or_404(Budget)
    sales = Revenue.objects.values('amount').filter(date__range=(now, end_date))\
        .aggregate(totalrevenue=Sum('amount'))
        
    categories = Expense.objects.values('expenseType__category__category').filter(date__range=(now, end_date))\
        .annotate(value=Sum('amount'))\
        .values('value', 'expenseType__category__category')
    categories_total = Expense.objects.values('amount').filter(date__range=(now, end_date))\
        .aggregate(totalspent=Sum('amount'))

    # salessum = sales.aggregate(Sum('value'))['value__sum']
    buy_sell = (product.buyprice/product.salesprice)*100
    package_total = (product.package_cost/product.salesprice)*100
    tax_format = (budget.tax/product.salesprice)*100
    tax_total = '{:.2f}'.format(tax_format)
    sales_comission = (product.sales_comission/100) * product.salesprice
    bonus = (product.bonus/100) * product.salesprice
    spendings = (categories_total['totalspent']/sales['totalrevenue'])*100

    total_geral = (product.salesprice/product.salesprice)*100-(spendings + buy_sell + package_total + budget.tax + product.sales_comission + product.bonus)
    total_cash = product.salesprice - (product.buyprice + product.package_cost + sales_comission + bonus + tax_format +(spendings/100)*product.salesprice)
      
    data = {
        'data': [
            {
                'label': item['expenseType__category__category'],
                'value': item['value']
            }
          
            for item in categories
        ], 'product': product, 'tax_total': tax_format,'budget':budget, 'package_total': package_total, 'buy_sell': buy_sell, 'sales_comission': sales_comission, 'bonus': bonus,
            'salessum': sales, 'now': now, 'end_date':end_date, 'categories_total': categories_total, 'total_geral': total_geral, 'total_cash': total_cash
    }
    return render(request, 'products/productpricing2.html', data)

@login_required
def productList(request):
    product_list = Product.objects.all().order_by('-created_at')
    ProductFormSet = formset_factory(ProductForm)
    formset = formset_factory(ProductFormSet)
    return render(request, 'products/productlist.html', {'product_list': product_list, 'formset': formset })


@login_required
def productListAnalytics(request):
    now = datetime.now()
    end_date = now+timedelta(days=365)
    product = Product.objects.all()
    budget = get_object_or_404(Budget)
    sales = Revenue.objects.values('amount').filter(date__range=(now, end_date))\
        .aggregate(totalrevenue=Sum('amount'))
        
    categories = Expense.objects.values('expenseType__category__category').filter(date__range=(now, end_date))\
        .annotate(value=Sum('amount'))\
        .values('value', 'expenseType__category__category')
    categories_total = Expense.objects.values('amount').filter(date__range=(now, end_date))\
        .aggregate(totalspent=Sum('amount'))

    # buy_sell = (product.buyprice/product.salesprice)*100
    # package_total = (product.package_cost/product.salesprice)*100
    # tax_format = (budget.tax/product.salesprice)*100
    # tax_total = '{:.2f}'.format(tax_format)
    # sales_comission = (product.sales_comission/100) * product.salesprice
    # bonus = (product.bonus/100) * product.salesprice
    spendings = (categories_total['totalspent']/sales['totalrevenue'])*100

    # total_geral = (product.salesprice/product.salesprice)*100-(spendings + buy_sell + package_total + budget.tax + product.sales_comission + product.bonus)
    # total_cash = product.salesprice - (product.buyprice + product.package_cost + sales_comission + bonus + tax_format +(spendings/100)*product.salesprice)
      
    data = {
        'data': [
            {
                'label': item['expenseType__category__category'],
                'value': item['value'],
            }
            for item in categories
        ], 'product_list': product, 'budget':budget, 'salessum': sales, 'categories_total': categories_total, 'spendings': spendings 
    }
    return render(request, 'products/productlist2.html', data)


