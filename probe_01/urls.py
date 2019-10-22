"""probe_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from base_obr.views import index, b_o_View, del_stka, exp_csv



#from base_obr.views import b_o_View

urlpatterns = [
    #path('', index, name='index'),
    path('', LoginView.as_view(), name='login'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', b_o_View.as_view(), name='add'),
    path('thema/<int:thema>/', b_o_View.as_view(), name='add_t'),
    #path('accounts/profile/<int:thema>/', b_o_View.as_view(), name='add_t'),
    path('del/<int:base_obr_id>/', del_stka),
    path('export/', exp_csv, name='exp'),
    path('admin/', admin.site.urls),



]



