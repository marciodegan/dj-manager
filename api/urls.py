from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('expenses', views.expenses, name='expenses_api'),
    path('semester/<int:year>/<str:id>', views.expensesSemester, name='expenses_semester_api'),
    path('semester/bycategory/<int:year>/<str:id>', views.expensesSemesterByCategory, name='expenses_semester_by_category_api'),  
 
]