# Generated by Django 2.2.12 on 2022-05-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0005_auto_20220519_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
