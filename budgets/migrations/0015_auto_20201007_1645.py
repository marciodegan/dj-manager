# Generated by Django 3.1 on 2020-10-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0014_auto_20201007_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue2',
            name='date',
            field=models.DateField(),
        ),
    ]
