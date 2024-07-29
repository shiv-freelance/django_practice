from django.urls import path
from webapp.views import home_page, register


urlpatterns = [
    path("", view=home_page, name=""),
    path("register", view=register, name="register"),
]
