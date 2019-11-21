from django.contrib import admin
from .models import ob_tems, ob_vopros, ob_list_tel_obr
# Register your models here.

class ob_tems_admin(admin.ModelAdmin):
	list_display = ('kod', 'name')
	list_display_links = ('kod', 'name')
	search_fields = ('kod', 'name',)

class ob_vopros_admin(admin.ModelAdmin):
	list_display = ('kod_tems', 'kod', 'name')
	list_display_links = ('kod_tems', 'kod', 'name')
	search_fields = ('kod', 'name',)

class ob_list_tel_obr_admin(admin.ModelAdmin):
	list_display = ('author', 'vopros', 'fio')
	list_display_links = ('author', 'vopros', 'fio')
	search_fields = ('vopros',)


admin.site.register(ob_tems, ob_tems_admin)
admin.site.register(ob_vopros, ob_vopros_admin)
admin.site.register(ob_list_tel_obr, ob_list_tel_obr_admin)