from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import PermissionDenied
from .models import BookingReview
from .forms import BookingReviewForm


class Index(View):
    """
    Renders homepage also showing the published reviews
    to all users.
    """
    template_name = 'reviews/index.html'

    def get(self, request, *args, **kwargs):
        """
        Shows the published reviews to all users.
        """
        review_form = BookingReviewForm()
        reviews = (
            BookingReview.objects.filter(status=1).order_by('-created_at')
        )
        context = {
            "review_form": review_form,
            "reviews": reviews
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Allows the user to submit a review, If the request method is POST
        the form will be saved as draft review only an superuser can publish
        the reviews. If the form is not valid it will render the index.html.
        """
        review_form = BookingReviewForm(request.POST)
        if request.method == "POST":
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review_success')

        context = {
            "review_form": review_form,
        }

        return render(request, self.template_name, context)


def view_all_draft_reviews(request):
    """
    Allows the admin to view all the draft reviews made,
    if they are not the superuser they will be redirected to the
    403 page.
    """
    if not request.user.is_superuser:
        raise PermissionDenied

    review_draft = (
            BookingReview.objects.filter(status=0).order_by('-created_at')
        )

    context = {
        "review_draft": review_draft,
    }

    return render(request, "reviews/view_all_draft_reviews.html", context)


def review_success(request):
    """
    Renders review-sucess.html
    """
    return render(request, 'reviews/review_success.html')
