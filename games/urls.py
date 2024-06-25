from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.CustomLoginView.as_view(), name='login'),
    path('game/list/', views.game_list, name='game_list'),
    path('inicial', views.inicial, name='inicial'),
    path('add/', views.add_game, name='add_game'),
    path('game/<int:pk>/edit/', views.game_update, name='game_update'),
    path('game/<int:pk>/delete/', views.game_delete, name='game_delete'),
    path('register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
