from django.shortcuts import render
from Grostena_app.models import  AutoService, RepairCategory

def index(request):
    return render(request, 'index.html')

def search_results(request):
    if request.method == 'POST':
        repair_type = request.POST.get('repair_type')
        try:
            category = RepairCategory.objects.get(name=repair_type)
        except RepairCategory.DoesNotExist:
            return render(request, 'search_results.html', {'services': []})

        auto_services = AutoService.objects.filter(category=category)
        return render(request, 'search_results.html', {'services': auto_services})

    return render(request, 'search_results.html', {'services': []})

def service_details(request, service_id):
    try:
        service = AutoService.objects.get(id=service_id)
    except AutoService.DoesNotExist:
        service = None

    return render(request, 'service_details.html', {'service': service})