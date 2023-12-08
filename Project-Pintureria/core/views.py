from django.shortcuts import render
from. import views
from producto import views

# Create your views here.
def core_view (request):
    return render(request, "core/index.html")

