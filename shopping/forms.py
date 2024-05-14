from django import forms
from .models import Comment, Subscription


# contact infomation form the forms


# the contact form
class Contactform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "phone", "message"]

    # def clean_phone_number(self):
    # phone_number = self.cleaned_data.get('phone_number')
    # # Add your custom validation logic here
    # if not phone_number.startswith('+'):
    #     raise forms.ValidationError("Please enter a valid phone number (e.g., +1 123-456-7890)")
    # return phone_number


# the subscriptions form
class Subs(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"
