from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models.functions import Concat
from django.db.models.functions import Trunc
from django.db.models import CharField, Value as V
import django.utils.timezone

from tasks.models import Task, FaturamentoOrigem, ExpenseType
from dates.models import Date

REPETIR = (
        ('1', 'Não repetir'),
        ('2', '1'),
        ('3', '2'),
        ('4', '3'),
        ('5', '4'),
        ('6', '5'),
        ('7', '6'),
        ('8', '7'),
        ('9', '8'),
        ('10', '9'),
        ('11', '10'),
        ('12', '11'),
        ('13', '12'),
    )

class Month(models.Model):
    name = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Budget(models.Model):
    name = models.CharField(max_length=255)
    tax = models.FloatField(null=True)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), related_name='budgetuser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lancamento(models.Model):
    lancamento = models.ForeignKey(Task, on_delete=models.CASCADE)
    amount = models.FloatField(default=0, null=True)
    amount2 = models.FloatField(default=0, null=True)
    amount3 = models.FloatField(default=0, null=True)
    amount4 = models.FloatField(default=0, null=True)
    amount5 = models.FloatField(default=0, null=True)
    amount6 = models.FloatField(default=0, null=True)
    amount7 = models.FloatField(default=0, null=True)
    amount8 = models.FloatField(default=0, null=True)
    amount9 = models.FloatField(default=0, null=True)
    amount10 = models.FloatField(default=0, null=True)
    amount11 = models.FloatField(default=0, null=True)
    amount12 = models.FloatField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lancamento.title
    

class Faturamento(models.Model):
    faturamentoorigem = models.ForeignKey(FaturamentoOrigem, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    amount = models.FloatField(default=0, null=True)
    amount2 = models.FloatField(default=0, null=True)
    amount3 = models.FloatField(default=0, null=True)
    amount4 = models.FloatField(default=0, null=True)
    amount5 = models.FloatField(default=0, null=True)
    amount6 = models.FloatField(default=0, null=True)
    amount7 = models.FloatField(default=0, null=True)
    amount8 = models.FloatField(default=0, null=True)
    amount9 = models.FloatField(default=0, null=True)
    amount10 = models.FloatField(default=0, null=True)
    amount11 = models.FloatField(default=0, null=True)
    amount12 = models.FloatField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.faturamentoorigem.origem



# class DateManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().all().annotate(month=ExtractMonth('date'), year=ExtractYear('date'), conc=Concat('year', V(" / "), 'month', output_field=CharField()))


class Expense(models.Model):
    expenseType = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    repetir = models.CharField(
        blank=False,
        max_length=30,
        choices=REPETIR,
        default=1
    )


class Revenue(models.Model):
    Revenue_origin = models.ForeignKey(FaturamentoOrigem, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    # date_obj = DateManager()
    # objects = models.Manager()
    repetir = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        choices=REPETIR,
    )


class Revenue2(models.Model):
    Revenue_origin = models.ForeignKey(FaturamentoOrigem, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    repetir = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        choices=REPETIR,
    )
