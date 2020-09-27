from django.urls import path

from . import views

app_name = 'cpage'
urlpatterns = [
  path('', views.index, name='index'),
  path('page/<int:page>', views.page, name='page_no'),
  path('character/<int:character_id>/', views.character, name='char_page'),
  path('character/<int:character_id>/submit-edit', views.submit_edit, name='submit-edit'),
  path('character/<int:character_id>/submit-as', views.submit_as, name='submit-as'),
  path('character/<int:character_id>/submit-eq', views.submit_eq, name='submit-eq'),
  path('character/<int:character_id>/submit-sp', views.submit_sp, name='submit-sp'),
  path('edit/<int:character_id>/', views.edit, name='char_edit'),
  path('create/', views.create, name='create'),
  path('edit/<int:character_id>/send/', views.send_edit, name='post'),
]
