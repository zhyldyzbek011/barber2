#
from django.urls import path

from rating import views


urlpatterns = [
    path("rating/", views.AddStarRatingView.as_view()),
    path('parsing/', views.ParsingView.as_view()),
]