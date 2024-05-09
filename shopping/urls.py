from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name=" Home"),
    path("why", views.why, name="Why_us"),
    path("shop", views.shop, name="Shop"),
    path("testimonial", views.testimonial, name="Testimonial"),
    path("contact", views.contact, name="Contact"),
]
