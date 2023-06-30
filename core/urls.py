from django.urls import path,include
from core import views

urlpatterns = [
    path('', views.viewsIndex, name= 'index'),
    path('nosotros/', views.viewsNosotros, name= 'nosotros'),
]