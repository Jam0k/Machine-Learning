fetch('http://localhost:3000')
  .then(response => response.json())
  .then(data => {
    // Create a Chart.js chart using the JSON data
    const chartData = {
      labels: data.map(row => row.account_id),
      datasets: [{
        label: 'Clicks',
        data: data.map(row => row.clicks),
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }]
    };
    const chartOptions = {
      responsive: true,
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    };
    const chart = new Chart(document.getElementById('myChart'), {
      type: 'bar',
      data: chartData,
      options: chartOptions
    });
  })
  .catch(error => console.error(error));
