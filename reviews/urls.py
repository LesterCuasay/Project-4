from . import views
from django.urls import path


urlpatterns = [
    path(
        "success",
        views.review_success,
        name="review_success",
    ),
    path(
        "draft-reviews",
        views.view_all_draft_reviews,
        name="view_all_draft_reviews"
    ),
    path(
        "publish-reviews/<int:review_id>/",
        views.publish_reviews,
        name="publish_reviews"
    ),
]
