function initMap() {
    const myLatLng = { lat: 13.779954, lng: 100.559903 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 18,
        center: myLatLng,
    });
    new google.maps.Marker({
        position: myLatLng,
        map,
        animation: google.maps.Animation.DROP,
    });
}