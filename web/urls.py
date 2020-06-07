from django.urls import path
from .views import index, sports, contact, about, details

urlpatterns = [
    path('', index, name="index"),
    path('sports/', sports, name="sports"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('details/', details, name="details")
]
