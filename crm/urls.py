from django.urls import path
from django.contrib.auth.views import LoginView

from crm.views import (
    RegisterView, HomeView, ContactsView,
    CompaniesView, JobsView, CandidatesView, DealsView, ChatGPTView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', LoginView.as_view(template_name='sign-in.html'), name='signin'),
    # path('', SigninView.as_view(), name='signin'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('jobs/', JobsView.as_view(), name='jobs'),
    path('candidates/', CandidatesView.as_view(), name='candidates'),
    path('deals/', DealsView.as_view(), name='deals'),
    path('chatgpt/', ChatGPTView.as_view(), name='chatgpt'),
]



