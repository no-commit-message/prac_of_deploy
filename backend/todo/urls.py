from .views import TodoViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls))
]