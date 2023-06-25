from . import views
from django.urls import path


urlpatterns = [
    path(
        "create",
        views.create_review,
        name="create_review",
    ),
    path(
        "success",
        views.review_success,
        name="review_success",
    ),
]
