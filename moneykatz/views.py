from django.shortcuts import render


def index(request):

    context_dict = {'boldmessage': 'I am a bold message from the context dict'}

    return render(request, 'moneykatz/index.html', context_dict)


def about(request):

    context_dict = {'aboutmessage': 'This is a context dict variable'}

    return render(request, 'moneykatz/about.html', context_dict)
