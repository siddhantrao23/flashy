from django.urls import path

from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SetView.as_view(), name='set'),
    path('<int:set_id>/<int:card_id>/', views.CardView.as_view(), name='card'),
]
