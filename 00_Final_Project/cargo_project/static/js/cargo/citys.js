function initAutocomplete() {
        const originInput = document.getElementById('origin');
        const destinationInput = document.getElementById('destination');

        const originAutocomplete = new google.maps.places.Autocomplete(originInput, {
            types: ['(cities)'],
        });

        const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput, {
            types: ['(cities)'],
        });
    }

    // Ініціалізуємо при завантаженні
    window.addEventListener('load', initAutocomplete);