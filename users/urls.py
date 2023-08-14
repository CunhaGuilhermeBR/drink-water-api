from django.urls import path,include
from .views.users_views import save, read, update, delete, read_id
from .views.entrys_views import drink_water, read_id_entrys, read_entrys

urlpatterns = [
    path('create', save),
    path('read', read),
    path('read/<str:id>', read_id),
    path('update/<str:id>', update),
    path('delete/<str:id>', delete),
    path('drink_water', drink_water),
    path('entrys_read', read_entrys),
    path('entrys_read/<str:id>', read_id_entrys),
  
]