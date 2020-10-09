from django.urls import path
from . import views

urlpatterns = [
    
    path('budget2', views.categories_sum, name='cat_data'),
    path('all', views.dashboard_all, name='dash_month'),
    path('dashmonth/<str:id>', views.dashboard_month, name='dash_month'),
    path('semester/<int:year>/<str:id>', views.dashboard_semester, name='dash_month'),



]