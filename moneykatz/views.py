from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from moneykatz.models import Category, File
from moneykatz.forms import CategoryForm, FileForm, UserProfileForm, UserForm


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/moneykatz/')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/moneykatz/')

            else:
                return HttpResponse('Your account is disabled.')

        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'moneykatz/login.html', {})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            if 'spirit_animal_picture' in request.FILES:
                profile.spirit_animal_picture = request.FILES['spirit_animal_picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'moneykatz/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def add_file(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            if cat:
                document = form.save(commit=False)
                document.category = cat
                document.views = 0
                document.save()

                return category(request, category_name_slug)

        else:
            print form.errors

    else:
        form = FileForm()

    context_dict = {'form': form, 'category': cat, 'category_name_slug': category_name_slug}

    return render(request, 'moneykatz/add_file.html', context_dict)


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print form.errors

    else:
        form = CategoryForm()

    return render(request, 'moneykatz/add_category.html', {'form': form})


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        files = File.objects.filter(category=category)
        context_dict['files'] = files
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug

    except Category.DoesNotExist:
        pass

    return render(request, 'moneykatz/category.html', context_dict)


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    files_list = File.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'files': files_list,
                    'boldmessage': 'I am a bold message from the context dict',
                    }

    return render(request, 'moneykatz/index.html', context_dict)


def about(request):
    context_dict = {'aboutmessage': 'This is a context dict variable'}

    return render(request, 'moneykatz/about.html', context_dict)
