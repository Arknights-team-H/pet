# Generated by Django 3.2.7 on 2022-10-31 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogcat', '0003_auto_20221028_1635'),
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
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.CharField(max_length=7, verbose_name='病院ID')),
                ('hospital_name', models.CharField(max_length=40, verbose_name='病院名')),
                ('address', models.CharField(max_length=120, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=12, verbose_name='電話番号')),
                ('director_name', models.CharField(max_length=40, verbose_name='責任者名')),
            ],
            options={
                'verbose_name_plural': 'Hospital',
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
                ('hospital_id', models.CharField(max_length=7, verbose_name='病院ID')),
                ('hospital_name', models.CharField(max_length=40, verbose_name='病院名')),
                ('address', models.CharField(max_length=120, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=12, verbose_name='電話番号')),
                ('director_name', models.CharField(max_length=40, verbose_name='責任者名')),
                ('password', models.CharField(max_length=16, verbose_name='パスワード')),
            ],
            options={
                'verbose_name_plural': 'MasterHospital',
            },
        ),
        migrations.CreateModel(
            name='MasterMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_id', models.CharField(max_length=11, verbose_name='ペットID')),
                ('pet_name', models.CharField(max_length=40, verbose_name='名前')),
                ('user_birthday', models.DateField(verbose_name='生年月日')),
                ('type', models.CharField(max_length=40, verbose_name='お薬情報')),
            ],
            options={
                'verbose_name_plural': 'MasterMedicine',
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, verbose_name='ユーザID')),
                ('mc_number', models.CharField(max_length=15, verbose_name='個体番号')),
                ('user_password', models.CharField(max_length=16, verbose_name='パスワード')),
                ('user_birthday', models.DateField(verbose_name='生年月日')),
                ('createdate', models.DateField(blank=True, null=True, verbose_name='作成日付')),
                ('updatedate', models.DateField(blank=True, null=True, verbose_name='最終更新日')),
            ],
            options={
                'verbose_name_plural': 'User',
            },
        ),
        migrations.RenameField(
            model_name='vaccination',
            old_name='number',
            new_name='mc_number',
        ),
        migrations.RemoveField(
            model_name='vaccination',
            name='data',
        ),
        migrations.RemoveField(
            model_name='vaccination',
            name='hospitalid',
        ),
        migrations.AddField(
            model_name='vaccination',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='接種日付'),
        ),
        migrations.AddField(
            model_name='vaccination',
            name='hospital_id',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='病院ID'),
        ),
        migrations.AlterField(
            model_name='mastervaccination',
            name='vaccination',
            field=models.CharField(max_length=40, verbose_name='ワクチン種類'),
        ),
        migrations.AlterField(
            model_name='vaccination',
            name='vaccination',
            field=models.CharField(max_length=40, verbose_name='接種ワクチン'),
        ),
    ]
