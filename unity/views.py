from django.shortcuts import render

# Create your views here.


def text101(request):
    context_dict = {}
    return render(request, 'unity/text101.html', context_dict)