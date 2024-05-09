from django import forms
from .models import Comment, Subscription


# contact infomation form the forms


# the contact form
class Contactform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "phone", "message"]


# the subscriptions form
class Subs(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"
