# Generated by Django 2.2.12 on 2022-05-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='branch',
            field=models.TextField(default='CS'),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='company',
            field=models.TextField(default='IITM'),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='user_age',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='username',
            field=models.CharField(default='Eg. John', max_length=100),
        ),
    ]
