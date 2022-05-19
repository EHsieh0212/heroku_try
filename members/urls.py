from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),

    #SSO login/logout
    #path('saml/login', views.login_user2, name='saml/login'),
    #path('saml/logout', views.logout_user2, name='saml/logout'),
]
