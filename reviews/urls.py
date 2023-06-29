from django.urls import path

from . import views

urlpatterns = [
    path("",views.HomepageView.as_view(), name="homepage"),
    path("thankyou",views.ThankyouView.as_view(), name="thankyou"),
    path("all_reviews", views.AllReviewsView.as_view(), name="all_reviews"),
    path("review_detail/<int:pk>",views.ReviewDetailView.as_view(),name="review_detail")
]