document.addEventListener("DOMContentLoaded", function() {
    fetchLocations();

    // Update sqft display dynamically
    document.getElementById("sqftSlider").addEventListener("input", function() {
        document.getElementById("sqftValue").innerText = this.value;
    });
});

function fetchLocations() {
    fetch("/get_location_names")
        .then(response => response.json())
        .then(data => {
            let locationDropdown = document.getElementById("location");
            locationDropdown.innerHTML = "";

            if (data.locations.length > 0) {
                data.locations.forEach(loc => {
                    let option = document.createElement("option");
                    option.value = loc;
                    option.innerText = loc;
                    locationDropdown.appendChild(option);
                });
            } else {
                locationDropdown.innerHTML = "<option value='' disabled>No locations available</option>";
            }
        })
        .catch(error => console.error("Error fetching locations:", error));
}

function onClickedEstimatePrice() {
    let sqft = parseFloat(document.getElementById("sqftSlider").value);
    let location = document.getElementById("location").value;
    let bhk = parseInt(document.getElementById("bhk").value);
    let bath = parseInt(document.getElementById("bath").value);

    if (!location) {
        alert("Please select a location.");
        return;
    }

    let requestData = { total_sqft: sqft, location: location, bhk: bhk, bath: bath };

    fetch("/predict_home_price", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.estimated_price) {
            document.getElementById("estimatedPrice").innerText = `Estimated Price: ₹${data.estimated_price} Lakhs`;
        } else {
            alert("Error in prediction.");
        }
    })
    .catch(error => console.error("Error in prediction:", error));
}
