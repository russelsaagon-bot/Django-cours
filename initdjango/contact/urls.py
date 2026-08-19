from django.urls import path
from contact.views import contact_list, contact_add, contact_update, contact_delete

urlpatterns = [
    path('', contact_list, name="contact"),
    path('add/', contact_add, name="contact_add"),
    path('update/<int:pk>/', contact_update, name="contact_update"),
    path('delete/<int:pk>/', contact_delete, name="contact_delete"),
]
