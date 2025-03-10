'use strict';

async function fetchCargoData() {
    try {
        const response = await fetch("/api/cargo/");
        return await response.json();
    } catch (error) {
        console.error("Ошибка загрузки данных:", error);
        return [];
    }
}

document.addEventListener("DOMContentLoaded", async () => {
    const cargoData = await fetchCargoData();
    new Commutes(CONFIGURATION, cargoData);
});

class Commutes {
    constructor(configuration, cargoData) {
        this.configuration = configuration;
        this.commutesMap = null;
        this.directionsRenderer = null;
        this.cargoData = cargoData;

        this.initMapView();
        this.renderCargoCards();
    }

    initMapView() {
        this.commutesMap = new google.maps.Map(
            document.querySelector(".map-view"),
            this.configuration.mapOptions
        );
        this.directionsRenderer = new google.maps.DirectionsRenderer();
        this.directionsRenderer.setMap(this.commutesMap);
    }

    renderCargoCards() {
        const cargoCardsContainer = document.getElementById("cargo-cards");
        this.cargoData.forEach((cargo) => {
            const card = document.createElement("div");
            card.className = "cargo-card";
            card.innerHTML = `
                <h3>${cargo.name}</h3>
                <p><strong>From:</strong> ${cargo.origin}</p>
                <p><strong>To:</strong> ${cargo.destination}</p>
            `;
            card.addEventListener("click", () => this.handleCargoClick(cargo));
            cargoCardsContainer.appendChild(card);
        });
    }

   handleCargoClick(cargo) {
    console.log('Clicked Cargo:', cargo); // Проверим, что передается в cargo
    this.updateRouteInfo({
        origin: cargo.origin,
        destination: cargo.destination,
    });

    this.getDirections(cargo.origin, cargo.destination).then((response) => {
        if (!response || !response.routes || response.routes.length === 0) {
            console.error('No route found for this cargo.');
            return;
        }

        const leg = response.routes[0].legs[0];
        this.updateRouteInfo({
            origin: cargo.origin,
            destination: cargo.destination,
            distance: leg.distance.text,
            duration: leg.duration.text,
        });

        this.directionsRenderer.setDirections(response);
    }).catch((error) => {
        console.error('Error fetching directions:', error);
    });
}

    getDirections(origin, destination) {
    const request = {
        origin,
        destination,
        travelMode: this.configuration.defaultTravelMode,
    };

    const directionsService = new google.maps.DirectionsService();

    return new Promise((resolve, reject) => {
        directionsService.route(request, (result, status) => {
            if (status === google.maps.DirectionsStatus.OK) {
                resolve(result);
            } else {
                reject(new Error('Directions request failed due to ' + status));
            }
        });
    });
}

    updateRouteInfo(data) {
        document.getElementById("origin-info").textContent = data.origin;
        document.getElementById("destination-info").textContent = data.destination;
        document.getElementById("distance-info").textContent = data.distance || "N/A";
        document.getElementById("duration-info").textContent = data.duration || "N/A";
    }
}

const CONFIGURATION = {
  defaultTravelMode: "DRIVING", // Режим передвижения по умолчанию (автомобиль)
  distanceMeasurementType: "METRIC", // Метрическая система (км, м)
  mapOptions: {
    center: { lat: 50.4503596, lng: 30.5241376 }, // Начальный центр карты (Киев)
    fullscreenControl: false,
    mapTypeControl: true,
    streetViewControl: true,
    zoom: 6,
    zoomControl: true,
    maxZoom: 20,
    mapId: "",
  },
  mapsApiKey: "AIzaSyCfB1EAVuIvBnDjolH6SOtuami3gaLuSNI",
};

