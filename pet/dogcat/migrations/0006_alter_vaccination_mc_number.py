# Generated by Django 3.2.7 on 2022-11-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogcat', '0005_auto_20221101_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccination',
            name='mc_number',
            field=models.IntegerField(blank=True, max_length=15, null=True, verbose_name='個体番号'),
        ),
    ]
