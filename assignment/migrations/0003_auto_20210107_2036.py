# Generated by Django 3.1.5 on 2021-01-07 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AddField(
            model_name='login',
            name='favourite',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='assignment.user'),
        ),
    ]
