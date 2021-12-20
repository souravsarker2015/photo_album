from django.urls import path
from photo import views

urlpatterns = [

    path('gallery/', views.gallery, name='gallery'),
    path('view_photo/<str:pk>', views.view_photo, name='view_photo'),
    path('add/', views.add, name='add'),
]
