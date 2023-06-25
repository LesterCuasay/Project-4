from django.shortcuts import render
from .models import BookingReview
from .forms import BookingReviewForm


def create_review(request):
    if request.method == "POST":
        review_form = BookingReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review_success')

    else:
        review_form = BookingReviewForm()

    context = {
        "form": review_form,
    }

    return render(request, "index.html", context)


def review_success(request):
    return render(request, 'reviews/review-success.html')
