from django.db import models

class Dogcat(models.Model):
    number = models.IntegerField(max_length=255, verbose_name='個体番号', blank=True, null=True)
    data = models.DateField('日付', blank=True, null=True)
    vaccination = models.CharField(max_length=255, verbose_name='接種ワクチン')
    hospitalid = models.CharField(max_length=255, verbose_name='病院ID', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Dogcat'
