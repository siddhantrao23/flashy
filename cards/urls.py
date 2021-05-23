from django.urls import path

from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:set_id>/<int:card_id>/', views.CardView.as_view(), name='card'),
    path('set_index/<int:set_id>', views.SetIndexView.as_view(), name='setIndex'),
    path('new_set', views.NewSetView.as_view(), name='newSet'),
    path('new_card/<int:set_id>', views.NewCardView.as_view(), name='newCard'),
]
