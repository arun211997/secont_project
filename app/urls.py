from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('show',views.show,name='show'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editfun/<int:pk>',views.editfun,name='editfun'),
    path('delete/<int:pk>',views.delete,name='delete')
]