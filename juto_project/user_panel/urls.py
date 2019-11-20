from django.urls import path
from .views import index, dashboard
from django.contrib.auth import views as auth_views
#from django.contrib.auth import logout
from .views import ob_list_tel_obr_Veiw

# path('logout/', auth_views.LogoutView.as_view(), name='logout'),

urlpatterns = [
    path('', index),
    #path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('dashboard/', dashboard, name='dashboard'),
	path('account/list_tel/', ob_list_tel_obr_Veiw.as_view(), name='list_tel' )

    
]
