from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from products.models import Product

from .forms import ContactForm

def home_page(request):

    category_student = Product.objects.filter(customer_type=1)
    category_exec    = Product.objects.filter(customer_type=2)
    category_prog    = Product.objects.filter(customer_type=3)
    category_gamer   = Product.objects.filter(customer_type=4)
    category_datasc  = Product.objects.filter(customer_type=5)
    category_home    = Product.objects.filter(customer_type=6)

    context = {
        "title":"Hello there!",
        "content":" Welcome to the homepage.",
        "category_student" : category_student,
        "category_exec" : category_exec,
        "category_prog" : category_prog,
        "category_gamer" : category_gamer,
        "category_datasc" : category_datasc,
        "category_home" : category_home,
    }

    print(category_student,category_exec,category_prog,category_gamer,category_datasc,category_home)

    if request.user.is_authenticated():
        context["premium_content"] = "Premium content"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About Page",
        "content":" Welcome to the about page."
    }
    return render(request, "ecom/home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
