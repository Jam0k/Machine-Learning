fetch('http://localhost:3000')
  .then(response => response.json())
  .then(data => {
    // Display the JSON data in the "data" div element
    const dataElement = document.getElementById('data');
    dataElement.innerHTML = JSON.stringify(data);
  })
  .catch(error => console.error(error));
