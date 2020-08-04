from django.urls import path

from . import views

app_name = 'dex'
urlpatterns = [
    path('', views.IndexView, name = 'index'),
    path('lsb/', views.LeftSidebarView, name = 'left-sidebar'),
    path('rsb/', views.RightSidebarView, name = 'right-sidebar'),
    path('nsb/', views.NoSidebarView, name = 'no-sidebar'),
]
