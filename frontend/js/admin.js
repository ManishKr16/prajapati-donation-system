function loadSummary() {
  const year = document.getElementById("year").value;

  fetch(`http://localhost:5000/summary/${year}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("total").innerText =
        data.total_collection;
    });
}
