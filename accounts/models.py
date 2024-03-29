from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

class MyUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta(AbstractUser.Meta):
        db_table = 'my_user'
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'

    username = models.CharField(verbose_name='ユーザ名',max_length=20)
    email = models.EmailField(verbose_name='メールアドレス')
    mc_number = models.CharField(max_length=15, verbose_name='個体番号',
                                 validators=[MinLengthValidator(15, '個体番号は15文字です。'),
                                             RegexValidator(r'^[0-9]*$', '数字のみを入力してください。')],
                                 )
    user_birthday = models.DateField(verbose_name='ユーザの生年月日')
    pet_id = models.CharField(max_length=11, verbose_name='ペットID')
    pet_name = models.CharField(max_length=40, verbose_name='ペットの名前')
    pet_birthday = models.DateField(verbose_name='ペットの生年月日')