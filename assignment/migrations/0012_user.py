# Generated by Django 3.1.5 on 2021-01-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0011_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('favourite', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
