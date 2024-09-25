from django.shortcuts import redirect, render
import random
from .forms import UserInfoForm
from .models import UserForm

# Create your views here\.
quotes = [
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
    },
    {
        "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "author": "Winston Churchill",
    },
    {
        "quote": "In the middle of every difficulty lies opportunity.",
        "author": "Albert Einstein",
    },
    {
        "quote": "Your time is limited, so don’t waste it living someone else’s life.",
        "author": "Steve Jobs",
    },
    {
        "quote": "The best way to predict the future is to invent it.",
        "author": "Alan Kay",
    },
    {"quote": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
    {
        "quote": "Whether you think you can or you think you can’t, you’re right.",
        "author": "Henry Ford",
    },
    {
        "quote": "The only limit to our realization of tomorrow is our doubts of today.",
        "author": "Franklin D. Roosevelt",
    },
    {
        "quote": "It does not matter how slowly you go, as long as you do not stop.",
        "author": "Confucius",
    },
    {
        "quote": "Act as if what you do makes a difference. It does.",
        "author": "William James",
    },
]


def custom_page(request):
    return render(request, "project/index.html")


def generate_quote(request):
    choice = random.randint(0, 9)
    selected_quote = quotes[choice]
    print(selected_quote)
    context = {"quotes": selected_quote}
    return render(request, "project/quote.html", context)


def user_form(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user_info = UserForm(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                date_of_birth=form.cleaned_data['dob'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone']
            )
            # Save the user info to the database
            user_info.save()
            return redirect('form-success')
    else:
        form = UserInfoForm()

    return render(request, "project/form.html", {"form": form})

def form_success_view(request):
    return render(request, 'project/success.html')