var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var marker = L.marker([51.5, -0.09]).addTo(map);

var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0,
};

function success(pos) {
    var crd = pos.coords;

    var userLocation = [crd.latitude, crd.longitude];
    map.setView(userLocation, 13);

    marker.setLatLng(userLocation);
}

function error(err) {
    console.warn(`ERRO(${err.code}): ${err.message}`);
}

navigator.geolocation.getCurrentPosition(success, error, options);




