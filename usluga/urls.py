from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('nashi', views.Nashi_UslugiViewSet)

urlpatterns = [
    path('uslugi/', include(router.urls))
]
