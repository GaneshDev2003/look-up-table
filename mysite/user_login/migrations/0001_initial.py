# Generated by Django 2.2.12 on 2022-05-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='Eg. John')),
                ('user_age', models.TextField(default='0')),
                ('country', models.TextField(default='India')),
                ('company', models.TextField(default='Enter Company')),
                ('branch', models.TextField(default='Enter branch')),
                ('isEditor', models.BooleanField(default=False)),
            ],
        ),
    ]
