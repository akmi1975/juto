from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from django.views.generic.edit import CreateView
from .forms import ob_list_tel_obr_Form
#from django.contrib.auth.models import User


class ob_list_tel_obr_Veiw(CreateView):
	template_name = "account/list_tel.html"
	from_class = ob_list_tel_obr_Form
	succes_url = "/dashboard/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#context['kod_tems'] = ob_tems.objects.all()
		context['vopros'] = ob_vopros.objects.all()
		return context



# Create your views here.

def index(request):
	return HttpResponse("<h1>test</h1>")
'''
def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request,
				username=cd['username'],
				password=cd['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse('Authenticated successfully')
			else:
				return HttpResponse('Disabled account')
		else:
			return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form': form})
'''

@login_required
def dashboard(request):
	#print(request.user.groups.all()[0])
	#print(request.user)
	return render(request,'account/dashboard.html',{'section': 'dashboard'})
