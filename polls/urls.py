from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('search/', views.search, name='search'),
    path('<target_id>/', views.detail, name='detail'),
    # ex: /polls/5/neighbors/
    path('<int:target_id>/neighbors/', views.neighbors, name='neighbors'),
]
