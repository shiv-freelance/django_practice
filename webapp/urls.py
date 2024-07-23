from django.urls import path
from webapp.views import home_page

urlpatterns = [
    path('', view=home_page, name=""),
]
