from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', views.home, name='home'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipos/nuevo/', views.crear_equipo, name='crear_equipo'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", csrf_exempt(auth_views.LogoutView.as_view(next_page="home")), name="logout"),
]
