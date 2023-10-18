from django.urls import path
from .views import ContactAdd, ContactList, ContactView

urlpatterns = [
    path('contact/add/', ContactAdd.as_view(), name = 'contact_add'),
    path('', ContactList.as_view(), name = 'contact_list'),
    path('contact/view/', ContactView.as_view(), name = 'contact_view'),
]