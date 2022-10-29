from django.db import models

class Vaccination(models.Model):
    number = models.CharField(max_length=15, verbose_name='個体番号', blank=True, null=True)
    data = models.DateField('日付', blank=True, null=True)
    vaccination = models.CharField(max_length=255, verbose_name='接種ワクチン')
    hospitalid = models.CharField(max_length=255, verbose_name='病院ID', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Vaccination'

class MasterVaccination(models.Model):
    vaccination = models.CharField(max_length=255, verbose_name='接種ワクチン')

    class Meta:
        verbose_name_plural = 'MasterVaccination'

class User(models.Model):
    user_id = models.CharField(max_length=10, verbose_name='ユーザID')
    mc_number = models.CharField(max_length=15, verbose_name='個体番号')
    user_password = models.CharField(max_length=16, verbose_name='パスワード')
    user_birthday = models.DateField('生年月日')
    createdata = models.DateField('作成日付', blank=True, null=True)
    updatedata = models.DateField('最終更新日', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'User'
