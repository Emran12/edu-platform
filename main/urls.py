from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('courses/', views.course_list, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('about/', views.about, name='about'),

]
