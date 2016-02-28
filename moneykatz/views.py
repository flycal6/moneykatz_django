from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from moneykatz.forms import CategoryForm, FileForm
from moneykatz.models import Category, File


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
    category_list = Category.objects.all()
    files_list = File.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'files': files_list,
                    'boldmessage': 'I am a bold message from the context dict',
                    }

    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[: -7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 7200:
            visits += 1
            reset_last_visit_time = True

    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits

    response = render(request, 'moneykatz/index.html', context_dict)
    return response


def about(request):
    context_dict = {'aboutmessage': 'This is a context dict variable'}

    return render(request, 'moneykatz/about.html', context_dict)
