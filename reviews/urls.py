from . import views
from django.urls import path


urlpatterns = [
    path(
        "success",
        views.review_success,
        name="review_success",
    ),
]
