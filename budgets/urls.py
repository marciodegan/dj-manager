from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('expense/add', views.expenseAdd, name='expense_add'),
    path('expense/edit/<int:id>', views.expenseEdit, name='expense-edit'),
    path('expense/editlist/<int:id>', views.expenseListEdit, name='expense_editlist'),
    path('expense/editfull/<int:id>', views.expenseFullEdit, name='expense_full_edit'),
    path('expense/delete/<int:id>', views.expenseDelete, name='expense_delete'),
    path('revenue/add', views.revenueAdd, name='revenue_add'),


    
  
]