from django.contrib import admin

# Register your models here.

from .models import thema_obr, them_obr, vid_kons, rez_kons, kod_oper, kod_rayon, base_obr

class ta_o_Admin(admin.ModelAdmin):
	list_display = ('kod', 'name')

class t_o_Admin(admin.ModelAdmin):
	list_display = ('kod_thema', 'kod', 'name')

class v_k_Admin(admin.ModelAdmin):
	list_display = ('kod', 'name')

class r_k_Admin(admin.ModelAdmin):
	list_display = ('kod', 'name')

class k_o_Admin(admin.ModelAdmin):
	list_display = ('kod', 'name')

class k_r_Admin(admin.ModelAdmin):
	list_display = ('kod', 'name')

class b_o_Admin(admin.ModelAdmin):
	list_display = ('author', 'date_obr', 'fio', 'snils', 'kod_thema', 'kod_them', 'kod_vid', 'kod_rez', 'kol_min', 'fio_oper', 'kod_oper', 'kod_word')
	list_per_page = 10
	class Meta:
		ordering = ['-date_obr']

admin.site.register(thema_obr, ta_o_Admin)
admin.site.register(them_obr, t_o_Admin)
admin.site.register(vid_kons, v_k_Admin)
admin.site.register(rez_kons, r_k_Admin)
admin.site.register(kod_oper, k_o_Admin)
admin.site.register(kod_rayon, k_r_Admin)
admin.site.register(base_obr, b_o_Admin)