from django.urls import path
from . import views

urlpatterns = (
    path('', views.dashboard, name="dashboard"),
    path('login/', views.l_login, name="login"),
    # path('logout/', views.logoutt, name='logout'),
    path('register/', views.reg_before, name='reg_before'),
    path('member/', views.member_page, name="member"),
    path('member_user/', views.member_user, name="member_user"),
    path('investor', views.investor_page, name="investor"),
    path('investor_user/', views.investor_user, name="investor_user"),
    path('startup/', views.startup_page, name="startup"),
    path('startup_user/', views.startup_user, name="startup_user"),
    path('startup/startup_form', views.startup_form, name="startup_form"),
    path('member/member_form', views.member_form, name="member_form"),
    path('investor/investor_form', views.investor_form, name="investor_form"),
    path('member_register/', views.member_register, name='mem_reg'),
    path('investor_register/', views.investor_register, name='inv_reg'),
    path('startup_register/', views.startup_register, name='sta_reg'),
    path('member_list/', views.member_list, name='member_list'),
    path('investor_list/', views.investor_list, name='investor_list'),
    path('startup_list/', views.startup_list, name='startup_list'),
)
