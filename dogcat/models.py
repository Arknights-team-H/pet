from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

class MasterVaccination(models.Model): # 予防接種種類マスタテーブル
    vaccination_type = models.CharField(max_length=40, verbose_name='ワクチン種類')
    def __str__(self):
        return self.vaccination_type
    class Meta:
        verbose_name_plural = 'MasterVaccination'


class MasterGender(models.Model): # 性別マスタテーブル
    gender = models.CharField(max_length=2, verbose_name='性別')
    def __str__(self):
        return self.gender
    class Meta:
        verbose_name_plural = 'MasterGender'


class Vaccination(models.Model): # 予防接種情報テーブル
    mc_number = models.CharField(max_length=15,verbose_name='個体番号',
                                 validators=[MinLengthValidator(15,'個体番号は15文字です。'),
                                             RegexValidator(r'^[0-9]*$', '数字のみを入力してください。')],
                                 )
    date = models.DateField(verbose_name='接種日付', default=timezone.now())
    vaccination_type = models.ForeignKey(MasterVaccination, on_delete=models.DO_NOTHING, verbose_name='接種ワクチン')
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID',
                                   validators=[MinLengthValidator(7,'病院IDは7文字です。'),
                                               RegexValidator(r'^[0-9]*$', '数字のみを入力してください。')]
                                   )
    owner_name = models.CharField(max_length=100, verbose_name='飼い主名')
    owner_address = models.CharField(max_length=255, verbose_name='住所')
    pet_name = models.CharField(max_length=100, verbose_name='ペット名')
    species = models.CharField(max_length=30, verbose_name='種別')
    gender = models.ForeignKey(MasterGender, on_delete=models.DO_NOTHING, verbose_name='性別')

    class Meta:
        verbose_name_plural = 'Vaccination'


class MasterHospital(models.Model): # 病院情報マスタテーブル
    hospital_name = models.CharField(max_length=40, verbose_name='病院名')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number = models.CharField(max_length=12, verbose_name='電話番号')
    director_name = models.CharField(max_length=40, verbose_name='責任者名')

    class Meta:
        verbose_name_plural = 'MasterHospital'


class HospitalApply(models.Model): # 病院側利用申請テーブル
    hospital_name = models.CharField(max_length=40, verbose_name='病院名')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number = models.CharField(max_length=12, verbose_name='電話番号',
                                    validators=[RegexValidator(r'^[0-9]*$', '数字のみを入力してください。')])
    director_name = models.CharField(max_length=40, verbose_name='責任者名')
    licence_copy = models.ImageField(verbose_name='獣医師免許写し')

    class Meta:
        verbose_name_plural = 'HospitalApply'

class MasterHospitalUser(models.Model): # 病院ユーザ情報マスタテーブル
    hospital_id = models.CharField(max_length=7, verbose_name='病院ID')
    password = models.CharField(max_length=256, verbose_name='パスワード')

    class Meta:
        verbose_name_plural = 'Hospital'


class MasterMedicine(models.Model): # お薬情報マスタテーブル
    medicine_type = models.CharField(max_length=40, verbose_name='お薬情報')
    def __str__(self):
        return self.medicine_type

    class Meta:
        verbose_name_plural = 'MasterMedicine'

class Medicine(models.Model): # お薬情報テーブル

    pet_id = models.CharField(max_length=11, verbose_name='ペットID')
    taking_date = models.DateField('飲む日付')
    create_date = models.DateField('作成日付', blank=True, default=timezone.now())
    update_date = models.DateField('最終更新日', blank=True, null=True)
    medicine_type = models.ForeignKey(MasterMedicine, on_delete=models.DO_NOTHING, verbose_name='服用薬')
    class Meta:
        verbose_name_plural = 'Medicine'

class QRcodeHistory(models.Model): # QRコード履歴テーブル

    issue = models.DateField('発行日', blank=True, null=True)
    issue_limit = models.DateField('発行期限', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'QRcodeHistory'
