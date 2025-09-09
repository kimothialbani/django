from django.shortcuts import render

from .models import Tour


# from django.http import HttpResponse



def index(request):

    tours = Tour.objects.all()

    context = {'app_app1': tours}

    return render(request, 'app_app1/index.html', context)




