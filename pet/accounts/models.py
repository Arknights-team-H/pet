from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class HospitalUserManager(BaseUserManager):
    def create_user(self, hospital_id, password=None):
        if not hospital_id:
            raise ValueError('Users must have an hospital_id address')

        Hospitaluser = self.model(
            hospital_id=self.normalize_hospital_id(hospital_id),
        )

        Hospitaluser.set_password(password)
        Hospitaluser.save(using=self._db)
        return Hospitaluser

class HospitalUser(AbstractBaseUser):
    """拡張ユーザーモデル"""
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.CharField(
        'email',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that email already exists.",
        },
    )
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID',primary_key=True)
    hospital_name = models.CharField(max_length=40, verbose_name='病院名')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number = models.CharField(max_length=12, verbose_name='電話番号')
    director_name = models.CharField(max_length=40, verbose_name='責任者名')

    #ログインの際にユーザー名の代わりとして入力する項目
    USERNAME_FIELD = 'hospital_id'

    #紐づけ
    objects = HospitalUserManager()

    #管理者画面に一覧表示する際の表示する項目名
    def __str__(self):
        return self.hospital_id



    class Meta:
        verbose_name_plural = 'HospitalUser'