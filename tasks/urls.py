from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    
    # path('task/<int:id>', views.taskView, name="task-view"),
    path('add/', views.lancamentoAdd, name="lancamento-add"),
    path('list/', views.lancamentoList, name="lancamento-list"),
    path('faturamento/add/', views.faturamentoAdd, name="faturamento-add"),
    path('faturamento/list/', views.faturamentoList, name="faturamento-add"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]