from django.db import models

class Vaccination(models.Model):
    mc_number = models.BigIntegerField(max_length=15, verbose_name='個体番号', blank=True, null=True)
    date = models.DateField('接種日付', blank=True, null=True)
    vaccination = models.CharField(max_length=40, verbose_name='接種ワクチン')
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Vaccination'

class MasterVaccination(models.Model):
    vaccination = models.CharField(max_length=40, verbose_name='ワクチン種類')

    class Meta:
        verbose_name_plural = 'MasterVaccination'

class User(models.Model):
    user_id = models.CharField(max_length=10, verbose_name='ユーザID')
    mc_number = models.CharField(max_length=15, verbose_name='個体番号')
    user_password = models.CharField(max_length=16, verbose_name='パスワード')
    user_birthday = models.DateField('生年月日')
    createdate = models.DateField('作成日付', blank=True, null=True)
    updatedate = models.DateField('最終更新日', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'User'

class MasterHospital(models.Model):
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID')
    hospital_name = models.CharField(max_length=40, verbose_name='病院名')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number = models.CharField(max_length=12, verbose_name='電話番号')
    director_name = models.CharField(max_length=40, verbose_name='責任者名')
    password = models.CharField(max_length=16, verbose_name='パスワード')

    class Meta:
        verbose_name_plural = 'MasterHospital'

class Hospital(models.Model):
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID')
    hospital_name = models.CharField(max_length=40, verbose_name='病院名')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number = models.CharField(max_length=12, verbose_name='電話番号')
    director_name = models.CharField(max_length=40, verbose_name='責任者名')

    class Meta:
        verbose_name_plural = 'Hospital'

class MasterMedicine(models.Model):
    pet_id = models.CharField(max_length=11, verbose_name='ペットID')
    pet_name = models.CharField(max_length=40, verbose_name='名前')
    user_birthday = models.DateField('生年月日')
    type = models.CharField(max_length=40, verbose_name='お薬情報')

    class Meta:
        verbose_name_plural = 'MasterMedicine'

class Medicine(models.Model):

    pet_id = models.CharField(max_length=11, verbose_name='ペットID')
    taking_date = models.DateField('飲んだ日付け')
    create_date = models.DateField('作成日付', blank=True, null=True)
    update_date = models.DateField('最終更新日', blank=True, null=True)
    taking1 = models.CharField(max_length=40, verbose_name='飲んだ薬①')
    taking2 = models.CharField(max_length=40, verbose_name='飲んだ薬②')
    taking3 = models.CharField(max_length=40, verbose_name='飲んだ薬③')
    class Meta:
        verbose_name_plural = 'Medicine'

class LoginHistory(models.Model):

    login = models.DateField('ログイン日', blank=True, null=True)
    login_limit = models.DateField('ログインの有効期限', blank=True, null=True)
    logout_flag = models.CharField(max_length=1, verbose_name='ログアウトフラグ')
    distinction_flag = models.CharField(max_length=1, verbose_name='一般、病院判別フラグ')

    class Meta:
        verbose_name_plural = 'LoginHistory'

class AlarmHistory(models.Model):

    issue = models.DateField('発行日', blank=True, null=True)
    issue_limit = models.DateField('発行期限', blank=True, null=True)
    alarm_content = models.CharField(max_length=40, verbose_name='アラート内容')

    class Meta:
        verbose_name_plural = 'AlarmHistory'

class QRcodeHistory(models.Model):

    issue = models.DateField('発行日', blank=True, null=True)
    issue_limit = models.DateField('発行期限', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'QRcodeHistory'
