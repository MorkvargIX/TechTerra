//document.addEventListener('DOMContentLoaded', function() {
//    var ctx = document.getElementById('exchangeRateChart').getContext('2d');
//
//    var data = {
//        labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"], // Здесь должны быть ваши даты
//        datasets: [{
//            label: 'USD to UAH Exchange Rate',
//            data: [28.5, 28.7, 28.8, 28.6, 28.4], // Здесь должны быть ваши курсы
//            borderColor: 'green',
//            borderWidth: 3,
//            fill: false
//        }]
//    };
//
//    var options = {
//        responsive: true,
//        maintainAspectRatio: false,
//        scales: {
//            y: {
//                beginAtZero: false
//            }
//        }
//    };
//
//    var exchangeRateChart = new Chart(ctx, {
//        type: 'line',
//        data: data,
//        options: options
//    });
//});

document.addEventListener("DOMContentLoaded", function() {
    const prevRate = 27.00; // Предыдущий курс валюты (замените на фактический)
    const currentRate = 27.50; // Текущий курс валюты (замените на фактический)

    const exchangeRate = document.getElementById("exchangeRate");
    const arrow = document.getElementById("arrow");

    exchangeRate.textContent = currentRate.toFixed(2); // Отображение текущего курса

    if (currentRate > prevRate) {
        arrow.classList.add("arrow", "up"); // Добавление классов "arrow" и "up"
    } else if (currentRate < prevRate) {
        arrow.classList.add("arrow", "down"); // Добавление классов "arrow" и "down"
    }
});
