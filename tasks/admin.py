from django.contrib import admin

from .models import Task, Category, FaturamentoOrigem, ExpenseType

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(FaturamentoOrigem)
admin.site.register(ExpenseType)

