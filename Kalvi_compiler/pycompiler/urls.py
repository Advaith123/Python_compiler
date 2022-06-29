
from django.urls import path, include
# import views
from . import views

urlpatterns = [
    path('', views.index, name='indexpage'),
    path('scratch', views.scratch, name='scratch'),
    path('runcode', views.runcode, name='runcode'),
]
