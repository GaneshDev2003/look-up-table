# Generated by Django 2.2.12 on 2022-05-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0002_auto_20220517_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
