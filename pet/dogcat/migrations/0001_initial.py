# Generated by Django 3.2.7 on 2022-11-14 07:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.DateField(blank=True, null=True, verbose_name='発行日')),
                ('issue_limit', models.DateField(blank=True, null=True, verbose_name='発行期限')),
                ('alarm_content', models.CharField(max_length=40, verbose_name='アラート内容')),
            ],
            options={
                'verbose_name_plural': 'AlarmHistory',
            },
        ),
        migrations.CreateModel(
            name='HospitalApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=40, verbose_name='病院名')),
                ('address', models.CharField(max_length=120, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=12, verbose_name='電話番号')),
                ('director_name', models.CharField(max_length=40, verbose_name='責任者名')),
                ('licence_copy', models.ImageField(upload_to='', verbose_name='獣医師免許写し')),
            ],
            options={
                'verbose_name_plural': 'HospitalApply',
            },
        ),
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.DateField(blank=True, null=True, verbose_name='ログイン日')),
                ('login_limit', models.DateField(blank=True, null=True, verbose_name='ログインの有効期限')),
                ('logout_flag', models.CharField(max_length=1, verbose_name='ログアウトフラグ')),
                ('distinction_flag', models.CharField(max_length=1, verbose_name='一般、病院判別フラグ')),
            ],
            options={
                'verbose_name_plural': 'LoginHistory',
            },
        ),
        migrations.CreateModel(
            name='MasterHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=40, verbose_name='病院名')),
                ('address', models.CharField(max_length=120, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=12, verbose_name='電話番号')),
                ('director_name', models.CharField(max_length=40, verbose_name='責任者名')),
            ],
            options={
                'verbose_name_plural': 'MasterHospital',
            },
        ),
        migrations.CreateModel(
            name='MasterHospitalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.CharField(max_length=7, verbose_name='病院ID')),
                ('password', models.CharField(max_length=16, verbose_name='パスワード')),
            ],
            options={
                'verbose_name_plural': 'Hospital',
            },
        ),
        migrations.CreateModel(
            name='MasterMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, verbose_name='お薬情報')),
            ],
            options={
                'verbose_name_plural': 'MasterMedicine',
            },
        ),
        migrations.CreateModel(
            name='MasterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, verbose_name='ユーザID')),
                ('mc_number', models.CharField(max_length=15, verbose_name='個体番号')),
                ('user_password', models.CharField(max_length=16, verbose_name='パスワード')),
                ('user_birthday', models.DateField(verbose_name='ユーザの生年月日')),
                ('pet_id', models.CharField(max_length=11, verbose_name='ペットID')),
                ('pet_name', models.CharField(max_length=40, verbose_name='名前')),
                ('pet_birthday', models.DateField(verbose_name='ペットの生年月日')),
                ('createdate', models.DateField(blank=True, null=True, verbose_name='作成日付')),
                ('updatedate', models.DateField(blank=True, null=True, verbose_name='最終更新日')),
            ],
            options={
                'verbose_name_plural': 'MasterUser',
            },
        ),
        migrations.CreateModel(
            name='MasterVaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccination_type', models.CharField(max_length=40, verbose_name='ワクチン種類')),
            ],
            options={
                'verbose_name_plural': 'MasterVaccination',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_id', models.CharField(max_length=11, verbose_name='ペットID')),
                ('taking_date', models.DateField(verbose_name='飲んだ日付け')),
                ('create_date', models.DateField(blank=True, null=True, verbose_name='作成日付')),
                ('update_date', models.DateField(blank=True, null=True, verbose_name='最終更新日')),
                ('taking1', models.CharField(max_length=40, verbose_name='飲んだ薬①')),
                ('taking2', models.CharField(max_length=40, verbose_name='飲んだ薬②')),
                ('taking3', models.CharField(max_length=40, verbose_name='飲んだ薬③')),
            ],
            options={
                'verbose_name_plural': 'Medicine',
            },
        ),
        migrations.CreateModel(
            name='QRcodeHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.DateField(blank=True, null=True, verbose_name='発行日')),
                ('issue_limit', models.DateField(blank=True, null=True, verbose_name='発行期限')),
            ],
            options={
                'verbose_name_plural': 'QRcodeHistory',
            },
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mc_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='個体番号')),
                ('date', models.DateField(default=datetime.datetime(2022, 11, 14, 7, 44, 2, 371388, tzinfo=utc), verbose_name='接種日付')),
                ('hospital_id', models.CharField(blank=True, max_length=7, null=True, verbose_name='病院ID')),
                ('vaccination_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dogcat.mastervaccination', verbose_name='接種ワクチン')),
            ],
            options={
                'verbose_name_plural': 'Vaccination',
            },
        ),
    ]
