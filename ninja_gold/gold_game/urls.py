from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('place/<str:place>', views.process_money),
    path('win_condition', views.win_condition)


]