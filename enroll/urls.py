
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from. import views



router = DefaultRouter()
router.register('enrolls', views.EnrollViewSet)

urlpatterns = [
    path('add/', include(router.urls)),
]