const API_URL = "http://127.0.0.1:8000";

// Toggle bike rent size
function toggleRentSize(isRenting) {
    const rentSizeGroup = document.getElementById('rentSizeGroup');
    const bikeSizeInput = document.getElementById('bikeSize');
    
    if (isRenting) {
        rentSizeGroup.classList.remove('hidden');
        bikeSizeInput.required = true;
    } else {
        rentSizeGroup.classList.add('hidden');
        bikeSizeInput.required = false;
    }
}

// Load participant count on page load
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch(`${API_URL}/participants/`);
        const data = await response.json();
        const countElement = document.getElementById('count');
        if (countElement) {
            countElement.innerText = data.total;
        }
    } catch (error) {
        console.error("Could not load participant count:", error);
    }
});

// Form submission
document.getElementById('registrationForm')?.addEventListener('submit', async function(e) {
    e.preventDefault();

    const isRenting = document.querySelector('input[name="bike"]:checked').value === 'rent';

    const newParticipant = {
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        stravaScore: parseInt(document.getElementById('stravaScore').value),
        weight: parseFloat(document.getElementById('weight').value),
        level: document.getElementById('level').value,
        bikeStatus: isRenting ? `Renting (${document.getElementById('bikeSize').value})` : 'Own Bike',
        needs: document.getElementById('otherNeeds').value,
        droneConsent: document.getElementById('droneConsent').checked
    };

    try {
        const response = await fetch(`${API_URL}/participants/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newParticipant)
        });

        const data = await response.json();

        if (data.error) {
            alert("ACCESS DENIED: " + data.error);
            return;
        }

        window.location.href = 'leaderboard.html';

    } catch (error) {
        alert("Server error. Make sure the backend is running.");
        console.error(error);
    }
});