from django.shortcuts import render, redirect
from django.views import View
from .models import BookingReview
from .forms import BookingReviewForm


class Index(View):
    """
    Renders homepage also showing the published reviews
    to all users.
    """
    template_name = 'home/index.html'

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


def review_success(request):
    """
    Renders review-sucess.html
    """
    return render(request, 'reviews/review-success.html')
