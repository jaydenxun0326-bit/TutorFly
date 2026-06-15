from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "pages/login.html", {"form": form})
