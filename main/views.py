from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : "Janssen's Bakery",
        'npm' : '2306152102',
        'name': 'Janssen Benedict',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)