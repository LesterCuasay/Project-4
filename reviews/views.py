from django.shortcuts import render, redirect
from django.views import View
from .models import BookingReview
from .forms import BookingReviewForm


class Index(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        review_form = BookingReviewForm()
        reviews = BookingReview.objects.all()
        context = {
            "review_form": review_form,
            "reviews": reviews
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
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
    return render(request, 'reviews/review-success.html')
