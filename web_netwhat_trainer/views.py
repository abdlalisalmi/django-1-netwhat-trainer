from django.shortcuts import render


def home_view(request):
    context = {}
    template_name = 'home.html'
    return render(request, template_name, context)