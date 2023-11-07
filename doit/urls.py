from django.urls import path

from . import views

app_name = 'doit'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:doit_item_id>/', views.detail, name="detail"),
    path('create/item/', views.create_item, name="create_item"),
    path('finish/<int:doit_item_id>', views.finish_item, name="finish"),
    path('delete/<int:doit_item_id>', views.delete_item, name="delete")
]
