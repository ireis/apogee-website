from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('search/', views.search, name='search'),
    path('<target_id>/', views.detail, name='detail'),
    path('<int:target_id>/neighbors/', views.neighbors, name='neighbors'),
]
