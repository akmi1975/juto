from django.db import models

from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser

'''
class AdvUser(AbstractUser):
	is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Proshel activaciyu')
	send_messages = models.BooleanField(default=True)
	class Meta(AbstractUser.Meta):
		pass
'''
#from datetime import date

# https://ru.stackoverflow.com/questions/990082/%D0%9A%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%B2%D1%81%D0%B5-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F-%D0%BD%D0%B0-django
# Create your models here.

class thema_obr(models.Model):
	kod = models.CharField(max_length=2)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.kod + ' ' + self.name
	class Meta:
		verbose_name = 'Тема обращения'
		verbose_name_plural = 'Темы обращений'

class them_obr(models.Model):
	kod_thema = models.ForeignKey(thema_obr, null=True, on_delete=models.PROTECT)
	kod = models.CharField(max_length=5)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.kod + ' ' + self.name
	class Meta:
		verbose_name = 'Подтема обращения'
		verbose_name_plural = 'Подтемы обращений'

class vid_kons(models.Model):
	kod = models.CharField(max_length=2)
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.kod + " " + self.name
	
	class Meta:
		verbose_name_plural = 'Виды консультаций'
		verbose_name = 'Вид консультации'

class rez_kons(models.Model):
	kod = models.CharField(max_length=2)
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.kod + " " + self.name

	class Meta:
                verbose_name_plural = 'Результаты консультирования'
                verbose_name = 'Результат консультирования'

class kod_oper(models.Model):
	kod = models.CharField(max_length=2)
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.kod + " " + self.name
	class Meta:
                verbose_name_plural = 'Коды операторов'
                verbose_name = 'Код оператора'

class kod_rayon(models.Model):
	kod = models.CharField(max_length=2)
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.kod + " " + self.name



class base_obr(models.Model):
	author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
	date_obr = models.DateField(auto_now_add=True, null=True, verbose_name='Дата обращения')
	fio = models.CharField(max_length=150, null=True, verbose_name='ФИО гражданина')
	snils = models.CharField(max_length=14, null=True, verbose_name='СНИЛС')
	kod_word = models.BooleanField(null=True, verbose_name='Кодовое слово')
	#kod_rayon = models.ForeignKey(kod_rayon, null=True, on_delete=models.PROTECT) 
	kod_thema = models.ForeignKey(thema_obr, null=True, on_delete=models.PROTECT)
	kod_them = models.ForeignKey(them_obr, null=True, on_delete=models.PROTECT, verbose_name='Вопрос обращения')
	kod_vid = models.ForeignKey(vid_kons, null=True, on_delete=models.PROTECT, verbose_name='Вид консультации')
	kod_rez = models.ForeignKey(rez_kons, null=True, on_delete=models.PROTECT, verbose_name='Результат консультирования')
	kol_min = models.IntegerField(null=True, verbose_name='Продолжительность разговора')
	fio_oper = models.CharField(max_length=150, null=True, verbose_name='ФИО оператора')
	kod_oper = models.ForeignKey(kod_oper, null=True, on_delete=models.PROTECT, verbose_name='Код оператора')

	class Meta:
		#ordering = ['-date_obr']
		ordering = ['-id']
		verbose_name = 'База обращений'
		verbose_name_plural = 'База обращений'

