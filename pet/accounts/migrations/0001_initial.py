# Generated by Django 3.2.7 on 2022-11-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username')),
                ('email', models.CharField(error_messages={'unique': 'A user with that email already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='email')),
                ('hospital_id', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='病院ID')),
                ('hospital_name', models.CharField(max_length=40, verbose_name='病院名')),
                ('address', models.CharField(max_length=120, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=12, verbose_name='電話番号')),
                ('director_name', models.CharField(max_length=40, verbose_name='責任者名')),
            ],
            options={
                'verbose_name_plural': 'HospitalUser',
            },
        ),
    ]
