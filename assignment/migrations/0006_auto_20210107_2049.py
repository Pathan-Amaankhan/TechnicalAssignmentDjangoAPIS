# Generated by Django 3.1.5 on 2021-01-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0005_auto_20210107_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='favourite',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='assignment.user'),
        ),
    ]
