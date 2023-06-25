from django.shortcuts import render


def review_success(request):
    return render(request, 'reviews/review-success.html')
