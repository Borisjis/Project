from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import increase_counter
from .views import contact_form



urlpatterns = [
    path('', views.my_default_view, name='default_view'),
    path('financial-planning/', views.financial_planning, name='financial_planning'),
    path('reports-and-analytics/', views.reports_and_analytics, name='reports_and_analytics'),
    path('account-settings/', views.account_settings, name='account_settings'),
    path('support/', views.support, name='support'),
    path('register/', views.register, name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.my_default_view, name='home'),
    path('expense-list/', views.expense_list, name='expense_list'),  
    path('news1.html', views.news1_view, name='news1'), 
    path('news2.html', views.news2_view, name='news2'), 
    path('news3.html', views.news3_view, name='news3'), 
    path('news4.html', views.news4_view, name='news4'), 
    path('news5.html', views.news5_view, name='news5'), 
    path('news6.html', views.news6_view, name='news6'), 
    path('news7.html', views.news7_view, name='news7'), 
    path('news8.html', views.news8_view, name='news8'), 
    path('news9.html', views.news9_view, name='news9'), 
    path('news10.html', views.news10_view, name='news10'), 
    path('increase_counter/', increase_counter, name='increase_counter'),
    path('contact/', contact_form, name='contact_form'),
    path('finance_resources/', views.finance_resources, name='finance_resources'),
    path('tax_calculator/', views.tax_calculator, name='tax_calculator'),
    path('finance_resources/economy_tips.html', views.economy_tips_view, name='economy_tips'),
    path('review/', views.review_form, name='review_form'),
    path('capital/', views.capital, name='capital'),
    path('finance_resources/investment_tips.html', views.investment_tips_view, name='investment_tips'),
    path('finance_resources/investment2_tips.html', views.investment2_tips_view, name='investment2_tips'),

]
    
