fetch('http://localhost:3000')
  .then(response => response.json())
  .then(data => {
    // Create the HTML table with the data
    let tableHtml = '<div class="table-responsive"><table class="table"><thead><tr><th>Campaign Name</th><th>Linear Regression</th><th>Polynomial Regression</th><th>Random Forest Regression</th><th>Logistic Regression</th></tr></thead><tbody>';
    data.forEach(row => {
      tableHtml += `<tr><td>${row.campaign_name}</td><td>${row.linear_regression}</td><td>${row.polynomial_regression}</td><td>${row.random_forest_regression}</td><td>${row.logistic_regression}</td></tr>`;
    });
    tableHtml += '</tbody></table></div>';

    // Display the HTML table in the "data" div element
    const dataElement = document.getElementById('data');
    dataElement.innerHTML = tableHtml;
  })
  .catch(error => console.error(error));
