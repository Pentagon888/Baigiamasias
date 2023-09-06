from geopy.distance import geodesic

from .models import AutoService

def search_services(keyword, user_location):
    # Поиск автосервисов по ключевому слову (названию) в имени сервиса
    services = AutoService.objects.filter(name__icontains=keyword)


    # Фильтрация автосервисов по расстоянию от заданного местоположения
    nearest_garages = []
    for service in services:
        service_location = (service.location_lat, service.location_lon)
        distance = geodesic(user_location, service_location).kilometers

        if distance <= 10:  # Предполагаемое максимальное расстояние в километрах от пользователя
            nearest_garages.append({
                'service': service,
                'distance': distance,
            })

    # Сортировка по расстоянию от ближайшего к дальнему
    nearest_garages = sorted(nearest_garages, key=lambda x: x['distance'])

    return nearest_garages
results = search_services
for result in results:
    service = result['service']
    distance = result['distance']
    print(f"Автосервис: {service.name}, Расстояние: {distance} км")