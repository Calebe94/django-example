from django.urls import path, include
from . import views
from .views import Another
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("", Another.as_view()),
    # path("first", views.first)
]
