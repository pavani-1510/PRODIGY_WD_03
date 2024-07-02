# tictactoe_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_game, name='new_game'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('move/<int:game_id>/<int:position>/', views.make_move, name='make_move'),
]
