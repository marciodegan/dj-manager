# Generated by Django 3.1 on 2020-10-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_filelancamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='files/filebackup')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
    ]
