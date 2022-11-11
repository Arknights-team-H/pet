from django.db import models
from django.utils import timezone

class MasterVaccination(models.Model): # 予防接種種類のマスタテーブル
    vaccination_type = models.CharField(max_length=40, verbose_name='ワクチン種類')

    def __str__(self):
        return self.vaccination_type
    class Meta:
        verbose_name_plural = 'MasterVaccination'


class Vaccination(models.Model): # 病院側の予防接種情報登録テーブル
    mc_number = models.CharField(max_length=15, verbose_name='個体番号', blank=True, null=True)
    date = models.DateField(verbose_name='接種日付', default=timezone.now())
    vaccination_type = models.ForeignKey(MasterVaccination, on_delete=models.DO_NOTHING, verbose_name='接種ワクチン')
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Vaccination'


class MasterUser(models.Model): # 一般ユーザ側アプリのユーザ情報テーブル
    user_id = models.CharField(max_length=10, verbose_name='ユーザID')
    mc_number = models.CharField(max_length=15, verbose_name='個体番号')
    user_password = models.CharField(max_length=16, verbose_name='パスワード')
    user_birthday = models.DateField('ユーザの生年月日')
    pet_id = models.CharField(max_length=11, verbose_name='ペットID')
    pet_name = models.CharField(max_length=40, verbose_name='名前')
    pet_birthday = models.DateField('ペットの生年月日')
    createdate = models.DateField('作成日付', blank=True, null=True)
    updatedate = models.DateField('最終更新日', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'MasterUser'

class MasterHospital(models.Model): # 病院情報のマスタテーブル
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID')
    hospital_name = models.CharField(max_length=40, verbose_name='病院名')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number = models.CharField(max_length=12, verbose_name='電話番号')
    director_name = models.CharField(max_length=40, verbose_name='責任者名')

    class Meta:
        verbose_name_plural = 'MasterHospital'

class Hospital(models.Model): # 病院側の病院情報テーブル
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID')
    password = models.CharField(max_length=16, verbose_name='パスワード')
    male_address = models.CharField(max_length=255, verbose_name='メールアドレス')

    class Meta:
        verbose_name_plural = 'Hospital'

class MasterMedicine(models.Model): # 一般ユーザ側のお薬情報マスタテーブル
    type = models.CharField(max_length=40, verbose_name='お薬情報')

    class Meta:
        verbose_name_plural = 'MasterMedicine'

class Medicine(models.Model): # 一般ユーザ側のお薬情報テーブル

    pet_id = models.CharField(max_length=11, verbose_name='ペットID')
    taking_date = models.DateField('飲んだ日付け')
    create_date = models.DateField('作成日付', blank=True, null=True)
    update_date = models.DateField('最終更新日', blank=True, null=True)
    taking1 = models.ForeignKey(MasterMedicine, on_delete=models.DO_NOTHING, verbose_name='飲んだ薬①')
    taking2 = models.ForeignKey(MasterMedicine, on_delete=models.DO_NOTHING, verbose_name='飲んだ薬②')
    taking3 = models.ForeignKey(MasterMedicine, on_delete=models.DO_NOTHING, verbose_name='飲んだ薬③')
    class Meta:
        verbose_name_plural = 'Medicine'

class LoginHistory(models.Model): # ログイン判別テーブル

    login = models.DateField('ログイン日', blank=True, null=True)
    login_limit = models.DateField('ログインの有効期限', blank=True, null=True)
    logout_flag = models.CharField(max_length=1, verbose_name='ログアウトフラグ')
    distinction_flag = models.CharField(max_length=1, verbose_name='一般、病院判別フラグ')

    class Meta:
        verbose_name_plural = 'LoginHistory'

class AlarmHistory(models.Model): # 一般ユーザ側のアラートテーブル

    issue = models.DateField('発行日', blank=True, null=True)
    issue_limit = models.DateField('発行期限', blank=True, null=True)
    alarm_content = models.CharField(max_length=40, verbose_name='アラート内容')

    class Meta:
        verbose_name_plural = 'AlarmHistory'

class QRcodeHistory(models.Model): # 一般ユーザ側のQRコード発行テーブル

    issue = models.DateField('発行日', blank=True, null=True)
    issue_limit = models.DateField('発行期限', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'QRcodeHistory'
