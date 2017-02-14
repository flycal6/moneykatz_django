from datetime import datetime
from secrets import website_email, merchant_id, access_key_id, secret_access_key, client_id, client_secret

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from moneykatz.forms import CategoryForm, FileForm, ContactForm
from moneykatz.models import Category, File

from django.core.mail import send_mail, BadHeaderError


def valentines(request):
    context_dict = {}
    return render(request, 'moneykatz/valentines_day.html', context_dict)


def success(request):
    context_dict = {}
    return render(request, 'moneykatz/success.html', context_dict)


def cancelled(request):
    context_dict = {}
    return render(request, 'moneykatz/cancelled.html', context_dict)


def privacy(request):
    context_dict = {}
    return render(request, 'moneykatz/privacy.html', context_dict)


def payments(request):
    context_dict = {'merchant_id': merchant_id,
                    'client_secret': client_secret,
                    'access_key_id': access_key_id,
                    'secret_access_key': secret_access_key,
                    'client_id': client_id,
                    'test_var': 'context dict working',
                    }
    return render(request, 'moneykatz/payments.html', context_dict)


def sale(request):
    context_dict = {}
    return render(request, 'moneykatz/sale.html', context_dict)


def for_sale(request):
    context_dict = {}
    return render(request, 'moneykatz/forsale.html', context_dict)


def contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # My server doesn't allow email sent from other servers, so sender's address added to message
            # This could be changed to use a Reply-To by changing send_mail() to EmailMessage()
            message = message + '\nSent From: ' + from_email

            try:
                send_mail(subject, message, website_email, [website_email], )
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.  Are trying to hack me?')
            return redirect('thanks')

    else:
        form = ContactForm()

    return render(request, 'moneykatz/contact.html', {'form': form})


def thanks(request):
    context_dict = {}
    return render(request, 'moneykatz/thanks.html', context_dict)


def fixit(request):
    context_dict = {}
    return render(request, 'moneykatz/fixit.html', context_dict)


def gallery(request):
    context_dict = {}
    return render(request, 'moneykatz/gallery.html', context_dict)


def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()

    return HttpResponse(likes)


def blog(request):
    context_dict = {}

    visits = request.session.get('visits')
    context_dict['visits'] = visits
    return render(request, 'moneykatz/blog.html', context_dict)


def jresume(request):
    context_dict = {}
    return render(request, 'moneykatz/jresume.html', context_dict)


def resume(request):
    context_dict = {}
    return render(request, 'moneykatz/resume.html', context_dict)


@staff_member_required
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


@login_required()
def cat_list(request):
    category_list = Category.objects.order_by('-views')
    files_list = File.objects.order_by('-views')[:10]
    context_dict = {'categories': category_list,
                    'files': files_list,
                    'header_text': 'Browse, Upload or Download files',
                    }

    return render(request, 'moneykatz/cat_list.html', context_dict)


@staff_member_required
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


@login_required
def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        files = File.objects.filter(category=category)
        context_dict['files'] = files
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug

        visits = request.session.get('visits')
        context_dict['visits'] = visits

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
    context_dict['visits'] = 'Visits: ' + str(visits)

    response = render(request, 'moneykatz/index.html', context_dict)
    return response


def about(request):
    visits = request.session.get('visits')
    context_dict = {'aboutmessage': 'This is a context dict variable', 'visits': visits}

    return render(request, 'moneykatz/about.html', context_dict)


def index_old(request):
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
    context_dict['visits'] = 'Visits: ' + str(visits)

    response = render(request, 'moneykatz/index_old.html', context_dict)
    return response
