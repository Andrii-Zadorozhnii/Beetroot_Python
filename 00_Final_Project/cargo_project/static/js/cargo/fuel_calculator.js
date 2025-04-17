console.log('fuel_calculator.js загружен');

function calculateFuel() {
    const distance = parseFloat(document.getElementById("distance").value);
    const consumption = parseFloat(document.getElementById("consumption").value);
    const price = parseFloat(document.getElementById("price").value);

    if (isNaN(distance) || isNaN(consumption) || isNaN(price)) {
        document.getElementById("result").innerText = "Пожалуйста, заполните все поля корректно.";
        return;
    }

    const totalLiters = (distance / 100) * consumption;
    const totalCost = totalLiters * price;

    document.getElementById("result").innerText =
        `Вы израсходуете ${totalLiters.toFixed(2)} литров и потратите ${totalCost.toFixed(2)} у.е.`;
}

// Подвешиваем обработчик после загрузки DOM
document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("calculate-button");
    if (button) {
        button.addEventListener("click", calculateFuel);
    }
});