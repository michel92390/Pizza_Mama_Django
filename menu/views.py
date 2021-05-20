from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all().order_by("prix")
    # pizzas_names = [pizza.nom + ": £" + str(pizza.prix) for pizza in pizzas]
    # pizzas_names_str = ", ".join(pizzas_names)
    # return HttpResponse("Les pizzas: " + pizzas_names_str)

    return render(request, 'menu/index.html', {'pizzas': pizzas })