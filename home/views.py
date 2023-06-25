from django.shortcuts import render
from django.views import View


class Index(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        review_form = BookingReviewForm()
        context = {
            "review_form": review_form,
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


class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/menu.html')
