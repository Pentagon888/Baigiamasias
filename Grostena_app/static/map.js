// Инициализация карты
var map = L.map('map').setView([54.75271573295219, 25.24918544483979], 13);

// Используйте слой OpenStreetMap для стандартного стиля карты
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Создание слоя для хранения маркеров сервисов
var serviceMarkersLayer = L.layerGroup().addTo(map);

// Переменные для хранения маркеров и маршрута
var currentLocationMarker, route;

// Функция для отображения маркеров и маршрута на карте
function showOnMap(latitude, longitude, serviceName, phoneNumber) {
    // Удаление предыдущего маршрута (если есть)
    if (route) {
        map.removeControl(route);
        route = null;
    }

    // Удаление предыдущих маркеров сервисов
    serviceMarkersLayer.clearLayers();

    // Добавление маркера выбранного сервиса на карту
    var serviceMarker = L.marker([latitude, longitude]).addTo(serviceMarkersLayer);

    // Создание всплывающего окна с информацией о сервисе
    var popupContent = '<strong>' + serviceName + '</strong><br>' + phoneNumber;
    serviceMarker.bindPopup(popupContent).openPopup();

    // Проверка наличия геолокации в браузере
    if ('geolocation' in navigator) {
        // Запрос на геолокацию
        navigator.geolocation.getCurrentPosition(function (position) {
            var currentLatitude = position.coords.latitude;
            var currentLongitude = position.coords.longitude;

            // Удаление предыдущего маркера текущего местоположения (если есть)
            if (currentLocationMarker) {
                map.removeLayer(currentLocationMarker);
            }

            // Добавление маркера текущего местоположения на карту
            currentLocationMarker = L.marker([currentLatitude, currentLongitude]).addTo(map);

            // Вычисление и отображение маршрута между маркерами
            var waypoints = [
                currentLocationMarker.getLatLng(),
                L.latLng(latitude, longitude)
            ];
            route = L.Routing.control({
                waypoints: waypoints,
                routeWhileDragging: true
            }).addTo(map);
        });
    } else {
        // Геолокация не поддерживается в этом браузере, можно вывести сообщение пользователю
        alert('Геолокация не поддерживается в вашем браузере');
    }
}

// Обработчик нажатия кнопки "Показать на карте"
var showOnMapButtons = document.querySelectorAll('.show-on-map-btn');
showOnMapButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var latitude = parseFloat(this.dataset.latitude);
        var longitude = parseFloat(this.dataset.longitude);
        var serviceName = this.parentElement.querySelector('strong').innerText;
        var phoneNumber = this.parentElement.querySelector('p:nth-child(3)').innerText.split(": ")[1];
        showOnMap(latitude, longitude, serviceName, phoneNumber);
    });
});

// Функция для отображения маркера вашей геолокации на карте
function showUserLocation() {
    // Проверка наличия геолокации в браузере
    if ('geolocation' in navigator) {
        // Запрос на геолокацию
        navigator.geolocation.getCurrentPosition(function (position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            L.marker([latitude, longitude]).addTo(map).bindPopup('Ваша геолокация').openPopup();
        });
    } else {
        // Геолокация не поддерживается в этом браузере, можно вывести сообщение пользователю
        alert('Геолокация не поддерживается в вашем браузере');
    }
}

// Вызов функции для отображения маркера вашей геолокации на карте
showUserLocation();
function showRouteToService()