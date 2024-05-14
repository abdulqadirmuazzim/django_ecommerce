from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Subscription
from .forms import Contactform, Subs

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
            print(form.errors)

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
                messages.error(req, "There is a problem with you form")
                return render(
                    req,
                    "index.html",
                    {
                        "name": name,
                        "email": email,
                        "message": message,
                        "phone": phone,
                        "form_err": form.errors.values(),
                    },
                )
        if "subscribe" in req.POST:
            sub_model = Subscription
            objects = sub_model.objects.all()
            subcrip = Subs(req.POST)

            email = req.POST["email"]

            # if the person has already subscribed then send an error
            if email in [a.email for a in objects]:
                subcrip.add_error("email", "You have already subscribed")
                print(f"{email} is present in the database")
                messages.error(req, "This email is already Subscribed")
                return render(req, "index.html")

            if subcrip.is_valid():
                # subcrip.save()
                messages.success(req, "You have successfully subscribed")
                # send_mail(
                #     "Thanks for Subscribing",
                #     f"Dear {email} thanks for subscribing",
                #     settings.EMAIL_HOST_USER,
                #     [email],
                #     fail_silently=False,
                # )
                return render(req, "index.html")
            else:
                messages.error(req, "Could not subscribe!")
                return render(req, "index.html", {"err_mail": email})

        if "find" in req.POST:
            query = req.POST["search"]
            print(req.POST["search"])
        return render(req, "index.html", {"query": query})

    return render(req, "index.html")


def shop(req):
    if req.method == "POST":

        subcrip = Subs(req.POST)
        email = req.POST["email"]
        sub_model = Subscription
        objects = sub_model.objects.all()

        if email in [a.email for a in objects]:
            subcrip.add_error("email", "You have already subscribed")
            print(f"{email} is present in the database")
            messages.error(req, "This email is already Subscribed")

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
            print(f"{email} is present in the database")
            messages.error(req, "This email is already Subscribed")

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
            # Django doesn't have a phone number field in it's model so we have to do some extra validation for the phone field
            # -------PHOME NUMBER VALIDATION------
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
                print(f"{email} is present in the database")
                messages.error(req, "This email is already Subscribed")
                return render(
                    req, "contact.html", {"form_err": subscribed.errors.as_text()}
                )

            print(subscribed)
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
            print(f"{email} is present in the database")
            messages.error(req, "This email is already Subscribed")

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
            return render(req, "why.html")
        else:
            messages.error(req, "Could not subscribe!")
            return render(req, "why.html", {"err_mail": email})

    return render(req, "why.html")


# Base template
def base(req):
    if req.method == "POST":
        form = Subscription(req.POST)
        print("It worked")
    return render(req, "base.html", {})
