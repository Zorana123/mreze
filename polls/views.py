from django.http import HttpResponse


def index(request):
    return HttpResponse("Danas je divan dan")
