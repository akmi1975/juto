from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ob_tems(models.Model):
	kod = models.CharField(max_length=2, verbose_name='Код')
	name = models.CharField(max_length=100, verbose_name='Наименование')

	def __str__(self):
		return self.kod + ' - ' + self.name


	class Meta():
		verbose_name_plural = 'Темы обращений'
		verbose_name = 'Тема обращения'
		ordering = ['kod']

class ob_vopros(models.Model):
	kod_tems = models.ForeignKey(ob_tems, null=True,on_delete=models.PROTECT,verbose_name='Наименование темы')
	kod = models.CharField(max_length=5, verbose_name='Код')
	name = models.CharField(max_length=100, verbose_name='Наименование')

	def __str__(self):
		return self.name

	class Meta():
		verbose_name_plural = 'Вопросы обращений'
		verbose_name = 'Вопрос обращения'
		ordering = ['kod']	

# ===========================

class ob_list_tel_obr(models.Model):
	author = models.ForeignKey(User, null=True,on_delete=models.PROTECT	)
	#kod_tems = models.ForeignKey(ob_tems, null=True,on_delete=models.PROTECT,verbose_name='Наименование темы')
	vopros = models.ForeignKey(ob_vopros, null=True, on_delete=models.PROTECT)
	fio = models.CharField(max_length=150, verbose_name='ФИО')

	class Meta():
		verbose_name_plural = 'Список обращений'
		verbose_name = 'Обращениe'
		ordering = ['id']	
