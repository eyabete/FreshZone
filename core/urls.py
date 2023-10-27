from msilib.schema import AdminExecuteSequence
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from .forms import LoginForm
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', include('buy.urls', namespace='buy')),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.UserProfile, name='userprofile'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:index'), name='logout'),
]
