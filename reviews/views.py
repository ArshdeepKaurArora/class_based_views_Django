from typing import Any
from django.shortcuts import render
from django.views import View
from .form import ReviewsForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import ReviewsModel

# Create your views here.

# class HomepageView(View):
#     """Create a homapage view for website. """
#     def get(self, request):
#         form = ReviewsForm()
#         return render(request, "reviews/homepage.html",{
#             'form': form
#         })
    
#     def post(self, request):
#         form = ReviewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect_path = reverse("thankyou")
#             return HttpResponseRedirect(redirect_path)
#         return render(request, "reviews/homepage.html", {
#             "form": form
#         })

# class HomepageView(FormView):
#     form_class = ReviewsForm
#     template_name = "reviews/homepage.html"
#     success_url = "thankyou"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class HomepageView(CreateView):
    """To return the homepage of website using Django class based view."""
    model = ReviewsModel
    form_class = ReviewsForm
    template_name = "reviews/homepage.html"
    success_url = "thankyou"


class ThankyouView(TemplateView):
    """Return the thank you page"""
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context
    
# class AllReviewsView(TemplateView):
#     """Return the webpage showing all reviews using Template View"""
#     template_name = "reviews/all_reviews.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = ReviewsModel.objects.all()
#         context["reviews"] = reviews
#         return context

class AllReviewsView(ListView):
    """To return a webpage with the list of all reviews."""
    template_name = "reviews/all_reviews.html"
    model = ReviewsModel
    context_object_name = "reviews"   #To change the name of variable passed to template

    def get_queryset(self):
        """To get a list of reviews with rating greater than 2."""
        query = super().get_queryset()
        selected_reviews = query.filter(rating__gt=2)
        return selected_reviews
    
# class ReviewDetailView(TemplateView):
#     """Return the webpage with review detail using TemplateView."""
#     template_name = "reviews/review_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         selected_review = ReviewsModel.objects.get(id=review_id)
#         context["review"] = selected_review
#         return context
    
    
class ReviewDetailView(DetailView):
    """Return detailed view of review using DetailView feature of Django""" 
    model = ReviewsModel
    template_name = "reviews/review_detail.html"
    context_object_name = 'review'
