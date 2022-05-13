# Generated by Django 4.0.3 on 2022-05-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('phone', models.IntegerField()),
                ('emp_id', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=23)),
            ],
        ),
    ]
