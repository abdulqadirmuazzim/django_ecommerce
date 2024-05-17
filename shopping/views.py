from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Subscription, product
from .forms import Contactform, Subs
import re

# Create your views here.


def landing(req):
    if req.method == "POST":
        if "contact" in req.POST:
            # get the fields
            name = req.POST["name"]
            email = req.POST["email"]
            phone = req.POST["phone"]
            message = req.POST["message"]

            form = Contactform(req.POST)

            if form.is_valid():
                # save to the database
                form.save()
                # flash a success message
                messages.success(req, "Form Submitted")
                # send email
                return render(req, "index.html")
            else:
                # get the value of the fields
                # pass them in to our templates
                messages.error(req, "There is a problem with you form scroll down")
                return render(
                    req,
                    "index.html",
                    {
                        "name": name,
                        "email": email,
                        "message": message,
                        "phone": phone,
                        "cont_err": form.errors.values(),
                    },
                )
        if "subscribe" in req.POST:
            sub_model = Subscription
            objects = sub_model.objects.all()
            subcrip = Subs(req.POST)

            email = req.POST["email"]

            # if the person has already subscribed then send an error
            if email in [a.email for a in objects]:
                # Add an error to the error list so it Doesn't validate
                subcrip.add_error("email", "You have already subscribed")
                messages.error(req, 'There is a problem with this email')

                # render the template back with the error messages
                return render(req, "index.html", {"form_err": subcrip.errors.values()})

            elif subcrip.is_valid():
                subcrip.save()
                messages.success(req, "You have successfully subscribed")
                send_mail(
                    "Thanks for Subscribing",
                    f"Dear {email}, you have subscribed to our news letter, thanks for subscribing",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return render(req, "index.html")
            else:
                messages.error(req, "Could not subscribe!")
                return render(req, "index.html", {"err_mail": email})

    return render(req, "index.html")


def shop(req):
    if req.method == "POST":

        subcrip = Subs(req.POST)
        email = req.POST["email"]
        sub_model = Subscription
        objects = sub_model.objects.all()

        if email in [a.email for a in objects]:
            subcrip.add_error("email", "You have already subscribed")

            return render(req, "shop.html", {"form_err": subcrip.errors.values()})

        if subcrip.is_valid():
            subcrip.save()
            messages.success(req, "You have successfully subscribed")
            send_mail(
                "Thanks for Subscribing",
                f"Dear {email} thanks for subscribing",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return redirect("Shop")
        else:
            messages.error(req, "Could not subscribe!")
            return render(req, "shop.html", {"err_mail": email})

    return render(req, "shop.html")


def testimonial(req):
    if req.method == "POST":
        sub_model = Subscription
        subcrip = Subs(req.POST)
        email = req.POST["email"]
        objects = sub_model.objects.all()

        if email in [a.email for a in objects]:
            subcrip.add_error("email", "You have already subscribed")
            return render(
                req, "testimonial.html", {"form_err": subcrip.errors.values()}
            )

        if subcrip.is_valid():
            subcrip.save()
            messages.success(req, "You have successfully subscribed")
            send_mail(
                "Thanks for Subscribing",
                "thanks for subscribing",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(req, "testimonial.html")
        else:
            messages.error(req, "Could not subscribe!")
            return render(req, "testimonial.html", {"err_mail": email})

    return render(req, "testimonial.html")


def contact(req):
    if req.method == "POST":
        # our form
        # if its the contact form
        if "contact" in req.POST:
            form = Contactform(req.POST)

            # if form is valid
            if form.is_valid():
                # save it
                form.save()
                # return a success message
                messages.success(req, f"Form Submitted")
                # render the page back
                return redirect("Contact")
            else:
                # get the value of the fields
                form = Contactform()
                name = req.POST["name"]
                email = req.POST["email"]
                phone = req.POST["phone"]
                message = req.POST["message"]
                # pass the value of the fields in to our templates
                messages.error(req, "There is a problem with you form")
                return render(
                    req,
                    "contact.html",
                    {"name": name, "email": email, "message": message, "phone": phone},
                )
        # if our subscibe form was filled
        if "subscribe" in req.POST:

            sub_model = Subscription
            subscribed = Subs(req.POST)
            email = req.POST["email"]
            objects = sub_model.objects.all()

            if email in [a.email for a in objects]:
                subscribed.add_error("email", "You have already subscribed")
                # messages.error(req, "This email is already Subscribed")
                return render(
                    req, "contact.html", {"form_err": subscribed.errors.values()}
                )

            # if our subscription form is valid
            if subscribed.is_valid():
                subscribed.save()

                send_mail(
                    "Thanks for subscribing",
                    f"Dear {email} we noticed you have subscribed,\n Thank you for Subscribing.",
                )

                messages.success(req, "Your have successfully subscribed!")

                return render(req, "contact.html")

            else:
                messages.error(req, "Could not subscribe!")
                return render(req, "contact.html")

    return render(req, "contact.html")


def why(req):
    if req.method == "POST":

        subcrip = Subs(req.POST)
        email = req.POST["email"]
        sub_model = Subscription
        objects = sub_model.objects.all()

        if email in [a.email for a in objects]:
            subcrip.add_error("email", "You have already subscribed")
            return render(req, "why.html", {"form_err": subcrip.errors.values()})

        if subcrip.is_valid():
            subcrip.save()
            messages.success(req, "You have successfully subscribed")
            send_mail(
                "Thanks for Subscribing",
                f"Dear {email}, \n You have successfully subscribed",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(req, "why.html")
        else:
            messages.error(req, "Could not subscribe!")
            return render(req, "why.html", {"err_mail": email})

    return render(req, "why.html")


# Product template
def prod(req):
    if req.method == "POST":
        if "find" in req.POST:
            # get the prodcts
            pd = product

            # get the search query
            query = req.POST["search"]

            # filter the items from the database
            items = pd.objects.filter(Pname__contains=query.title())
            # return our page with results
            return render(req, "product.html", {"query": query, "items": items})

        if "subscribe" in req.POST:
            # databse
            sub_model = Subscription
            # form data
            subscribed = Subs(req.POST)
            # email data from html form
            email = req.POST["email"]
            # objects data from database
            objects = sub_model.objects.all()

            if email in [a.email for a in objects]:
                subscribed.add_error("email", "You have already subscribed")

                return render(
                    req, "product.html", {"form_err": subscribed.errors.values()}
                )
            if subscribed.is_valid():
                # save to the data base
                subscribed.save()
                # send an email
                send_mail(
                    "Thanks for Subscribing",
                    f"Dear {email}, \n You have successfully subscribed",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                # then a success message
                messages.success(req, "You have successfully subscribed")
            # else
            else:
                messages.error(req, "Could not subscribe!")

    return render(req, "product.html")
