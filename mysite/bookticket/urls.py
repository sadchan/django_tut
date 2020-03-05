from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookticket, name='bookticket'),
]
