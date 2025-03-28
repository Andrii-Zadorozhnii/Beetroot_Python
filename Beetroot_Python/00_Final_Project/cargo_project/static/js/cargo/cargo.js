      let map;
      let directionsService;
      let directionsRenderer;
      let geocoder;

      // Инициализация карты
      function initMap() {
        const defaultOrigin = { lat: 0, lng: 0 }; // Сан-Франциско
        const defaultDestination = { lat: 0, lng: 0 }; // Лос-Анджелес

        map = new google.maps.Map(document.getElementById("map"), {
          zoom: 7,
          center: defaultOrigin,
        });

        directionsService = new google.maps.DirectionsService();
        directionsRenderer = new google.maps.DirectionsRenderer({
          map: map,
        });

        geocoder = new google.maps.Geocoder();

        // Маркеры для начальной и конечной точки
        new google.maps.Marker({
          position: defaultOrigin,
          map: map,
          title: "Origin",
        });

        new google.maps.Marker({
          position: defaultDestination,
          map: map,
          title: "Destination",
        });

        // Отображение маршрута
        displayRoute(defaultOrigin, defaultDestination);
      }

      // Функция обновления карты при клике на карточку
      function updateMap(origin, destination) {
        geocodeAddress(origin, destination);
      }

      // Функция геокодирования
      function geocodeAddress(origin, destination) {
        geocoder.geocode({ address: origin }, function (results, status) {
          if (status === "OK") {
            const originCoords = results[0].geometry.location;

            geocoder.geocode({ address: destination }, function (results, status) {
              if (status === "OK") {
                const destinationCoords = results[0].geometry.location;

                // Обновляем информацию о маршруте
                document.getElementById("route-origin").innerText = origin;
                document.getElementById("route-destination").innerText = destination;

                // Рисуем новый маршрут на карте
                displayRoute(originCoords, destinationCoords);
              } else {
                console.error("Geocode failed for destination: " + status);
              }
            });
          } else {
            console.error("Geocode failed for origin: " + status);
          }
        });
      }

      // Функция для отображения маршрута на карте
      function displayRoute(origin, destination) {
        const request = {
          origin: origin,
          destination: destination,
          travelMode: google.maps.TravelMode.DRIVING,
        };

        directionsService.route(request, function (result, status) {
          if (status === google.maps.DirectionsStatus.OK) {
            directionsRenderer.setDirections(result);
          } else {
            console.error("Directions request failed: " + status);
          }
        });
      }

      // Функция для фильтрации карточек товаров
      function filterCargos() {
        const originSelect = document.getElementById("origin-select");
        const destinationSelect = document.getElementById("destination-select");
        const selectedOrigin = originSelect.value;
        const selectedDestination = destinationSelect.value;

        const cargoCards = document.querySelectorAll(".cargo-card");

        cargoCards.forEach((card) => {
          const origin = card.getAttribute("data-origin");
          const destination = card.getAttribute("data-destination");

          const originMatch = !selectedOrigin || origin === selectedOrigin;
          const destinationMatch = !selectedDestination || destination === selectedDestination;

          if (originMatch && destinationMatch) {
            card.style.display = "block";
          } else {
            card.style.display = "none";
          }
        });
      }

      // Инициализация карты при загрузке
      window.onload = initMap;