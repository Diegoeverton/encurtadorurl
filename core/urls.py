
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('val_link/', views.val_link, name='val_link'),
    path('/<str:link>', views.redirecionar, name='redirecionar')

]
