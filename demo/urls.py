from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    path("", Another.as_view()),
]
