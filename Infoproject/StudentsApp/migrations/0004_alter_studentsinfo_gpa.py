# Generated by Django 4.0.5 on 2022-06-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentsApp', '0003_rename_birth_data_studentsinfo_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsinfo',
            name='GPA',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
