document.getElementById("predictionForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    let disasterType = document.getElementById("disasterType").value;
    let url = "";
    let requestData = {};  

    if (disasterType === "earthquake") {
        url = "/predict_earthquake";
        requestData = {
            "Latitude": parseFloat(document.getElementById("latitude").value),
            "Longitude": parseFloat(document.getElementById("longitude").value),
            "Depth": parseFloat(document.getElementById("depth").value)
        };
    } else if (disasterType === "hurricane") {
        url = "/predict_hurricane";
        requestData = {
            "Maximum Wind": parseFloat(document.getElementById("wind_speed").value),
            "Minimum Pressure": parseFloat(document.getElementById("pressure").value)
        };
    }

    if (Object.values(requestData).some(value => isNaN(value) || value === "")) {
        document.getElementById("result").innerText = "Please fill in all required fields.";
        return;
    }

    try {
        let response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestData)
        });

        let data = await response.json();
        if (data.prediction) {
            document.getElementById("result").innerHTML = `Prediction: ${data.prediction}<br>Precautionary Measures: ${data.precautionary_measures}`;
        } else {
            document.getElementById("result").innerText = "Error: " + data.error;
        }
    } catch (error) {
        document.getElementById("result").innerText = "Error connecting to server!";
    }
});

// Show/hide fields based on disaster type selection
document.getElementById("disasterType").addEventListener("change", function() {
    if (this.value === "earthquake") {
        document.getElementById("earthquakeFields").style.display = "block";
        document.getElementById("hurricaneFields").style.display = "none";
    } else {
        document.getElementById("earthquakeFields").style.display = "none";
        document.getElementById("hurricaneFields").style.display = "block";
    }
});

// Chatbot functionality
async function sendMessage() {
    const userMessage = document.getElementById('userMessage').value;
    if (!userMessage.trim()) return;

    document.getElementById('chatMessages').innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();
    const botMessage = data.response || data.error;

    document.getElementById('chatMessages').innerHTML += `<p><strong>Bot:</strong> ${botMessage}</p>`;
    document.getElementById('userMessage').value = '';
}
