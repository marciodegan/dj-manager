# Generated by Django 3.1 on 2020-10-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200930_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ref',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='buyprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='salesprice',
            field=models.FloatField(null=True),
        ),
    ]
