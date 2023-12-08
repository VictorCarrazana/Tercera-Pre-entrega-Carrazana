from django.shortcuts import render

# Create your views here.


# Create your views here.
def cliente_view (request):
    return render(request, "cliente/index.html")