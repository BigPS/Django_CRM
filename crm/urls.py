from django.urls import path

from crm import views

urlpatterns = [
    path('', views.signin, name="sign-in"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('companies/', views.companies, name='companies'),
    path('jobs/', views.jobs, name='jobs'),
    path('candidates/', views.candidates, name='candidates'),
    path('deals/', views.deals, name='deals'),
    path('chatgpt/', views.chatgpt, name='chatgpt'),
]