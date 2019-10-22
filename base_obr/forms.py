from django.forms import ModelForm
from django.forms import HiddenInput

from .models import base_obr

class b_o_Forms(ModelForm):
	class Meta:
		model = base_obr
		#fields = ('author','kod_them','kod_vid','kod_rez','kod_oper','fio')
		fields = ('author', 'fio', 'snils', 'kol_min', 'kod_word', 'kod_thema', 'kod_them', 'kod_vid', 'kod_rez', 'fio_oper', 'kod_oper')
		#exclude = ('author')
		widgets = {'author': HiddenInput(),
					'kod_thema': HiddenInput(),}

	def __init__(self, *args, **kwargs):
		thema = kwargs.pop('thema', None)
		super().__init__(*args, **kwargs)
		self.fields['kod_them'].queryset = self.fields['kod_them'].queryset.filter(kod_thema=thema)
		# http://qaru.site/questions/17369808/how-to-implement-a-dependent-drop-down-list-with-django-createview