# Generated by Django 3.1.5 on 2021-01-07 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_auto_20210107_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='favourite',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='assignment.user'),
        ),
    ]
