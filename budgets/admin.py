from django.contrib import admin

from .models import Budget, Lancamento, Month, Faturamento, Expense, Revenue, Revenue2

admin.site.register(Budget)
admin.site.register(Lancamento)
admin.site.register(Month)
admin.site.register(Faturamento)
admin.site.register(Expense)
admin.site.register(Revenue2)


