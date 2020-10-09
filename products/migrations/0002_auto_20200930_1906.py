# Generated by Django 3.1 on 2020-09-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bonus',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_cost',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sales_comission',
            field=models.FloatField(null=True),
        ),
    ]
