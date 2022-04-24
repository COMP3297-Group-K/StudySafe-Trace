from django.db import router
from django.urls import path, include
from Trace import views

urlpatterns = [
    path('infected', views.ViewInfected.as_view()),
    path('venues', views.ViewVenuesAll.as_view()),
    path('contacts', views.ViewContactsAll.as_view()),
    path('venues/<str:hkuID>', views.ViewVenues.as_view(), name='venues-members'),
    path('contacts/<str:hkuID>', views.ViewContacts.as_view(), name='contacts-members'),
]