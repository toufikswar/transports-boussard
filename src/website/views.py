from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "website/index.html", {})

def test(request):
    return render(request, "website/test.html", {})

def login(request):
    return render(request, "website/login.html", {})

def presentation(request):
    return render(request, "website/presentation.html", {})


def edit(request):
    return render(request, "website/edit.html", {})

