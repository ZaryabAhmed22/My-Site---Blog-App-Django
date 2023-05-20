from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # form based on Comment model
        exclude = ["post"]  # include all field except "post"
        labels = {  # setting custom label names
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comments"
        }
