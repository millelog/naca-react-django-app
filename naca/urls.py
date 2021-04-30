from django.urls import path
from . import views

urlpatterns = [
    path('api/address/', views.AddressListCreate.as_view()),
]
