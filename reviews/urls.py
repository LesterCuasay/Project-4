from . import views
from django.urls import path


urlpatterns = [
    path(
        "review_view",
        views.review_view,
        name="review_view",
    ),
    path(
        "success",
        views.review_success,
        name="review_success",
    ),
]
