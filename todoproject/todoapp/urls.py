from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('deleteTask/<str:pk>/', deleteTask, name='deleteTask'),
	path('updateTask/<str:pk>/', updateTask, name='updateTask'),
]