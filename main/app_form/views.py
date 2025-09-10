from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def home_view(request):

    return render(request, "app_form/home.html")

#define contact_view function to handle contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("home")

    else:
        form = ContactForm()
        context = {"form": form}
        return render(request, "app_form/contact.html", {"form": form})

def contact_success_view(request):
    return render(request, "app_form/contact_success.html")
