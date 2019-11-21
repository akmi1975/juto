from django.shortcuts import render
from django.http import HttpResponse	
from django import http
# Create your views here.

from django.views.generic.edit import CreateView

from .forms import b_o_Forms

from django.urls import reverse_lazy

from .models import base_obr, thema_obr, them_obr
from django.core.paginator import Paginator

#from django.core.cache import cache
#from django.contrib.auth import login,authenticate
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

import csv, datetime

user_adm = ['miha', 'DZHARAMAZA', 'GERGALVIK', 'BOTBOTKAI']


def index(request):
	#return HttpResponse("test")
	return render(request, 'test_index.html')

def del_stka(request, base_obr_id):
	d_bo = base_obr.objects.filter(pk=base_obr_id)
	d_bo.delete()
	return render(request, 'test_del.html')

# ----------------- export csv --------------------------------
def exp_csv(request):
	#print(request.user.groups.all()[0].id) request.user.groups.all()[0]

	user_csv = request.user.username

	if user_csv in user_adm:
		bos = base_obr.objects.all()
	else:
		bos = base_obr.objects.filter(author = request.user.id)

	response = HttpResponse(content_type='text/csv;charset=windows-1251')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	writer = csv.writer(response, delimiter=';')
	writer.writerow(['Дата', 'ФИО', 'СНИЛС', 'Тема', 'Вопрос', 'Вид','Результат', 'Время','Пользователь', 'Код оператора', 'Ключевое слово', 'Управление'])
	#b_o = []	
	for b in bos:
		b_o = str(b.date_obr).split('-')
		# ===========================================================
		#m_fio = b.fio_oper.split()
		#l_name = m_fio[0]
		#f_name = ' '.join(m_fio[1:])
		#ray_u = User.objects.get(last_name=l_name, first_name=f_name)
		ray_u = User.objects.get(pk=b.author_id)
		ray_ray = ray_u.groups.all()[0].name
		# ===========================================================
		writer.writerow([str(b_o[2] + '.' + b_o[1] + '.' + b_o[0]), b.fio, b.snils, b.kod_thema, b.kod_them, b.kod_vid, b.kod_rez, b.kol_min, b.fio_oper, b.kod_oper, b.kod_word, ray_ray])		
	return response
# ----------------- export csv --------------------------------

class AuthenticatedMixin(object):
	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponceForbidden()
		return super(AuthenticatedMixin, self).dispatch(request, *args, **kwargs)



class b_o_View(AuthenticatedMixin,CreateView):
	#cache.clear()
	form_class = b_o_Forms
	template_name = 'test_user.html'

	success_url = reverse_lazy('add')#reverse_lazy('index')

	#@method_decorator(login_required)
	def get_initial(self): # установка значений по умолчанию
		initial = super().get_initial()
		initial['author'] = self.request.user
		initial['fio_oper'] = self.request.user.last_name + ' ' + self.request.user.first_name
		initial['kod_oper'] = 2
		initial['kod_word'] = False
		#initial['snils'] = '000-000-000 00'
		initial['kol_min'] = 1
		try:
			initial['kod_thema'] = self.kwargs['thema']
		except:
			#initial['thema'] = 1
			pass

		return initial

	def get_context_data(self, **kwargs): # дополнительные поля для вывода 
		context = super().get_context_data(**kwargs)
		#print(self.request.user.username)
		bos = None
		user_m = self.request.user.username
		if user_m in user_adm:
			bos = base_obr.objects.all()
			#bos = base_obr.objects.filter(date_obr=datetime.datetime.date(datetime.datetime.now()))
		else:
			bos = base_obr.objects.filter(author = self.request.user.id)  #base_obr.objects.all()

		#context['bos'] = bos # - загрузка всего списка из базы данных
		# ----------------- paginator -------------------

		paginator = Paginator(bos, 5) # количество строк на экране
		if 'page' in self.request.GET:
			page_num = self.request.GET['page']
		else:
			page_num = 1
		page = paginator.get_page(page_num)
		context['page'] = page
		context['bos'] = page.object_list  # - загрузка по страничного списка из базы данных
		# ----------------- paginator -------------------
		context['thema_1'] = thema_obr.objects.all()

		try:
			context['thema_2'] = thema_obr.objects.filter(pk=self.kwargs['thema'])
		except Exception as e:
			pass
		return context

	def get_form_kwargs(self): # работа со списком тема
		kwargs = super().get_form_kwargs()
		try:
			kwargs['thema'] = self.kwargs['thema']
		except:
			pass
		return kwargs


