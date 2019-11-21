from django import forms
from django.forms import ModelForm

from .models import ob_list_tel_obr




class ob_list_tel_obr_Form(ModelForm):
	class Meta:
		model = ob_list_tel_obr
		fields = ('author','vopros','fio')


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)