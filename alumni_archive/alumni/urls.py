from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.homepage_view, name='homepage'),

    path('forgotpassword/', views.forgotpassword_view, name='forgotpassword'),
]