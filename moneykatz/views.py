from django.shortcuts import render
from moneykatz.models import Category, File
from moneykatz.forms import CategoryForm, FileForm


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
