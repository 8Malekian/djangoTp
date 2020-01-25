from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('liste/',views.liste,name='liste'),
    path('detail/<int:pk>',views.detail,name='detail'),
]