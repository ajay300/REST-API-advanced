# Generated by Django 4.0.3 on 2022-05-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(null=True),
        ),
    ]