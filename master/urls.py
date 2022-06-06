from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('masters', views.MasterViewSet)
router.register('category', views.CategoryViewSet)
urlpatterns = [
    path('nashi/', include(router.urls)),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('favorite/', views.UserAppointmentList.as_view()),
]
