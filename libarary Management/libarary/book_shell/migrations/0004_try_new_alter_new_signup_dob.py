# Generated by Django 4.1 on 2023-01-17 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shell', '0003_alter_new_signup_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='try_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('passw', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='new_signup',
            name='dob',
            field=models.DateField(default=datetime.datetime(2023, 1, 17, 20, 18, 5, 416635)),
        ),
    ]
