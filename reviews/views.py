from django.shortcuts import render
from .models import BookingReview


def create_review(request):
    if request.method == "POST":
        author = request.user
        email = request.POST['email']
        comment = request.POST['comment']

    review = BookingReview(
        author=author,
        email=email,
        comment=comment,
    )

    return render('review_success')


def review_success(request):
    return render(request, 'reviews/review-success.html')
