# Generated by Django 3.1 on 2020-10-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0002_auto_20200930_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='repetir',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=30, null=True),
        ),
    ]
