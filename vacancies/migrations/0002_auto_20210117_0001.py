# Generated by Django 3.1.5 on 2021-01-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='published',
            field=models.DateField(),
        ),
    ]
