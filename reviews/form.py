from django import forms
from .models import ReviewsModel

class ReviewsForm(forms.ModelForm):
    """Create a form for collecting reviews"""
    class Meta:
        """To add special features of form"""
        model = ReviewsModel
        fields = "__all__"
        labels = {
            "username": "Your name",
            "review": "Your review",
            "rating": "Your rating"
        }
        errors = {
            "username": {
                "required" : "This field is mendatory.",
                "max_length" : "Please write shorter name."
            }
        }
