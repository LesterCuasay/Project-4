from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
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
        if request.method == "POST":
            review_form = BookingReviewForm(request.POST)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review.save()

                messages.success(request, "Review submitted!")
                return redirect('review_success')

        else:
            review_form = BookingReviewForm

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


def publish_reviews(request, review_id):
    """
    Allows the admin to publish draft reviews from the
    view all draft reviews html if they are not the superuser
    they will be redirected to the 403 page.
    """
    if not request.user.is_superuser:
        raise PermissionDenied

    review_publish = get_object_or_404(BookingReview, id=review_id)

    if request.method == "POST":

        review_publish.status = 1
        review_publish.save()

        send_review_confirmation_email(review_publish)

        messages.success(request, "Review published!")
        return redirect('view_all_draft_reviews')

    else:
        review_form = BookingReviewForm(instance=review_publish)

    context = {
        "review_publish": review_publish,
    }

    return render(request, "reviews/publish_review.html", context)


def delete_reviews(request, review_id):
    """
    Allows the admin to delete published/draft reviews,
    if they are not the superuser they will be redirected
    to the 403 page.
    """
    if not request.user.is_superuser:
        raise PermissionDenied

    review_delete = get_object_or_404(BookingReview, id=review_id)

    if request.method == "POST":
        review_delete.delete()

        messages.error(request, "Review deleted!")
        return redirect('view_all_draft_reviews')

    context = {
        "review_delete": review_delete
    }

    return render(request, "reviews/delete_review.html", context)


def review_success(request):
    """
    Renders review-sucess.html
    """
    return render(request, 'reviews/review_success.html')


def send_review_confirmation_email(review_publish):
    """
    When a review is published by the admin, the user will recieve
    an email containing the content of the completed form.
    The email template sent will be the html version, but if
    it cannot be rendered it will render the txt file instead.
    """

    subject = "Review Published"
    text_template = "reviews/review_confirmation_email.txt"
    html_template = "reviews/review_confirmation_email.html"

    context = {
        'service_rating': review_publish.service_rating,
        'food_rating': review_publish.food_rating,
        'overall_rating': review_publish.overall_rating,
        'comment': review_publish.comment,
        'author': review_publish.author
    }

    text_content = render_to_string(text_template, context)
    html_content = render_to_string(html_template, context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[review_publish.email],
    )

    email.attach_alternative(html_content, 'text/html')

    email.send()
