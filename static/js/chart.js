const ctx = document.getElementById('cicdChart');

new Chart(ctx, {
    type: 'line',

    data: {
        labels: [
            'Week 1',
            'Week 2',
            'Week 3',
            'Week 4'
        ],

        datasets: [
            {
                label: 'Pipeline Success %',
                data: [72, 84, 91, 98],
                borderWidth: 3,
                tension: 0.4,
                fill: true
            },

            {
                label: 'Deployments',
                data: [10, 18, 26, 35],
                borderWidth: 3,
                tension: 0.4
            }
        ]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        plugins: {
            legend: {
                position: 'top'
            }
        },

        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});