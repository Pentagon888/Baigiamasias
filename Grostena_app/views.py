import translation as translation
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutoServiceForm
from .models import AutoService, RepairCategory
import logging
from django.conf import settings

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import AutoService  # Импорт модели AutoService

from django.utils.translation import activate, get_language

logger = logging.getLogger(__name__)




def switch_language(request, language):
    # Перенаправляем пользователя обратно на ту же страницу, с которой он пришел
    next_url = request.META.get('HTTP_REFERER', '/')
    response = redirect(next_url)

    # Устанавливаем язык в сессии
    request.session['django_language'] = language

    # Устанавливаем язык в куках
    response.set_cookie('django_language', language)

    return response

def register_service(request):
    if request.method == 'POST':
        form = AutoServiceForm(request.POST)
        if form.is_valid():
            service = form.save()  # Сохраняем сервис в базе данных
            categories = request.POST.getlist('categories')  # Получаем выбранные категории
            service.category.set(categories)  # Устанавливаем выбранные категории для сервиса
            return redirect('search_results')  # Перенаправляем после успешной регистрации
    else:
        form = AutoServiceForm()

    context = {'form': form, 'repair_categories': RepairCategory.objects.all()}
    return render(request, 'service_form.html', context)

def user_context(request):
    return {'user': request.user}


def search_results(request):
    if request.method == 'POST':
        repair_type = request.POST.get('repair_type')
        logger.debug(f"Received repair type: {repair_type}")

        auto_services = AutoService.objects.filter(Q(category__name__iexact=repair_type) | Q(category__name__icontains=repair_type))
        logger.debug(f"Found {auto_services.count()} services for repair type: {repair_type}")

        repair_categories = RepairCategory.objects.all()

        return render(request, 'search_results.html', {'services': auto_services, 'repair_categories': repair_categories})

    return render(request, 'search_results.html', {'services': [], 'repair_categories': []})

def index(request):

    response = render(request, 'index.html', {'user': request.user})
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
    return render(request, 'index.html', {'user': request.user})


def redirect_to_index(request):
    return redirect('index')
def service_form(request):
    # Здесь можно добавить логику для обработки данных формы, если это требуется
    return render(request, 'service_form.html')



def service_details(request, service_id):
    service = get_object_or_404(AutoService, id=service_id)
    return render(request, 'service_details.html', {'service': service})


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматический вход после регистрации
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)

def user_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'user_form.html', {'form': form, 'user_already_exists': True})
            else:
                user = form.save()
                # Остальная логика после успешной регистрации
                return render(request, 'user_form_success.html', {'name': username})
    else:
        form = UserCreationForm()
    return render(request, 'user_form.html', {'form': form, 'user_already_exists': False})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Перенаправление на главную страницу
    return render(request, 'login.html')
