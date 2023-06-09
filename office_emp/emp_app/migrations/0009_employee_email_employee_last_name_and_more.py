# Generated by Django 4.2.1 on 2023-05-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0008_remove_employee_email_remove_employee_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
