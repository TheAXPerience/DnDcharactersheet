from django.urls import path

from . import views

app_name = 'cpage'
urlpatterns = [
  path('', views.index, name='index'),
  path('character/<int:character_id>/', views.character, name='char_page'),
  path('edit/<int:character_id>/', views.edit, name='char_edit'),
  path('create/', views.create, name='create'),
  path('edit/<int:character_id>/send/', views.send_edit, name='post'),
]
